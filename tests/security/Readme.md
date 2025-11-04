# Security Testing - 安全性測試

## 📋 概述

本目錄包含針對 Local LLM API 的安全性測試案例，重點驗證系統對敏感資訊、惡意輸入、內容過濾等安全議題的防護能力。

## 🎯 測試設計目的

### 核心目標
1. **驗證內容過濾**：測試 LLM API 是否能過濾敏感、違規、惡意內容
2. **防止 prompt injection**：驗證系統對 prompt injection 攻擊的防護能力
3. **敏感資訊保護**：確保不洩漏用戶或系統敏感資訊

### 測試策略
- **內容過濾**：測試不當內容、違規詞彙的過濾效果
- **拒絕關鍵字**：驗證模型對拒絕回應關鍵字的處理
- **prompt injection**：模擬 prompt injection 攻擊
- **敏感資訊洩漏**：測試敏感資料是否會被回傳

## 📝 測試案例說明

### TC-SECURITY-0001: 內容過濾
**檔案**: `test_content_filter.py`
- 測試不當內容過濾

### TC-SECURITY-0002: 拒絕關鍵字
**檔案**: `test_model_refusal_keywords.py`
- 驗證模型對拒絕回應關鍵字的處理

### TC-SECURITY-0003: prompt injection
**檔案**: `test_prompt_injection.py`
- 模擬 prompt injection 攻擊

### TC-SECURITY-0004: 敏感資訊洩漏
**檔案**: `test_sensitive_info_leak.py`
- 測試敏感資訊是否會被回傳

## 🔧 執行方式

```bash
pytest tests/security/ -v --alluredir=allure-results
```

## 📊 測試覆蓋率

| 測試維度 | 測試案例 | 覆蓋率 |
|---------|---------|--------|
| 內容過濾 | TC-SECURITY-0001 | ✅ |
| 拒絕關鍵字 | TC-SECURITY-0002 | ✅ |
| prompt injection | TC-SECURITY-0003 | ✅ |
| 敏感資訊洩漏 | TC-SECURITY-0004 | ✅ |

## 🔍 測試重點
- 不當內容不得回傳
- 敏感資訊不得洩漏
- prompt injection 必須防禦

## 🎓 相關文件
- [Test Framework Design](../../docs/Test_Framework_Design.md)
- [Test Strategy](../../docs/Test_Strategy.md)

## 📅 更新記錄
- 2025-11-04: 初始版本，包含 4 個安全性測試案例
