# Stability Testing - 穩定性測試

## 📋 概述

本目錄包含針對 Local LLM API 的穩定性測試案例，重點驗證系統在長時間運作、大量上下文、記憶體壓力等情境下的穩定性與資源管理能力。

## 🎯 測試設計目的

### 核心目標
1. **驗證長時間運作穩定性**：測試系統長時間運作下的穩定性
2. **大量上下文處理能力**：驗證系統對超長上下文的處理能力
3. **記憶體管理與回收**：觀察記憶體使用與潛在洩漏
4. **異常恢復能力**：測試系統異常重啟後的恢復能力

### 測試策略
- **長上下文測試**：模擬大量上下文輸入
- **長時間壓力測試**：長時間高負載運作
- **記憶體洩漏檢查**：觀察記憶體使用情形
- **重啟恢復測試**：模擬異常重啟後的恢復

## 📝 測試案例說明

### TC-STABILITY-0001: 長上下文穩定性
**檔案**: `ollama_llama3_long_context_stability.jmx`
- 測試大量上下文下的穩定性

### TC-STABILITY-0002: 長時間壓力測試
**檔案**: `ollama_llama3_long_duration_stress.jmx`
- 測試長時間高負載下的穩定性

### TC-STABILITY-0003: 記憶體洩漏檢查
**檔案**: `ollama_llama3_memory_leak_simple.jmx`
- 觀察記憶體使用與洩漏情形

### TC-STABILITY-0004: 重啟恢復測試
**檔案**: `ollama_llama3_restart_recovery.jmx`
- 測試異常重啟後的恢復能力

## 🔧 執行方式

```bash
# 需安裝 Apache JMeter
jmeter -n -t tests/stability/ollama_llama3_long_context_stability.jmx
jmeter -n -t tests/stability/ollama_llama3_long_duration_stress.jmx
jmeter -n -t tests/stability/ollama_llama3_memory_leak_simple.jmx
jmeter -n -t tests/stability/ollama_llama3_restart_recovery.jmx
```

## 📊 測試覆蓋率

| 測試維度 | 測試案例 | 覆蓋率 |
|---------|---------|--------|
| 長上下文 | TC-STABILITY-0001 | ✅ |
| 長時間壓力 | TC-STABILITY-0002 | ✅ |
| 記憶體洩漏 | TC-STABILITY-0003 | ✅ |
| 重啟恢復 | TC-STABILITY-0004 | ✅ |

## 🔍 測試重點
- 長時間、長上下文下的穩定性
- 記憶體管理與回收
- 異常恢復能力

## 🎓 相關文件
- [Test Framework Design](../../docs/Test_Framework_Design.md)
- [Test Strategy](../../docs/Test_Strategy.md)

## 📅 更新記錄
- 2025-11-04: 初始版本，包含 4 個穩定性測試案例
