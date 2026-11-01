# CHANGELOG

## v3.0（2026-11）

**結構重整**

- 依四層架構重新拆分文件：`docs/01`～`04` 各講一層，模板集中到 `docs/templates/`。
- 合併重複內容：四要素、Stress Test、Self-check 只在各自的章節定義一次。
- 統一 JSON 結構為 [prompt-template.json](docs/templates/prompt-template.json)，所有範例都採用同一組欄位。
- 移除文件中的 AI 對話殘留語句，改為中性的參考文件語氣；修正錯字。
- 投資模板加上免責聲明，範例數據改為虛構示意。
- README 改為首頁與導覽，附上舊網址對照。

**新增內容**（涵蓋原規劃的 v2.1 Metrics Layer 與 v2.2 AI Workflow Automation）

- [現代最佳實踐](docs/05-modern-practices.md)：推理模型時代的寫法、XML 標籤、長文件技巧、降低幻覺、Prompt Chaining、Meta-prompting、結構化輸出。
- [Agent 與 Context Engineering](docs/06-agent-context-engineering.md)：給 AI 代理的任務寫法、專案說明檔、工具脈絡與護欄。
- [評估與迭代](docs/07-evaluation-iteration.md)：成功標準、測試案例、評分表、LLM-as-judge、版本比較。
- [與 AI 協作開發流程](docs/08-ai-dev-workflow.md)：從想法到 PR 的完整流程與護欄清單。

**觀念更新**

- 推理模型不必再寫「請逐步思考」；改為說清楚目標、限制與理由。
- 限制條件附上原因，取代「嚴禁」等強烈語氣。
- 資料改用 XML 標籤區隔（`<<< >>>` 仍可用）。

## v2.0

- 從 v1.0 的 8 個平行模組，重構為四層架構（Core、Advanced Control、Decision & Validation、Knowledge & Template）。
- 加入 8 步決策閉環與 Output SLA。

## v1.0

- 8 模組平行結構：Persona × Task × Context × Format × Depth × Decision × Stress Test × Self-check。
- 程式與專案模板、Few-shot + CoT 黃金模板。
