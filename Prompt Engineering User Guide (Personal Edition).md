# 🧠 Prompt Engineering 一頁式操作指南

（高品質輸出 = 控制思考系統）

---

## 一、核心公式

> **Persona × Task × Context × Format × Depth × Decision × Stress Test × Self-check**

如果只記得一句話：

> 不只控制「要什麼」，還要控制「怎麼思考」。

---

# 二、8 大模組極簡說明

| 模組              | 作用     | 你在做什麼   |
| --------------- | ------ | ------- |
| **Persona**     | 指定思考身份 | 控制專業框架  |
| **Task**        | 指定任務   | 控制行為方向  |
| **Context**     | 補充背景   | 降低猜測誤差  |
| **Format**      | 指定輸出形式 | 提高可用性   |
| **Depth**       | 控制分析層級 | 提高深度    |
| **Decision**    | 產出行動方案 | 從思考到決策  |
| **Stress Test** | 挑戰觀點   | 提高穩健性   |
| **Self-check**  | 自我審查   | 提高品質穩定度 |

---

# 三、操作流程（使用順序）

### Step 1️⃣ 先定義角色（Persona）

> 我要用什麼專業視角思考？

例：

* 資深顧問
* 架構師
* 投資分析師
* 初學者講師
* 批判型思考者

---

### Step 2️⃣ 明確任務（Task）

> 我要它做什麼？

類型：

* 摘要整理
* 分析拆解
* 挑戰觀點
* 教學說明
* 專案解析
* 決策建議

---

### Step 3️⃣ 補足背景（Context）

> 在什麼情境下？

包含：

* 目標
* 對象
* 限制條件
* 原始資料

---

### Step 4️⃣ 指定格式（Format）

> 我要怎麼呈現？

例：

* 條列
* 表格
* Markdown
* JSON
* README

---

### Step 5️⃣ 控制深度（Depth）

> 要多深？

選項：

* 基礎說明
* 結構性分析
* 第一性原理
* 底層邏輯
* 系統思考（找因果循環）
* 風險分析（最壞情境）
* 機率思考（不確定性）
* 槓桿思維（小投入大回報）
* 博弈思考（看利益衝突）

---

### Step 6️⃣ 要求決策輸出（Decision）

> 所以我該怎麼做？

要求：

* 提供 3 種策略
* 排序優先順序
* 評估風險與報酬
* 給出具體行動

---

### Step 7️⃣ 進行壓力測試（Stress Test）

> 這套說法哪裡會崩？

要求：

* 反對觀點
* 最大盲點
* 最壞情境
* 隱含假設

> 思維壓縮能力測試

要求完整、詳細： 

* 請濃縮成 150 字版本
* 再給我 30 字版本
* 再給我一句話版本

---

### Step 8️⃣ 要求自我檢查（Self-check）

> 有沒有邏輯漏洞？

檢查：

* 推理跳躍？
* 證據不足？
* 過度簡化？
* 可補強處？

---

# 四、快速使用模板（完整版）

可直接複製：

```
你是一位【角色 Persona】。

【Task 任務】
請完成：
1.
2.

【Context 情境】
背景：
目標：
限制：
資料：
<<<
>>>

【Format 格式】
請用【條列 / 表格 / Markdown】輸出。

【Depth 深度】
請用【第一性原理 / 系統思考 / 結構性分析】進行。

【Decision 決策】
請提供可執行建議與優先順序。

【Stress Test 壓力測試】
請指出可能盲點與反對觀點。

【Self-check 自我檢查】
請檢查是否存在推理漏洞與隱含假設。
```

```json

{
  "prompt_template": {
    "role": {
      "description": "角色 Persona",
      "instruction": "你是一位【角色 Persona】"
    },
    "task": {
      "description": "任務",
      "instruction": "請完成",
      "items": [
        "任務項目 1",
        "任務項目 2"
      ]
    },
    "context": {
      "description": "情境",
      "components": {
        "background": {
          "label": "背景",
          "content": ""
        },
        "goal": {
          "label": "目標",
          "content": ""
        },
        "constraints": {
          "label": "限制",
          "content": "禁用簡體字"
        },
        "data": {
          "label": "資料",
          "content": ""
        }
      }
    },
    "format": {
      "description": "格式",
      "instruction": "請用【條列 / 表格 / Markdown】輸出",
      "options": [
        "條列",
        "表格",
        "Markdown"
      ]
    },
    "depth": {
      "description": "深度",
      "instruction": "請用【第一性原理 / 系統思考 / 結構性分析】進行",
      "methods": [
        "第一性原理",
        "系統思考",
        "結構性分析"
      ]
    },
    "decision": {
      "description": "決策",
      "instruction": "請提供可執行建議與優先順序"
    },
    "stress_test": {
      "description": "壓力測試",
      "instruction": "請指出可能盲點與反對觀點"
    },
    "self_check": {
      "description": "自我檢查",
      "instruction": "請檢查是否存在推理漏洞與隱含假設"
    }
  }
}

```

---

# 五、極簡日常版（30 秒寫完）

```
角色：
任務：
背景：
格式：
深度：
決策：
反向測試：
自我檢查：
資料：
<<<
>>>
```

---

# 六、三個使用層級

| 層級 | 用法                                | 適用情境 |
| -- | --------------------------------- | ---- |
| 基礎 | Persona + Task + Context + Format | 日常整理 |
| 進階 | + Depth + Decision                | 分析決策 |
| 高階 | + Stress Test + Self-check        | 重要判斷 |

---

# 七、核心心法

1. 先定義思考框架，再要答案
2. 先控制推理深度，再看結論
3. 先壓力測試，再做決策

真正高手不是問問題的人。

而是設計思考流程的人。

---
