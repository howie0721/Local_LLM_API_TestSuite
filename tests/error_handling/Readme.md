# Error Handling Testing - 錯誤處理測試

## 📋 概述

本目錄包含針對 Local LLM API 的錯誤處理測試案例，重點驗證系統在遇到異常請求、缺參數、連線失敗等情境下，能否正確回應錯誤訊息並維持穩定。

## 🎯 測試設計目的

### 核心目標
1. **驗證 API 錯誤回應**：測試 LLM API 在遇到各種錯誤情境時，能否回傳正確的 HTTP 狀態碼與錯誤訊息
2. **確保系統穩定性**：異常情境下不應導致系統崩潰或未預期行為
3. **提升用戶體驗**：提供明確、易於理解的錯誤回應

### 測試策略
- **API 路徑錯誤**：請求不存在的 API 路徑
- **缺少必要參數**：省略必填欄位
- **HTTP 方法錯誤**：使用不支援的 HTTP 方法
- **連線失敗**：模擬無法連線情境

## 📝 測試案例說明

### TC-ERROR-0001: API 路徑不存在
**檔案**: `test_api_notfound.py`
- 測試不存在的 API 路徑，預期回傳 404 Not Found

### TC-ERROR-0002: 缺少必要參數
**檔案**: `test_missing_required_param.py`
- 測試省略必填欄位，預期回傳 400 Bad Request

### TC-ERROR-0003: HTTP 方法錯誤
**檔案**: `test_method_not_allowed.py`
- 測試使用不支援的 HTTP 方法，預期回傳 405 Method Not Allowed

### TC-ERROR-0004: 連線失敗
**檔案**: `test_cannot_connect.py`
- 模擬無法連線情境，預期回傳連線錯誤

## 🔧 執行方式

```bash
pytest tests/error_handling/ -v --alluredir=allure-results
```

## 📊 測試覆蓋率

| 測試維度 | 測試案例 | 覆蓋率 |
|---------|---------|--------|
| 路徑錯誤 | TC-ERROR-0001 | ✅ |
| 缺參數 | TC-ERROR-0002 | ✅ |
| 方法錯誤 | TC-ERROR-0003 | ✅ |
| 連線失敗 | TC-ERROR-0004 | ✅ |

## 🔍 測試重點
- 錯誤回應格式需明確
- HTTP 狀態碼需正確
- 不應洩漏敏感資訊

## 🎓 相關文件
- [Test Framework Design](../../docs/Test_Framework_Design.md)
- [Test Strategy](../../docs/Test_Strategy.md)

## 📅 更新記錄
- 2025-11-04: 初始版本，包含 4 個錯誤處理測試案例
