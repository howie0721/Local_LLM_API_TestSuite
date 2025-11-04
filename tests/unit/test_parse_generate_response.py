import pytest

pytestmark = pytest.mark.unit

def test_TC_UNIT_0006_parse_generate_response(ollama_client, validator):
    """
    TC-UNIT-0006: 驗證 /api/generate 回傳資料的 response 欄位型別與內容
    """
    payload = {"prompt": "Parse this!", "stream": False}
    response = ollama_client.generate(**payload, timeout=45)
    validator.assert_status_code(response, 200)
    
    data = response.json()
    assert "response" in data
    assert isinstance(data["response"], str)
    assert data["response"].strip() != ""
