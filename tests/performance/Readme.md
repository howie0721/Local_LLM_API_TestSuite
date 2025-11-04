# Performance Testing - 效能測試

## 📋 概述

本目錄包含針對 Local LLM API 的效能測試案例，重點驗證系統在高併發、大量請求、長輸入等情境下的反應速度、穩定性與資源使用狀況。

## 🎯 測試設計目的

### 核心目標
1. **驗證高併發處理能力**：測試多用戶同時請求下的效能
2. **長輸入處理能力**：驗證系統對超長 prompt 的效能表現
3. **壓力測試**：模擬極端負載，觀察系統極限

### 測試策略
- **單一請求效能**：單一請求的反應速度
- **長 prompt 測試**：超長輸入下的效能
- **併發測試**：多用戶同時請求的效能
- **壓力測試**：極端負載下的穩定性

## 📝 測試案例說明

### TC-PERF-0001: 單一請求效能
**檔案**: `ollama_llama3_single_request.jmx`
- 測試單一請求的反應速度

### TC-PERF-0002: 長 prompt 效能
**檔案**: `ollama_llama3_long_prompt.jmx`
- 測試超長 prompt 下的效能

### TC-PERF-0003: 併發請求效能
**檔案**: `ollama_llama3_concurrent_requests.jmx`
- 測試多用戶同時請求的效能

### TC-PERF-0004: 壓力測試
**檔案**: `ollama_llama3_stress_test.jmx`
- 模擬極端負載下的系統表現

## 🔧 執行方式

```bash
# 需安裝 Apache JMeter
jmeter -n -t tests/performance/ollama_llama3_single_request.jmx
jmeter -n -t tests/performance/ollama_llama3_long_prompt.jmx
jmeter -n -t tests/performance/ollama_llama3_concurrent_requests.jmx
jmeter -n -t tests/performance/ollama_llama3_stress_test.jmx
```

## 📊 測試覆蓋率

| 測試維度 | 測試案例 | 覆蓋率 |
|---------|---------|--------|
| 單一請求 | TC-PERF-0001 | ✅ |
| 長 prompt | TC-PERF-0002 | ✅ |
| 併發請求 | TC-PERF-0003 | ✅ |
| 壓力測試 | TC-PERF-0004 | ✅ |

## 🔍 測試重點
- 反應速度、資源使用、穩定性
- 高併發與極端負載下的表現

## 🎓 相關文件
- [Test Framework Design](../../docs/Test_Framework_Design.md)
- [Test Strategy](../../docs/Test_Strategy.md)

## 📅 更新記錄
- 2025-11-04: 初始版本，包含 4 個效能測試案例
