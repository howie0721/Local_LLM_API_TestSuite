# Local LLM API - 自動化測試套件

## 📋 專案概述

本專案為 **Local LLM API** 的完整自動化測試套件，採用 pytest 框架與資料驅動測試（Data-Driven Testing）設計，涵蓋單元測試、整合測試、端對端測試、效能測試、安全性測試等多維度驗證，確保 LLM API 在各種情境下的穩定性、正確性與安全性。

### 🎯 測試目標
- ✅ **功能正確性**：驗證 API 各項功能符合規格與預期
- ✅ **穩定可靠**：確保系統在各種極端與異常情境下穩定運作
- ✅ **效能優化**：監控系統效能、資源使用與瓶頸
- ✅ **安全防護**：防止惡意輸入、敏感資訊洩漏與攻擊
- ✅ **易於維護**：採用模組化設計與資料驅動測試，提升可維護性

---

## 🏗️ 測試金字塔架構

本專案測試設計遵循 **測試金字塔（Test Pyramid）** 原則，確保測試覆蓋率、執行效率與維護成本的最佳平衡：

```
                    /\
                   /  \
                  / E2E \                ← 端對端測試（少量、慢速、高價值）
                 /--------\
                /          \
               / Integration \           ← 整合測試（中量、中速、多模組）
              /--------------\
             /                \
            /  Component Tests \         ← 元件測試（中量、快速、模組驗證）
           /--------------------\
          /                      \
         /      Unit Tests        \      ← 單元測試（大量、快速、基礎驗證）
        /--------------------------\
```

### 測試層級說明

#### 🔷 第一層：Unit Tests（單元測試）
- **比例**：40%
- **特性**：執行速度快、測試粒度細、數量最多
- **目錄**：`tests/unit/`
- **範例**：API 連線測試、回應格式驗證、資料解析測試

#### 🔶 第二層：Component Tests（元件測試）
- **比例**：30%
- **特性**：驗證獨立模組或元件功能
- **目錄**：`tests/boundary/`、`tests/compatibility/`、`tests/error_handling/`
- **範例**：邊界值測試、多語言相容性、錯誤處理

#### 🔵 第三層：Integration Tests（整合測試）
- **比例**：20%
- **特性**：驗證多模組協作與資料流
- **目錄**：`tests/integration/`、`tests/regression/`
- **範例**：多模型一致性、產生與後處理流程、回歸驗證

#### 🟢 第四層：End-to-End Tests（端對端測試）
- **比例**：10%
- **特性**：模擬完整用戶流程、執行時間較長
- **目錄**：`tests/e2e/`
- **範例**：多輪對話、FAQ 查詢、多語言切換

#### 🔴 橫切關注點（Cross-Cutting Concerns）
- **效能測試**：`tests/performance/`（JMeter）
- **穩定性測試**：`tests/stability/`（JMeter）
- **安全性測試**：`tests/security/`
- **易用性測試**：`tests/usability/`

---

## 📂 測試目錄結構

```
tests/
├── unit/                          # 單元測試（基礎功能驗證，API/資料解析）
│   ├── test_connection.py
│   ├── test_generate_response_format.py
│   ├── test_generate_success.py
│   ├── test_multiple_version_requests_consistency.py
│   ├── test_parse_generate_response.py
│   ├── test_version_response_format.py
│   └── Readme.md
├── boundary/                      # 邊界值測試（極端輸入驗證）
│   ├── test_prompt_length_empty.py
│   ├── test_prompt_length_max.py
│   ├── test_prompt_length_over.py
│   ├── test_prompt_max_tokens.py
│   └── Readme.md
├── compatibility/                 # 相容性測試（多語言、特殊字元）
│   ├── test_multilingual_input_schema.py
│   ├── test_special_char_schema.py
│   ├── test_api_schema.py
│   ├── test_error_response_schema.py
│   └── Readme.md
├── error_handling/                # 錯誤處理測試（異常情境驗證）
│   ├── test_api_notfound.py
│   ├── test_missing_required_param.py
│   ├── test_method_not_allowed.py
│   ├── test_cannot_connect.py
│   └── Readme.md
├── integration/                   # 整合測試（多模組協作）
│   ├── test_generate_and_postprocess.py
│   ├── test_multi_language_consistency.py
│   ├── test_multi_model_consistency.py
│   ├── test_multi_stage_generate_postprocess.py
│   └── Readme.md
├── e2e/                           # 端對端測試（完整流程驗證）
│   ├── test_code_and_explanation.py
│   ├── test_faq_knowledge_query.py
│   ├── test_multi_turn_conversation.py
│   ├── test_multilingual_switch.py
│   └── Readme.md
├── regression/                    # 回歸測試（功能穩定性驗證）
│   ├── test_fixed_prompt_regression.py
│   ├── test_multi_turn_regression.py
│   ├── test_output_format_regression.py
│   ├── test_regression_math_consistency.py
│   └── Readme.md
├── security/                      # 安全性測試（防護能力驗證）
│   ├── test_content_filter.py
│   ├── test_model_refusal_keywords.py
│   ├── test_prompt_injection.py
│   ├── test_sensitive_info_leak.py
│   └── Readme.md
├── performance/                   # 效能測試（JMeter，壓力/併發/長輸入）
│   ├── ollama_llama3_single_request.jmx
│   ├── ollama_llama3_long_prompt.jmx
│   ├── ollama_llama3_concurrent_requests.jmx
│   ├── ollama_llama3_stress_test.jmx
│   └── Readme.md
├── stability/                     # 穩定性測試（JMeter，長時間/記憶體/重啟）
│   ├── ollama_llama3_long_context_stability.jmx
│   ├── ollama_llama3_long_duration_stress.jmx
│   ├── ollama_llama3_memory_leak_simple.jmx
│   ├── ollama_llama3_restart_recovery.jmx
│   └── Readme.md
├── usability/                     # 易用性測試（回應格式/表格/段落/程式碼）
│   ├── test_response_codeblock.py
│   ├── test_response_format.py
│   ├── test_response_paragraphs.py
│   ├── test_response_table.py
│   └── Readme.md
├── fixtures/                      # 測試資料（資料驅動測試）
│   ├── prompts_multilingual.json
│   ├── prompts_specialchar.json
│   └── Readme.md
├── conftest.py                    # pytest 共用 fixture 定義
└── README.md                      # 本檔案
```

---

## 📝 測試類型詳細說明

### 1️⃣ Unit Testing - 單元測試
**目錄**：`tests/unit/`  
**測試案例數**：6  
**執行速度**：⚡ 快速

**核心目標**：
- 驗證 API 基礎功能正確性
- 測試連線、回應格式、資料解析等獨立模組
- 確保多版本 API 請求一致性

**詳細說明**：[unit/Readme.md](unit/Readme.md)

---

### 2️⃣ Boundary Testing - 邊界值測試
**目錄**：`tests/boundary/`  
**測試案例數**：4  
**執行速度**：🐢 中速

**核心目標**：
- 驗證系統對極端輸入的容錯能力
- 測試空字串、超長輸入、最大上限等邊界情境
- 確保系統不會因極端輸入而崩潰

**測試維度**：
- 最小值邊界（空字串）
- 最大值邊界（1024 字元）
- 超出範圍（8192 字元）
- Token 邊界（高 token 數）

**詳細說明**：[boundary/Readme.md](boundary/Readme.md)

---

### 3️⃣ Compatibility Testing - 相容性測試
**目錄**：`tests/compatibility/`  
**測試案例數**：14（含參數化）  
**執行速度**：🐢 中速

**核心目標**：
- 驗證多語言支援（中、英、日、韓、法、德、西、俄、泰、阿拉伯等）
- 測試特殊字元、emoji、換行、多行等輸入
- 確保回應格式一致性

**資料驅動**：
- 使用 `fixtures/prompts_multilingual.json`（10 組語言）
- 使用 `fixtures/prompts_specialchar.json`（4 組特殊情境）

**詳細說明**：[compatibility/Readme.md](compatibility/Readme.md)

---

### 4️⃣ Error Handling Testing - 錯誤處理測試
**目錄**：`tests/error_handling/`  
**測試案例數**：4  
**執行速度**：⚡ 快速

**核心目標**：
- 驗證 API 錯誤回應正確性
- 測試 404、400、405、連線失敗等異常情境
- 確保錯誤訊息明確且不洩漏敏感資訊

**詳細說明**：[error_handling/Readme.md](error_handling/Readme.md)

---

### 5️⃣ Integration Testing - 整合測試
**目錄**：`tests/integration/`  
**測試案例數**：4  
**執行速度**：🐢 中速

**核心目標**：
- 驗證多模組協作正確性
- 測試產生與後處理流程
- 確保多語言、多模型下的一致性

**詳細說明**：[integration/Readme.md](integration/Readme.md)

---

### 6️⃣ End-to-End Testing - 端對端測試
**目錄**：`tests/e2e/`  
**測試案例數**：4  
**執行速度**：🐌 慢速

**核心目標**：
- 模擬實際用戶操作流程
- 測試多輪對話、FAQ 查詢、程式碼解釋等完整場景
- 驗證多語言切換正確性

**詳細說明**：[e2e/Readme.md](e2e/Readme.md)

---

### 7️⃣ Regression Testing - 回歸測試
**目錄**：`tests/regression/`  
**測試案例數**：4  
**執行速度**：🐢 中速

**核心目標**：
- 確保新功能或修正不影響既有功能
- 驗證固定 prompt、多輪對話、輸出格式等回歸場景
- 針對曾發生過的 bug 進行追蹤驗證

**詳細說明**：[regression/Readme.md](regression/Readme.md)

---

### 8️⃣ Security Testing - 安全性測試
**目錄**：`tests/security/`  
**測試案例數**：4  
**執行速度**：🐢 中速

**核心目標**：
- 驗證內容過濾與敏感詞彙處理
- 防止 prompt injection 攻擊
- 確保敏感資訊不洩漏

**詳細說明**：[security/Readme.md](security/Readme.md)

---

### 9️⃣ Performance Testing - 效能測試
**目錄**：`tests/performance/`  
**測試案例數**：4（JMeter）  
**執行速度**：🐌 慢速

**核心目標**：
- 驗證單一請求、併發請求、長 prompt 等效能表現
- 模擬極端負載壓力測試
- 監控反應速度與資源使用

**工具**：Apache JMeter

**詳細說明**：[performance/Readme.md](performance/Readme.md)

---

### 🔟 Stability Testing - 穩定性測試
**目錄**：`tests/stability/`  
**測試案例數**：4（JMeter）  
**執行速度**：🐌 慢速

**核心目標**：
- 驗證長時間運作穩定性
- 測試大量上下文與記憶體洩漏
- 模擬異常重啟恢復能力

**工具**：Apache JMeter

**詳細說明**：[stability/Readme.md](stability/Readme.md)

---

### 1️⃣1️⃣ Usability Testing - 易用性測試
**目錄**：`tests/usability/`  
**測試案例數**：4  
**執行速度**：⚡ 快速

**核心目標**：
- 驗證回應格式易讀性
- 測試程式碼區塊、表格、段落等輸出格式
- 確保用戶體驗良好

**詳細說明**：[usability/Readme.md](usability/Readme.md)

---

## 🔧 執行測試

### 前置需求
```bash
# 安裝 Python 依賴
pip install -r requirements.txt

# 安裝 Allure（可選，用於生成測試報告）
# macOS: brew install allure
# Windows: scoop install allure
# Linux: 參考官網安裝說明
```

### 執行全部測試
```bash
# 執行所有 pytest 測試
pytest tests/ -v --alluredir=allure-results

# 生成 Allure 報告
allure serve allure-results
```

### 執行特定類型測試
```bash
# 單元測試
pytest tests/unit/ -v

# 邊界值測試
pytest tests/boundary/ -v

# 相容性測試
pytest tests/compatibility/ -v

# 錯誤處理測試
pytest tests/error_handling/ -v

# 整合測試
pytest tests/integration/ -v

# 端對端測試
pytest tests/e2e/ -v

# 回歸測試
pytest tests/regression/ -v

# 安全性測試
pytest tests/security/ -v

# 易用性測試
pytest tests/usability/ -v
```

### 執行效能與穩定性測試（JMeter）
```bash
# 需先安裝 Apache JMeter
# 單一請求效能測試
jmeter -n -t tests/performance/ollama_llama3_single_request.jmx -l results.jtl

# 併發請求效能測試
jmeter -n -t tests/performance/ollama_llama3_concurrent_requests.jmx -l results.jtl

# 長上下文穩定性測試
jmeter -n -t tests/stability/ollama_llama3_long_context_stability.jmx -l results.jtl
```

### 執行單一測試檔案
```bash
pytest tests/unit/test_connection.py -v
pytest tests/boundary/test_prompt_length_max.py -v
pytest tests/e2e/test_multi_turn_conversation.py -v
```

---

## 📊 測試覆蓋率統計

| 測試類型 | 測試案例數 | 覆蓋範圍 | 執行速度 | 優先級 |
|---------|----------|---------|---------|--------|
| 單元測試 | 6 | API 基礎功能 | ⚡ 快速 | 🔴 高 |
| 邊界值測試 | 4 | 極端輸入 | 🐢 中速 | 🔴 高 |
| 相容性測試 | 14 | 多語言、特殊字元 | 🐢 中速 | 🟠 中 |
| 錯誤處理測試 | 4 | 異常情境 | ⚡ 快速 | 🔴 高 |
| 整合測試 | 4 | 多模組協作 | 🐢 中速 | 🟠 中 |
| 端對端測試 | 4 | 完整流程 | 🐌 慢速 | 🟠 中 |
| 回歸測試 | 4 | 功能穩定性 | 🐢 中速 | 🔴 高 |
| 安全性測試 | 4 | 安全防護 | 🐢 中速 | 🔴 高 |
| 效能測試 | 4 | 效能表現 | 🐌 慢速 | 🟡 低 |
| 穩定性測試 | 4 | 長時間運作 | 🐌 慢速 | 🟡 低 |
| 易用性測試 | 4 | 回應格式 | ⚡ 快速 | 🟡 低 |
| **總計** | **56** | **全方位覆蓋** | - | - |

---

## 🎯 資料驅動測試（Data-Driven Testing）

本專案採用 **資料驅動測試** 設計，測試資料與測試邏輯分離，提升測試可維護性與擴充性。

### Fixtures 目錄
**路徑**：`tests/fixtures/`

**目前資料檔案**：
- `prompts_multilingual.json`：10 組多語言 prompt（中、英、日、韓、法、德、西、俄、泰、阿拉伯）
- `prompts_specialchar.json`：4 組特殊字元測試資料（emoji、符號、換行、超長字串）

### 使用範例
```python
import pytest
import json
import os

@pytest.mark.parametrize("prompt,lang", [
    (item["prompt"], item["lang"]) 
    for item in json.load(open("tests/fixtures/prompts_multilingual.json", encoding="utf-8"))
])
def test_multilingual(ollama_client, validator, prompt, lang):
    messages = [{"role": "user", "content": prompt}]
    response = ollama_client.chat(messages=messages)
    validator.assert_status_code(response, 200)
```

**詳細說明**：[fixtures/Readme.md](fixtures/Readme.md)

---

## 🏆 測試設計最佳實踐

### 1️⃣ 遵循測試金字塔原則
- 單元測試（40%）：快速、大量、基礎驗證
- 元件測試（30%）：中速、中量、模組驗證
- 整合測試（20%）：中慢、適量、協作驗證
- 端對端測試（10%）：慢速、少量、流程驗證

### 2️⃣ 資料驅動測試
- 測試資料與邏輯分離
- 集中於 `fixtures/` 目錄管理
- 使用 `pytest.mark.parametrize` 參數化測試

### 3️⃣ 獨立性與可重複性
- 每個測試應獨立執行，不依賴其他測試
- 測試結果應可重複驗證

### 4️⃣ 明確的測試命名
- 測試檔案：`test_<功能描述>.py`
- 測試函式：`test_<測試案例編號>_<測試目的>`

### 5️⃣ Allure 報告整合
- 使用 `@allure.title()` 標註測試標題
- 使用 `--alluredir` 生成測試報告

### 6️⃣ 持續整合（CI/CD）
- 自動化執行測試套件
- 監控測試覆蓋率與通過率

---

## 📚 相關文件

- [Test Framework Design](../docs/Test_Framework_Design.md) - 測試框架設計文件
- [Test Strategy](../docs/Test_Strategy.md) - 測試策略與規劃
- [Test Plan](../docs/Test_Plan.md) - 測試計畫
- [Allure Report Guide](../docs/Allure_Report_Guide.md) - Allure 報告使用指南
- [Test Pyramid](../docs/Test_Pyramid.md) - 測試金字塔說明
- [CI/CD Integration](../docs/CI_CD_Integration.md) - CI/CD 整合指南

---

## 🐛 已知問題與限制

1. **模型差異**：不同 LLM 模型對相同輸入的回應可能略有差異
2. **語言處理**：部分語言或特殊字元在不同模型下表現不一
3. **效能測試**：需依實際環境調整併發數與負載參數
4. **Timeout 設定**：長輸入或複雜場景需適當調整 timeout

---

## 🔄 版本更新記錄

### v1.0.0 (2025-11-04)
- ✅ 初始版本發布
- ✅ 完成 11 類測試（單元、邊界值、相容性、錯誤處理、整合、E2E、回歸、安全性、效能、穩定性、易用性）
- ✅ 總計 56 個測試案例
- ✅ 導入資料驅動測試（fixtures）
- ✅ 整合 Allure 報告
- ✅ 建立完整測試金字塔架構

---

## 👥 貢獻指南

歡迎貢獻測試案例或改進建議！請參考 [Contributing.md](../docs/Contributing.md)

---

## 📧 聯絡資訊

如有問題或建議，請聯繫測試團隊或提交 Issue。

---

**測試是品質的保證，自動化是效率的關鍵！** 🚀
