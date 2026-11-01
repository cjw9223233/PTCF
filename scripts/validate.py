"""Validate the PTCF docs site: links, JSON against the schema, the template
registry, eval cases, and content conventions.

Usage: python scripts/validate.py   (requires: pip install jsonschema)
Exits non-zero and lists every problem when a check fails.
"""
import json
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "docs" / "templates"
MIN_CASES = 5

errors = []


def fail(path, msg):
    errors.append(f"{path.relative_to(ROOT).as_posix()}: {msg}")


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        fail(path, f"JSON 無法解析：{e}")
        return None


def schema_errors(validator, obj):
    return [f"{'/'.join(map(str, e.path)) or '(root)'}: {e.message}" for e in validator.iter_errors(obj)]


schema = load_json(TEMPLATES / "prompt-template.schema.json")
Draft202012Validator.check_schema(schema)
validator = Draft202012Validator(schema)

md_files = [ROOT / "README.md", ROOT / "CHANGELOG.md"] + sorted((ROOT / "docs").rglob("*.md"))

LINK = re.compile(r"\]\(([^)\s#]+)(#[^)]*)?\)")
JSON_BLOCK = re.compile(r"```json\n(.*?)```", re.S)
CHAT_TONE = re.compile(r"你好|我幫你|下一步建議|以下為你")
CARD_ROW = re.compile(r"^\| (版本|狀態) \| ([^|]+?) \|", re.M)

# 1. Markdown: links, JSON blocks, conventions
for md in md_files:
    text = md.read_text(encoding="utf-8").replace("\r\n", "\n")
    for m in LINK.finditer(text):
        target = m.group(1)
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (md.parent / target).exists():
            fail(md, f"連結目標不存在：{target}")
        if m.group(2):
            fail(md, f"避免使用中文標題錨點連結：{target}{m.group(2)}")
    for i, block in enumerate(JSON_BLOCK.findall(text), 1):
        try:
            obj = json.loads(block)
        except json.JSONDecodeError as e:
            fail(md, f"第 {i} 個 JSON 區塊無法解析：{e}")
            continue
        for err in schema_errors(validator, obj):
            fail(md, f"第 {i} 個 JSON 區塊不符合 schema：{err}")
    if "{{" in text or "{%" in text:
        fail(md, "含有 {{ 或 {%，會被 Jekyll 當成 Liquid 語法")
    if CHAT_TONE.search(text):
        fail(md, "含有對話口吻語句")
    if re.search(r"^<<<", text, re.M):
        fail(md, "資料區隔請用 XML 標籤，不要用 <<< >>>")

# 2. Template JSON
tpl = load_json(TEMPLATES / "prompt-template.json")
if tpl is not None:
    for err in schema_errors(validator, tpl):
        fail(TEMPLATES / "prompt-template.json", f"不符合 schema：{err}")

# 3. Registry, template cards, evals
registry_path = TEMPLATES / "registry.json"
registry = load_json(registry_path) or {"templates": []}
seen = set()
for t in registry["templates"]:
    tid = t.get("id")
    if tid in seen:
        fail(registry_path, f"重複的模板 id：{tid}")
    seen.add(tid)
    md = ROOT / t["file"]
    if not md.exists():
        fail(registry_path, f"{tid} 的檔案不存在：{t['file']}")
        continue
    card = dict(CARD_ROW.findall(md.read_text(encoding="utf-8")))
    if "| 模板卡 |" not in md.read_text(encoding="utf-8"):
        fail(md, "缺少模板卡")
    if card.get("版本") != t["version"]:
        fail(md, f"模板卡版本 {card.get('版本')} 與 registry {t['version']} 不一致")
    if not card.get("狀態", "").startswith(t["status"]):
        fail(md, f"模板卡狀態 {card.get('狀態')} 與 registry {t['status']} 不一致")
    if t["status"] == "已停用" and not t.get("replaced_by"):
        fail(registry_path, f"{tid} 已停用但沒有 replaced_by")
    if t["status"] != "已發布":
        continue
    evals_path = ROOT / (t.get("evals") or "")
    if not t.get("evals") or not evals_path.exists():
        fail(registry_path, f"{tid} 狀態為已發布，但缺少測試案例檔")
        continue
    evals = load_json(evals_path)
    if evals is None:
        continue
    if evals.get("template") != tid:
        fail(evals_path, f"template 應為 {tid}")
    if evals.get("template_version") != t["version"]:
        fail(evals_path, f"template_version {evals.get('template_version')} 與 registry {t['version']} 不一致")
    cases = evals.get("cases", [])
    if len(cases) < MIN_CASES:
        fail(evals_path, f"已發布模板至少需要 {MIN_CASES} 個測試案例，目前 {len(cases)} 個")
    for c in cases:
        for key in ("id", "input", "rubric"):
            if key not in c:
                fail(evals_path, f"案例 {c.get('id', '?')} 缺少 {key}")
        for err in schema_errors(validator, c.get("input", {})):
            fail(evals_path, f"案例 {c.get('id')} 的 input 不符合 schema：{err}")

for md in sorted(TEMPLATES.glob("*.md")):
    if md.relative_to(ROOT).as_posix() not in {t["file"] for t in registry["templates"]}:
        fail(md, "模板沒有登記在 registry.json")

# 4. Tutorial links to docs (../docs/x.html -> docs/x.md)
tutorial = ROOT / "tutorial" / "index.html"
for href in re.findall(r'href="\.\./([^"]+)"', tutorial.read_text(encoding="utf-8")):
    source = ROOT / re.sub(r"\.html$", ".md", href)
    if not source.exists():
        fail(tutorial, f"連結目標不存在：../{href}")

if errors:
    print(f"驗證失敗，共 {len(errors)} 項：")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"驗證通過：{len(md_files)} 份 Markdown、{len(registry['templates'])} 個模板。")
