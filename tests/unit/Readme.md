# Unit Testing - 單元測試

## 📋 概述

本目錄包含針對 Local LLM API 的單元測試案例，重點驗證各獨立模組、功能、API 回應格式等基礎元件的正確性與穩定性。

## 🎯 測試設計目的

### 核心目標
1. **驗證基礎功能正確性**：測試各獨立模組、API 回應格式、資料解析等
2. **確保版本相容性**：多版本請求與回應的一致性
3. **提升開發效率**：快速發現基礎錯誤，縮短回歸週期

### 測試策略
- **連線測試**：API 連線與回應格式驗證
- **回應格式測試**：產生回應、解析回應的正確性
- **多版本一致性**：多版本請求與回應一致性

## 📝 測試案例說明

### TC-UNIT-0001: 連線測試
**檔案**: `test_connection.py`
- 驗證 API 連線與回應格式

### TC-UNIT-0002: 回應格式產生
**檔案**: `test_generate_response_format.py`
- 測試回應格式產生正確性

### TC-UNIT-0003: 產生成功測試
**檔案**: `test_generate_success.py`
- 驗證產生功能正確性

### TC-UNIT-0004: 多版本一致性
**檔案**: `test_multiple_version_requests_consistency.py`
- 驗證多版本請求一致性

### TC-UNIT-0005: 回應解析測試
**檔案**: `test_parse_generate_response.py`
- 測試回應解析正確性

### TC-UNIT-0006: 版本回應格式
**檔案**: `test_version_response_format.py`
- 驗證版本回應格式正確性

## 🔧 執行方式

```bash
pytest tests/unit/ -v --alluredir=allure-results
```

## 📊 測試覆蓋率

| 測試維度 | 測試案例 | 覆蓋率 |
|---------|---------|--------|
| 連線 | TC-UNIT-0001 | ✅ |
| 回應格式產生 | TC-UNIT-0002 | ✅ |
| 產生成功 | TC-UNIT-0003 | ✅ |
| 多版本一致性 | TC-UNIT-0004 | ✅ |
| 回應解析 | TC-UNIT-0005 | ✅ |
| 版本格式 | TC-UNIT-0006 | ✅ |

## 🔍 測試重點
- 各模組獨立驗證
- 回應格式、資料解析需正確
- 多版本相容性

## 🎓 相關文件
- [Test Framework Design](../../docs/Test_Framework_Design.md)
- [Test Strategy](../../docs/Test_Strategy.md)

## 📅 更新記錄
- 2025-11-04: 初始版本，包含 6 個單元測試案例
