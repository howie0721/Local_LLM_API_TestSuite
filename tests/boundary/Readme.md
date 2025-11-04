# Boundary Testing - 邊界值測試

## 📋 概述

本目錄包含針對 Local LLM API 的邊界值測試案例，主要測試系統在處理極端輸入值時的穩定性與容錯能力。邊界值測試是軟體測試中的重要技術，專注於驗證系統在輸入參數的邊界條件下是否能正確運作。

## 🎯 測試設計目的

### 核心目標
1. **驗證系統容錯能力**：測試 LLM API 在接收極端或異常輸入時是否能妥善處理
2. **確保穩定性**：驗證系統不會因為邊界值輸入而崩潰或產生未預期的行為
3. **明確限制範圍**：確認系統對於輸入長度的上下限限制是否符合規格
4. **提升用戶體驗**：確保系統能對異常輸入提供適當的回應或錯誤訊息

### 測試策略
根據**邊界值分析 (Boundary Value Analysis)** 測試技術，針對以下維度進行測試：
- **最小值 (Minimum)**：空字串、零長度輸入
- **最大值 (Maximum)**：允許的最大長度上限
- **超出範圍 (Out of Range)**：超過系統限制的輸入
- **特殊情況 (Special Cases)**：高 token 數但字元數相對較少的輸入

## 📝 測試案例說明

### TC-BOUNDARY-0001: Prompt 長度=1024 (允許上限)
**檔案**: `test_prompt_length_max.py`

**測試目的**：
- 驗證系統能否正確處理達到允許上限（1024 字元）的 prompt
- 確認系統在最大合法輸入下的正常運作能力

**測試設計**：
```python
messages = [{"role": "user", "content": "a" * 1024}]
```
- 使用 1024 個 'a' 字元組成的字串作為 prompt
- 設定較長的 timeout (120秒) 以應對處理時間

**預期結果**：
- ✅ HTTP 狀態碼應為 200 (成功)
- ✅ 回應 JSON 中應包含 `choices` 欄位
- ✅ 系統應能正常處理並返回結果

---

### TC-BOUNDARY-0002: Prompt 長度=8192 (超過上限)
**檔案**: `test_prompt_length_over.py`

**測試目的**：
- 驗證系統對於超出限制（8192 字元）的 prompt 的處理機制
- 確認系統具備適當的輸入驗證與錯誤處理

**測試設計**：
```python
messages = [{"role": "user", "content": "a" * 8192}]
```
- 使用 8192 個 'a' 字元，遠超過允許的上限
- 預期系統應拒絕處理或返回錯誤

**預期結果**：
- ✅ HTTP 狀態碼應不為 200，或
- ✅ 回應 JSON 中不應包含 `choices` 欄位
- ✅ 系統應拒絕處理或返回適當的錯誤訊息
- ⚠️ 系統不應嘗試處理並返回結果

---

### TC-BOUNDARY-0003: Prompt 長度=0 (空字串)
**檔案**: `test_prompt_length_empty.py`

**測試目的**：
- 驗證系統對於最小邊界值（空字串）的處理能力
- 確認系統能妥善處理無內容的請求

**測試設計**：
```python
messages = [{"role": "user", "content": ""}]
```
- 傳送空字串作為 prompt
- 測試系統對於「無輸入」情況的反應

**預期結果**：
- ✅ HTTP 狀態碼應為 200 (成功)
- ✅ 回應 JSON 中應包含 `choices` 欄位
- ✅ 系統應能正常回應（可能返回空結果或預設回應）

---

### TC-BOUNDARY-0004: Prompt 極大 Token 數 (多空格)
**檔案**: `test_prompt_max_tokens.py`

**測試目的**：
- 驗證系統對於高 token 數輸入的處理能力
- 測試 tokenization 過程中的邊界情況

**測試設計**：
```python
prompt = " ".join(["word"] * 2048)
messages = [{"role": "user", "content": prompt}]
```
- 產生 2048 個 "word"，以空格分隔
- 字元數適中但 token 數極大的特殊情況
- 測試系統的 tokenizer 是否能正確處理

**預期結果**：
- ✅ HTTP 狀態碼應為 200, 400, 或 422
- ✅ API 不應崩潰或無回應
- ✅ 系統應返回成功處理或適當的錯誤碼（視模型限制而定）

## 🔧 執行方式

### 執行所有邊界值測試
```bash
pytest tests/boundary/ -v --alluredir=allure-results
```

### 執行單一測試案例
```bash
pytest tests/boundary/test_prompt_length_empty.py -v
pytest tests/boundary/test_prompt_length_max.py -v
pytest tests/boundary/test_prompt_length_over.py -v
pytest tests/boundary/test_prompt_max_tokens.py -v
```

### 生成 Allure 報告
```bash
allure serve allure-results
```

## 📊 測試覆蓋率

| 測試維度 | 測試案例 | 覆蓋率 |
|---------|---------|--------|
| 最小值邊界 | TC-BOUNDARY-0003 | ✅ |
| 最大值邊界 | TC-BOUNDARY-0001 | ✅ |
| 超出範圍 | TC-BOUNDARY-0002 | ✅ |
| Token 邊界 | TC-BOUNDARY-0004 | ✅ |

## 🔍 測試重點

### 1. 字元長度 vs Token 數量
- 字元長度和 token 數量不一定成正比
- 空格、標點符號會增加 token 數量
- 不同語言（中文 vs 英文）的 tokenization 結果不同

### 2. Timeout 設定
- 邊界值測試通常需要較長的處理時間
- 建議設定 120 秒以上的 timeout
- 避免因處理時間過長而誤判為失敗

### 3. 錯誤處理驗證
- 系統應對不合法輸入返回明確的錯誤訊息
- HTTP 狀態碼應符合 RESTful API 規範
- 錯誤回應應包含足夠的除錯資訊

## 🎓 相關文件

- [Test Framework Design](../../docs/Test_Framework_Design.md)
- [Test Strategy](../../docs/Test_Strategy.md)
- [Allure Report Guide](../../docs/Allure_Report_Guide.md)

## 📌 注意事項

1. **模型差異**：不同的 LLM 模型可能有不同的 token 限制
2. **性能考量**：超長輸入可能導致記憶體使用激增
3. **版本相容性**：確保測試環境與 LLM API 版本一致
4. **測試資料**：測試用的極端輸入不應影響模型的訓練或學習

## 🐛 已知問題

- 部分模型對於空字串 prompt 的處理方式不一致
- 超長 prompt 的錯誤訊息格式可能因版本而異
- Token 計算方式依賴於模型的 tokenizer 實作

## 📅 更新記錄

- 2025-11-04: 初始版本，包含 4 個邊界值測試案例