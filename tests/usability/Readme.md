# Usability Testing - 易用性測試

## 📋 概述

本目錄包含針對 Local LLM API 的易用性測試案例，重點驗證系統回應格式、段落、表格、程式碼區塊等輸出是否符合用戶易讀性與實用性需求。

## 🎯 測試設計目的

### 核心目標
1. **驗證回應格式易讀性**：測試回應內容是否易於閱讀與理解
2. **多樣輸出格式**：段落、表格、程式碼區塊等格式正確性
3. **提升用戶體驗**：確保回應內容實用且美觀

### 測試策略
- **程式碼區塊**：驗證回應中程式碼區塊格式
- **段落格式**：多段落回應的格式正確性
- **表格格式**：表格輸出的正確性
- **回應格式**：整體回應格式的易讀性

## 📝 測試案例說明

### TC-USABILITY-0001: 程式碼區塊格式
**檔案**: `test_response_codeblock.py`
- 驗證回應中程式碼區塊格式

### TC-USABILITY-0002: 回應格式
**檔案**: `test_response_format.py`
- 驗證整體回應格式易讀性

### TC-USABILITY-0003: 段落格式
**檔案**: `test_response_paragraphs.py`
- 驗證多段落回應格式

### TC-USABILITY-0004: 表格格式
**檔案**: `test_response_table.py`
- 驗證表格輸出格式

## 🔧 執行方式

```bash
pytest tests/usability/ -v --alluredir=allure-results
```

## 📊 測試覆蓋率

| 測試維度 | 測試案例 | 覆蓋率 |
|---------|---------|--------|
| 程式碼區塊 | TC-USABILITY-0001 | ✅ |
| 回應格式 | TC-USABILITY-0002 | ✅ |
| 段落格式 | TC-USABILITY-0003 | ✅ |
| 表格格式 | TC-USABILITY-0004 | ✅ |

## 🔍 測試重點
- 回應內容需易讀、格式正確
- 多樣輸出格式需驗證

## 🎓 相關文件
- [Test Framework Design](../../docs/Test_Framework_Design.md)
- [Test Strategy](../../docs/Test_Strategy.md)

## 📅 更新記錄
- 2025-11-04: 初始版本，包含 4 個易用性測試案例
