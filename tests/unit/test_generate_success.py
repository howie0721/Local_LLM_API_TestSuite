import pytest

pytestmark = pytest.mark.unit

def test_TC_UNIT_0003_generate_success(ollama_client, validator):
    """
    TC-UNIT-0003: 傳入正確 model 與 prompt，驗證 /api/generate 回傳 200 且 response 欄位為非空字串
    """
    response = ollama_client.generate(prompt="Hello, world!")
    reply = validator.get_generate_reply(response)
