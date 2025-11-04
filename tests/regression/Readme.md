# Regression Testing - 回歸測試

## 📋 概述

本目錄包含針對 Local LLM API 的回歸測試案例，重點驗證系統在功能更新、修正後，核心功能是否仍維持正確，避免新舊版本間產生不預期的錯誤。

## 🎯 測試設計目的

### 核心目標
1. **驗證功能穩定性**：確保新功能或修正不影響既有功能
2. **多輪對話與格式一致性**：驗證多輪對話、輸出格式、數學運算等回歸場景
3. **歷史問題追蹤**：針對曾發生過的 bug 進行回歸驗證

### 測試策略
- **固定 prompt 回歸**：驗證固定 prompt 下的回應一致性
- **多輪對話回歸**：多輪互動流程的正確性
- **輸出格式回歸**：回應格式、欄位、結構等一致性
- **數學運算回歸**：數學相關功能的正確性

## 📝 測試案例說明

### TC-REGRESSION-0001: 固定 prompt 回歸
**檔案**: `test_fixed_prompt_regression.py`
- 驗證固定 prompt 下回應是否一致

### TC-REGRESSION-0002: 多輪對話回歸
**檔案**: `test_multi_turn_regression.py`
- 驗證多輪對話流程回歸

### TC-REGRESSION-0003: 輸出格式回歸
**檔案**: `test_output_format_regression.py`
- 驗證回應格式一致性

### TC-REGRESSION-0004: 數學運算回歸
**檔案**: `test_regression_math_consistency.py`
- 驗證數學運算相關功能回歸

## 🔧 執行方式

```bash
pytest tests/regression/ -v --alluredir=allure-results
```

## 📊 測試覆蓋率

| 測試維度 | 測試案例 | 覆蓋率 |
|---------|---------|--------|
| 固定 prompt | TC-REGRESSION-0001 | ✅ |
| 多輪對話 | TC-REGRESSION-0002 | ✅ |
| 輸出格式 | TC-REGRESSION-0003 | ✅ |
| 數學運算 | TC-REGRESSION-0004 | ✅ |

## 🔍 測試重點
- 功能更新後需全數通過
- 格式、內容、流程需一致

## 🎓 相關文件
- [Test Framework Design](../../docs/Test_Framework_Design.md)
- [Test Strategy](../../docs/Test_Strategy.md)

## 📅 更新記錄
- 2025-11-04: 初始版本，包含 4 個回歸測試案例
