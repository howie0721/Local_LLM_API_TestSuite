"""
TC-INT-0004: LLM 多語言回應一致性整合測試
目標：驗證同一語意 prompt 用不同語言詢問，回應格式與語意一致
"""
import pytest
import allure

pytestmark = pytest.mark.integration

@allure.title("TC-INT-0004 LLM 多語言回應一致性整合測試")
def test_TC_INT_0004_multi_language_consistency(ollama_client, validator):
    prompts = [
        ("請用一句話介紹你自己。", "zh"),
        ("Please introduce yourself in one sentence.", "en"),
        ("请用一句话介绍你自己。", "zh-simplified")
    ]
    keywords = ["LLaMA", "AI", "助手", "模型", "language model"]
    
    for prompt, lang in prompts:
        messages = [{"role": "user", "content": prompt}]
        response = ollama_client.chat(messages=messages, timeout=60)
        validator.assert_status_code(response, 200)
        
        data = response.json()
        reply = data["choices"][0]["message"]["content"].strip()
        assert reply != "", f"{lang} 回應內容為空"
        
        # 驗證回應語意一致
        validator.assert_contains_keywords(reply, keywords)
