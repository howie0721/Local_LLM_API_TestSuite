import pytest

pytestmark = pytest.mark.unit

def test_TC_UNIT_0004_generate_response_format(ollama_client, validator, schema_validator):
    """
    TC-UNIT-0004: 驗證 /api/generate 回傳 JSON 必有 response、done、done_reason，且型別正確
    """
    payload = {"prompt": "Test format", "stream": False}
    response = ollama_client.generate(**payload, timeout=45)
    validator.assert_status_code(response, 200)
    
    data = response.json()
    schema_validator.assert_generate_response_schema(data)
