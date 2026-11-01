# CHANGELOG

## v3.2（2026-11）

- Level 4 新增「架構：Prompt as Code」：模板中繼資料改以 `docs/templates/registry.json` 為唯一來源，模板卡需與其一致。
- 新增 `prompt-template.schema.json`（JSON Schema 2020-12）；`prompt-template.json` 以 `$schema` 引用。
- 新增 `evals/<id>/cases.json`：五個模板各 5 個測試案例，含 prompt injection 案例。
- 新增 `scripts/validate.py` 與 `validate` workflow：檢查連結、JSON、registry、模板卡、測試案例與內容慣例。
- 撰寫規範新增防範 prompt injection、共用片段、prompt caching 結構；生命週期新增跨模型可攜性；發布新增可觀測性。
- 程式與專案模板升至 4.0.0：改為共同骨架＋六個子模板（專案掃描、除錯、程式碼審查、重構、架構與技術選型、寫測試）；新增對話與代理的分工表、貼上程式碼前的機密檢查、不能改的範圍、驗收要求與 diff 輸出；實例改用 #private；測試案例擴充為 8 個，含除錯、審查、機密與行為不變案例。
- 萬用模板新增「共用片段」（版本 3.1.0）；07 說明測試案例檔格式；教學 Lesson 4 新增「自動驗證」卡片。

## v3.1（2026-11）

- [Level 4](docs/04-template-system.md) 改寫為模板營運手冊：模板卡（中繼資料）、撰寫規範（`【變數】`、XML 標籤、限制附理由）、生命週期與重新驗證時機、發布到工具（Prompt as Code）、團隊治理。
- Output SLA 新增事實可追溯、格式合規、安全與隱私三個面向，並為每個面向標註建議量測方式。
- 新增 [Agent 任務模板](docs/templates/agent-task.md) 與 [摘要與文件審閱模板](docs/templates/summary-review.md)；既有三個模板加上模板卡。
- 選層對照表統一放在 README，Level 4 改為連結。
- 教學頁 Lesson 4 同步新增 SLA 面向與模板營運重點。

## v3.0.1（2026-11）

- 互動教學頁 UX 優化：閱讀進度條、課程完成追蹤與「前往下一課」、續讀入口、主題切換、程式碼複製按鈕、決策步驟可跳轉與全部展開、測驗作答進度與複習建議、產生器的復原提示與下載 .md／.json、手機版「查看輸出」按鈕；補強鍵盤操作、跳到主要內容連結與減少動態效果支援。

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
- [互動式教學頁](tutorial/)：分課講解四層架構、選層小測驗、Prompt 產生器（輸出符合 prompt-template.json 的 JSON）。

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
