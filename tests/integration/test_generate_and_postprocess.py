import pytest

pytestmark = pytest.mark.integration

def test_TC_INTEGRATION_0001_generate_and_postprocess(ollama_client, validator):
    """
    TC-INTEGRATION-0001: 產生 Ollama 回應後進行簡單後處理，驗證整合流程
    """
    response = ollama_client.generate(prompt="請用一句話介紹台灣。", timeout=30)
    reply = validator.get_generate_reply(response)
    
    # 將回應文字去除前後空白並轉成大寫（模擬下游後處理）
    processed = reply.strip().upper()
    
    # 驗證後處理結果不是空字串
    validator.assert_non_empty_string(processed, "後處理結果")
    
    # 驗證結果中有「台灣」或「TAIWAN」關鍵字
    assert "台灣" in processed or "TAIWAN" in processed, f"後處理結果: {processed}"
