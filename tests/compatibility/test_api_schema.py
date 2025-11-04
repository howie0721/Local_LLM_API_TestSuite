"""
TC-COMP-0001: LLM API Schema 相容性測試
目標：驗證 LLM 回傳 JSON 結構是否符合 OpenAI/官方 API 標準
"""
import pytest
import allure

pytestmark = pytest.mark.compatibility

@allure.title("TC-COMPATIBILITY-0001 LLM API Schema 相容性 (標準欄位)")
def test_TC_COMPATIBILITY_0001_api_schema_compatibility(ollama_client, schema_validator):
    messages = [{"role": "user", "content": "請用一句話自我介紹"}]
    response = ollama_client.chat(messages=messages, timeout=60)
    data = response.json()
    schema_validator.assert_chat_response_schema(data)
