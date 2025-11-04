"""
TC-INT-0003: LLM 多模型一致性整合測試
目標：驗證同一 prompt 在不同模型下回應格式與語意一致
"""
import pytest
import allure

pytestmark = pytest.mark.integration

@allure.title("TC-INT-0003 LLM 多模型一致性整合測試")
def test_TC_INT_0003_multi_model_consistency(batch_helper, validator):
    prompt = "請用一句話介紹你自己。"
    models = ["llama3", "llama2"]  # 可依實際部署模型調整
    keywords = ["LLaMA", "AI", "助手", "模型", "language model"]
    
    for model in models:
        messages = [{"role": "user", "content": prompt}]
        response = batch_helper.ollama_client.chat(messages=messages, model=model, timeout=60)
        validator.assert_status_code(response, 200)
        
        data = response.json()
        reply = data["choices"][0]["message"]["content"].strip()
        assert reply != "", f"{model} 回應內容為空"
        
        # 驗證回應語意一致
        validator.assert_contains_keywords(reply, keywords)
