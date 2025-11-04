"""
TC-COMP-0003: LLM 多語言輸入格式相容性測試
目標：驗證 LLM 對不同語言 prompt（中、英、日等）回應格式一致
"""
import allure


import json
import os
import pytest

pytestmark = pytest.mark.compatibility

@allure.title("TC-COMPATIBILITY-0003 LLM 多語言輸入格式相容性 (fixtures 驅動)")
@pytest.mark.parametrize("prompt,lang", [
    (item["prompt"], item["lang"]) for item in json.load(open(os.path.join(os.path.dirname(__file__), "..", "fixtures", "prompts_multilingual.json"), encoding="utf-8"))
])
def test_TC_COMPATIBILITY_0003_multilingual_input_schema(ollama_client, validator, schema_validator, prompt, lang):
    messages = [{"role": "user", "content": prompt}]
    response = ollama_client.chat(messages=messages, timeout=60)
    validator.assert_status_code(response, 200)
    data = response.json()
    try:
        schema_validator.assert_chat_response_schema(data)
    except AssertionError as e:
        raise AssertionError(f"{lang} - {str(e)}")
