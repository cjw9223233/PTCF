# 🧠 Prompt Guide v3.0

### 控制思考，而不只是控制輸出

一套分層式的 Prompt 參考與最佳實踐。從日常的四行 prompt，到決策分析、AI 代理與團隊標準化，都用同一套結構。

---

## ⚡ 30 秒快速開始

**有效輸出 = Persona × Task × Context × Format**

```markdown
Persona：你是一位【角色】，讀者是【對象】
Task：請【動詞 + 具體目標】
Context：背景【…】；目標【…】；限制【…，因為…】
Format：【條列 / 表格 / Markdown】，【長度】

<document>
（要處理的資料）
</document>
```

這四項寫清楚，就能解決大多數日常任務。需要更深入時，再往下加層。

---

## 🏗 四層架構

| 層級 | 模組 | 回答的問題 | 適用 |
| --- | --- | --- | --- |
| [**Level 1 核心層**](docs/01-core-ptcf.md) | Persona、Task、Context、Format | 做什麼？給誰？在什麼條件下？輸出什麼形式？ | 約 80% 日常任務 |
| [**Level 2 進階控制層**](docs/02-advanced-control.md) | Depth、Reasoning Mode、Constraint | 想多深？怎麼想？邊界在哪？ | 深度分析、架構設計 |
| [**Level 3 決策與驗證層**](docs/03-decision-validation.md) | Decision、Stress Test、Self-check | 所以該怎麼做？哪裡會崩？有沒有漏洞？ | 技術選型、投資判斷 |
| [**Level 4 模板與知識層**](docs/04-template-system.md) | 模板庫、Output SLA | 如何每次都寫好、別人也能用？ | 團隊標準化 |

### 依任務價值選層

| 任務價值 | 使用層級 | 例子 |
| --- | --- | --- |
| 低 | Level 1 | 寫一段自我介紹 |
| 中 | Level 1 + 2 | 設計高流量 API 架構 |
| 高 | Level 1 + 2 + 3 | SVN 轉 Git 的技術選型 |
| 團隊標準化 | 全部 + [評估](docs/07-evaluation-iteration.md) | 共用模板、自動化流程 |

```
小任務 → 用核心
大任務 → 加深度
決策任務 → 啟動閉環
團隊使用 → 標準化模板 + 評估
```

---

## 📚 文件導覽

### 分層指南

1. [Level 1｜核心層：PTCF 四要素](docs/01-core-ptcf.md)
2. [Level 2｜進階控制層：Depth、Reasoning Mode、Constraint](docs/02-advanced-control.md)
3. [Level 3｜決策與驗證層：Decision、Stress Test、Self-check](docs/03-decision-validation.md)
4. [Level 4｜模板與知識層：模板庫與 Output SLA](docs/04-template-system.md)

### 與時俱進

5. [現代最佳實踐：推理模型、結構化與長文件](docs/05-modern-practices.md)
6. [Agent 與 Context Engineering](docs/06-agent-context-engineering.md)
7. [評估與迭代：Metrics Layer](docs/07-evaluation-iteration.md)
8. [與 AI 協作開發流程](docs/08-ai-dev-workflow.md)

### 模板（可直接複製）

- [萬用模板](docs/templates/general.md)：極簡版、完整版、JSON 版
- [程式與專案模板](docs/templates/programming.md)：專案掃描、架構設計、重構
- [投資分析模板](docs/templates/investment.md)：分析類 prompt 寫法示範
- [prompt-template.json](docs/templates/prompt-template.json)：統一 JSON 結構

---

## ⚠ 常見誤區

| 誤區 | 正確做法 |
| --- | --- |
| 模組越多越好 | 依任務價值啟用對應層級 |
| 每次都寫「請逐步思考」 | 推理模型會自己思考；說清楚目標與理由更有效 |
| 用「嚴禁」「絕對」加強語氣 | 一般語氣 + 說明原因 |
| 只給 Persona 不給資料 | Context 才是降低幻覺的關鍵 |
| 一個 prompt 做所有事 | 拆成多步驟（Prompt Chaining） |
| 看一次結果就定案 | 用固定測試案例比較版本 |

---

## 🏁 核心原則

- ✅ 控制思考，而不只是控制輸出
- ✅ 用結構降低不確定性
- ✅ 說明理由，而不是加重語氣
- ✅ 用決策閉環避免空洞分析
- ✅ 用壓力測試確保穩健性
- ✅ 用測試案例驗證 prompt，而不是憑感覺

---

## 🔗 舊網址對照（v2.0 → v3.0）

| 舊文件 | 新位置 |
| --- | --- |
| `docs/PTCF.md` | [docs/01-core-ptcf.md](docs/01-core-ptcf.md) |
| `docs/prompt-eng-guide-personal.md` | [docs/02-advanced-control.md](docs/02-advanced-control.md)、[docs/03-decision-validation.md](docs/03-decision-validation.md) |
| `docs/few-shot-cot-golden-template.md` | [docs/templates/general.md](docs/templates/general.md)、[docs/templates/programming.md](docs/templates/programming.md)、[docs/templates/investment.md](docs/templates/investment.md) |
| `docs/prog-pm-context.md` | [docs/templates/programming.md](docs/templates/programming.md) |

版本演進見 [CHANGELOG](CHANGELOG.md)。

---

> Prompt 不只是提問，而是一套思考架構。
> 控制輸入結構，就能控制輸出品質；控制思考流程，就能控制決策結果。
