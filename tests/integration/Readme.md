# Integration Testing - 整合測試

## 📋 概述

本目錄包含針對 Local LLM API 的整合測試案例，重點驗證多模組、多語言、多階段流程的協作與一致性，確保系統整體功能協同運作。

## 🎯 測試設計目的

### 核心目標
1. **驗證多模組協作**：測試 LLM API 與其他模組（如後處理、不同模型）整合時的正確性
2. **多語言一致性**：驗證多語言下的回應一致性
3. **多階段流程**：測試多階段產生與後處理流程

### 測試策略
- **產生與後處理**：驗證產生內容後的自動後處理流程
- **多語言一致性**：同一請求於不同語言下的回應一致性
- **多模型一致性**：同一請求於不同模型下的回應一致性
- **多階段流程**：多階段產生與後處理的協作

## 📝 測試案例說明

### TC-INTEGRATION-0001: 產生與後處理
**檔案**: `test_generate_and_postprocess.py`
- 測試產生內容後自動後處理流程

### TC-INTEGRATION-0002: 多語言一致性
**檔案**: `test_multi_language_consistency.py`
- 驗證多語言下回應一致性

### TC-INTEGRATION-0003: 多模型一致性
**檔案**: `test_multi_model_consistency.py`
- 驗證多模型下回應一致性

### TC-INTEGRATION-0004: 多階段產生與後處理
**檔案**: `test_multi_stage_generate_postprocess.py`
- 測試多階段產生與後處理流程

## 🔧 執行方式

```bash
pytest tests/integration/ -v --alluredir=allure-results
```

## 📊 測試覆蓋率

| 測試維度 | 測試案例 | 覆蓋率 |
|---------|---------|--------|
| 產生與後處理 | TC-INTEGRATION-0001 | ✅ |
| 多語言一致性 | TC-INTEGRATION-0002 | ✅ |
| 多模型一致性 | TC-INTEGRATION-0003 | ✅ |
| 多階段流程 | TC-INTEGRATION-0004 | ✅ |

## 🔍 測試重點
- 多模組協作需正確
- 多語言/多模型一致性需驗證
- 多階段流程需無誤

## 🎓 相關文件
- [Test Framework Design](../../docs/Test_Framework_Design.md)
- [Test Strategy](../../docs/Test_Strategy.md)

## 📅 更新記錄
- 2025-11-04: 初始版本，包含 4 個整合測試案例
