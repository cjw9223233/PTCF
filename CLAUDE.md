# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A documentation-only repository (no code, no build, no tests) for **Prompt Guide v3.0 / PTCF** — a layered prompt-engineering reference and best-practice guide written in Traditional Chinese. It is published as a GitHub Pages site via Jekyll. Write and edit content in Traditional Chinese (繁體中文, Taiwan usage) in a neutral reference-document voice — no chat-style phrasing ("你好", "我幫你", "下一步建議").

## Publishing

- `.github/workflows/jekyll-gh-pages.yml` builds the repo root with `actions/jekyll-build-pages` and deploys to GitHub Pages on every push to `master` (or manual dispatch). Every committed `.md` file becomes a page, so don't commit unrelated notes under the repo.
- `_config.yml` (repo root) sets the theme, title, description and `exclude` (keeps `CLAUDE.md` off the site). Keep it at the root.
- Cross-page links use relative `.md` paths (GitHub Pages' jekyll-relative-links rewrites them). Avoid `#anchor` links to Chinese headings — generated ids are unreliable. Avoid `{{` / `{%` in content (Liquid).
- No local Jekyll setup (no Gemfile); the real build check is the Actions run after push.

## Content architecture

Core formula: **有效輸出 = Persona × Task × Context × Format** (PTCF). The framework has four layers, one doc each; each concept is defined once in its layer doc and only linked from elsewhere:

| File | Content |
| --- | --- |
| `README.md` | Site home: quick start, layer overview, layer-selection table, navigation, old→new URL map |
| `docs/01-core-ptcf.md` | Level 1: Persona / Task / Context / Format |
| `docs/02-advanced-control.md` | Level 2: Depth / Reasoning Mode / Constraint (incl. CoT guidance for reasoning models) |
| `docs/03-decision-validation.md` | Level 3: 8-step decision loop / Stress Test / Self-check |
| `docs/04-template-system.md` | Level 4: template library index, Output SLA |
| `docs/05`–`08` | Modern practices, agent/context engineering, evaluation (Metrics Layer), AI dev workflow |
| `docs/templates/` | Copy-ready templates (general, programming, investment) + `prompt-template.json` |
| `tutorial/index.html` | Self-contained interactive tutorial (inline CSS/JS, no front matter, so Jekyll copies it as-is). Lessons summarize docs 01–07; includes a level quiz and a prompt builder |

Conventions:

- Canonical module names: Persona, Task, Context, Format, Depth, Reasoning Mode, Constraint, Decision, Stress Test, Self-check. When renaming a concept, update README, all `docs/` and `CHANGELOG.md`.
- `docs/templates/prompt-template.json` is the single source for the JSON schema (`version`, `role`, `task.items`, `context.{background,goal,constraints,data}`, `format.{type,length}`, `depth`, `reasoning_mode`, `decision.items`, `stress_test.questions`, `self_check.items`). Every JSON example in Markdown must use the same keys, and Markdown template sections must map one-to-one to them.
- Data inside prompts is wrapped in XML-style tags (`<document>`, `<code>`, `<examples>`), not `<<< >>>`.
- Docs end with a prev / home / next navigation line; keep it in sync when adding or reordering docs.
- The tutorial page restates docs content; when a doc's concepts or examples change, update the matching lesson in `tutorial/index.html`. Its builder (`buildJSON`) must emit only keys from `prompt-template.json`. Links from the tutorial to docs use `../docs/<name>.html` (Jekyll's output names), and links into it use `tutorial/`.
- Investment content stays illustrative: keep the disclaimer and use fictional examples, not real tickers or figures.
- Record notable changes in `CHANGELOG.md`.
