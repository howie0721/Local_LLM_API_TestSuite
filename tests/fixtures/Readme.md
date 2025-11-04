# Fixtures - 測試資料管理

## 📋 概述

本目錄用於集中管理所有自動化測試所需的測試資料（fixtures），如多語言 prompt、特殊字元範例、回應範本等。透過 fixtures，可實現資料驅動測試，提升測試覆蓋率與維護彈性。

## 🎯 設計目的

1. **集中管理**：將所有測試用資料集中於 fixtures 目錄，方便團隊協作與維護
2. **資料驅動**：支援 pytest 參數化，讓同一測試可針對多組資料自動執行
3. **易於擴充**：新增測試資料只需編輯 JSON 檔，無需修改測試程式
4. **測試邏輯與資料分離**：提升測試可讀性與可維護性

## 📝 目前資料說明

### prompts_multilingual.json
- 多語言 prompt 測試資料，支援中、英、日、韓、法、德、西、俄、泰、阿拉伯等
- 供 compatibility/test_multilingual_input_schema.py 參數化測試使用

### prompts_specialchar.json
- 特殊字元（emoji、符號、換行、超長字串等）測試資料
- 供 compatibility/test_special_char_schema.py 參數化測試使用

## 🔧 使用方式

1. 在測試程式中讀取 fixtures 目錄下的 JSON 檔
2. 搭配 pytest.mark.parametrize 實現資料驅動測試
3. 新增或修改測試資料時，僅需編輯對應 JSON 檔案

## 📦 範例結構

```
fixtures/
	prompts_multilingual.json
	prompts_specialchar.json
	...
```

## 📌 注意事項

1. 測試資料請以 UTF-8 編碼儲存，避免亂碼
2. 建議以 JSON 格式管理，方便程式自動讀取
3. 若有大量資料，可依主題拆分多個檔案

## 🎓 相關文件

- [Test Framework Design](../../docs/Test_Framework_Design.md)
- [Test Strategy](../../docs/Test_Strategy.md)

## 📅 更新記錄

- 2025-11-04: 初始版本，說明 fixtures 目錄設計與用法
