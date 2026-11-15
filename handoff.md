# Handoff（2026-11-15）

> 工作交接筆記。**不要 commit**：repo 中每個 `.md` 都會變成網站頁面。

## 目前狀態

- 分支 `feat/eval-runner-and-v3.4`
  - 已 commit：`2072cf9`
  - 已 push 到 origin
  - validate CI 通過
- **尚未合併到 master，網站尚未部署**（push 到 master 就會部署）。
- 執行器**還沒用真的模型跑過**，所以 registry 的 `verified.models` 仍是空的。

## 這個分支做了什麼（v3.4）

- 新增 `scripts/run_evals.py`：
  - 讀 `evals/<id>/cases.json`，組成 prompt 後呼叫模型。
  - 用 `must_include`／`must_not` 做規則檢查；`--judge-model` 可選擇依 `rubric` 評分。
  - 結果寫到 `evals/<id>/results/<模型>-<日期>.json`。
  - `--update-registry`：完整案例集全數通過、且沒有觸發 fallback，才把模型寫進 `verified.models`。
- `scripts/validate.py`：`verified.models` 列出的模型，必須有該版本全數通過的 results 檔。
- `docs/06`：新增第 5–8 節（子代理、Skills、MCP、prompt injection／致命三要素），原本的「護欄」順延為第 9 節。
- `docs/04`、`docs/07` 補上執行器用法；04 第 6 節連到 06。
- `_config.yml` 加入 `lang: zh-Hant-TW`。
- README：
  - 標題拿掉版本號。
  - 教學時間改為約 25 分鐘。
  - 舊網址對照移到 CHANGELOG 的 v3.0 條目。
  - 模板描述與 04 對齊。
- 教學頁：拿掉「v3.0」字樣，更新 06 卡片描述。
- CHANGELOG 新增 v3.4；CLAUDE.md 補上執行器規則。

## 回來後的下一步

1. **決定是否合併部署**。合併方式與先前相同：

   ```bash
   git checkout master
   git pull
   git merge --no-ff feat/eval-runner-and-v3.4
   git push
   ```

   部署後檢查網站的 `<html lang>` 是否為 `zh-Hant-TW`，以及教學頁顯示正常。
2. **（選擇性，會花費 API 費用）實跑評估**：約 31 次呼叫，加上 judge 會變兩倍。
   1. 先執行 `python scripts/run_evals.py --dry-run`，確認案例數與呼叫次數。
   2. 實跑一個模板：`python scripts/run_evals.py --template general`。
   3. 看過 results 檔之後，加 `--update-registry` 重跑。
   4. 要宣稱跨模型可用，至少跑兩個 `--model`。
   5. 把 results 檔與 registry 的變更 commit。
3. **後續建議**（這次刻意沒做）：
   - 部署 workflow 加上 `needs: validate`。
   - 升級 Actions（Node 20 淘汰警告）。
   - 為 registry 與 cases 各寫一份 JSON Schema。
   - 新增 `.gitignore`（`.claude/`、`handoff.md`）與 issue／PR 模板。
   - 刪除 7 個已合併的分支：
     - `docs/agent-subtemplate-usage`
     - `docs/template-ops`
     - `docs/v3-restructure`
     - `feat/agent-task-v2`
     - `feat/template-architecture`
     - `feat/tutorial-page`
     - `feat/tutorial-ux`

## 環境備忘

- Python：`C:\Users\cjw\AppData\Local\Programs\Python\Python313\python.exe`，不在 bash 的 PATH 中。已用 `--user` 安裝 `jsonschema==4.23.0` 與 `anthropic`（2.8.0）。
- 本機沒有 `gh` CLI。查 CI 改用 GitHub API：`https://api.github.com/repos/cjw9223233/PTCF/actions/runs?branch=<分支>`。
- 執行 Python 時加上 `PYTHONIOENCODING=utf-8`，否則中文輸出會亂碼。
- `.claude/` 是未追蹤的本機設定，不要 commit。
- 計畫檔：`C:\Users\cjw\.claude\plans\repo-repo-prompt-compressed-alpaca.md`
