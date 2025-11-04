# Compatibility Testing - 相容性測試

## 📋 概述

本目錄包含針對 Local LLM API 的相容性測試案例，重點驗證系統對多語言、特殊字元等多樣輸入的處理能力與回應格式一致性。相容性測試確保系統能正確支援不同語言、符號及編碼，提升國際化與多元應用場景的穩定性。

## 🎯 測試設計目的

### 核心目標
1. **驗證多語言支援**：測試 LLM API 是否能正確處理中、英、日、韓、法、德等多語言 prompt
2. **特殊字元相容性**：驗證系統對 emoji、特殊符號、換行、長字串等輸入的處理能力
3. **回應格式一致性**：確保不同語言與符號下，API 回應格式皆符合預期 schema
4. **提升國際化體驗**：確保多語系用戶皆能獲得正確回應

### 測試策略
根據**相容性分析 (Compatibility Analysis)** 測試技術，針對以下維度進行測試：
- **多語言**：涵蓋常見語言（中、英、日、韓、法、德、西、俄、泰、阿拉伯等）
- **特殊字元**：emoji、符號、換行、多行、超長字串等
- **fixtures 結合**：測試資料集中於 fixtures 目錄，方便擴充與維護

## 📝 測試案例說明

### TC-COMPATIBILITY-0003: 多語言輸入格式相容性
**檔案**: `test_multilingual_input_schema.py`

**測試目的**：
- 驗證系統能否正確處理多語言 prompt 並回傳正確格式
- 確認所有語言皆符合回應 schema

**測試設計**：
```python
@pytest.mark.parametrize("prompt,lang", [...])
```
- 測試資料集中於 `fixtures/prompts_multilingual.json`
- 自動化測試多組語言輸入

**預期結果**：
- ✅ HTTP 狀態碼應為 200 (成功)
- ✅ 回應 JSON 應符合 schema
- ✅ 所有語言皆能正確處理

---

### TC-COMPATIBILITY-0004: 特殊字元/編碼相容性
**檔案**: `test_special_char_schema.py`

**測試目的**：
- 驗證系統對 emoji、特殊符號、換行、多行、超長字串等輸入的處理能力
- 確認回應格式皆正確

**測試設計**：
```python
@pytest.mark.parametrize("prompt,case", [...])
```
- 測試資料集中於 `fixtures/prompts_specialchar.json`
- 自動化測試多組特殊字元輸入

**預期結果**：
- ✅ HTTP 狀態碼應為 200 (成功)
- ✅ 回應 JSON 應符合 schema
- ✅ 所有特殊字元皆能正確處理

## 🔧 執行方式

### 執行所有相容性測試
```bash
pytest tests/compatibility/ -v --alluredir=allure-results
```

### 執行單一測試案例
```bash
pytest tests/compatibility/test_multilingual_input_schema.py -v
pytest tests/compatibility/test_special_char_schema.py -v
```

### 生成 Allure 報告
```bash
allure serve allure-results
```

## 📊 測試覆蓋率

| 測試維度 | 測試案例 | 覆蓋率 |
|---------|---------|--------|
| 多語言 | TC-COMPATIBILITY-0003 | ✅ |
| 特殊字元 | TC-COMPATIBILITY-0004 | ✅ |

## 🔍 測試重點

### 1. fixtures 集中管理
- 測試資料與邏輯分離，方便擴充與維護
- 新增語言或特殊字元只需編輯 JSON 檔

### 2. Schema 驗證
- 所有回應皆需通過 schema_validator 驗證
- 確保格式一致性

### 3. 國際化與多元應用
- 支援多語言、多符號，提升產品國際化能力

## 🎓 相關文件

- [Test Framework Design](../../docs/Test_Framework_Design.md)
- [Test Strategy](../../docs/Test_Strategy.md)
- [Allure Report Guide](../../docs/Allure_Report_Guide.md)

## 📌 注意事項

1. **語言覆蓋**：可依需求擴充更多語言
2. **符號多樣性**：可依需求擴充更多符號、emoji
3. **fixtures 維護**：測試資料建議集中於 fixtures 方便團隊協作

## 🐛 已知問題

- 部分語言或符號在不同模型下回應格式可能略有差異
- 超長字串的處理效能依賴於模型本身

## 📅 更新記錄

- 2025-11-04: 初始版本，包含多語言與特殊字元相容性測試案例
