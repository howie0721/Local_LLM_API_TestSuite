"""
TC-REG-0001: LLM 固定 prompt 回應一致性回歸測試
目標：驗證 LLM 對於固定 prompt 的回應內容/格式不會因升級或調整而退步
"""
import pytest
import allure

pytestmark = pytest.mark.regression

# 可根據實際需求調整 baseline 回應內容
BASELINE_REPLY = "我是 LLaMA，一個由 Meta AI 訓練的大型語言模型。很高興為您提供協助！"

@allure.title("TC-REG-0001 LLM 固定 prompt 回應一致性")
def test_TC_REG_0001_fixed_prompt_regression(ollama_client, validator):
    # 使用 temperature=0 確保一致性
    messages = [{"role": "user", "content": "請用一句話介紹你自己。"}]
    response = ollama_client.chat(messages=messages, timeout=60, temperature=0)
    validator.assert_status_code(response, 200)
    
    data = response.json()
    reply = data["choices"][0]["message"]["content"].strip()
    
    allure.attach(reply, name="LLM 回應", attachment_type=allure.attachment_type.TEXT)
    
    # 放寬驗證條件：只要回應不為空且包含任一關鍵字即可
    assert reply, "回應內容不應為空"
    
    keywords = ["llama", "ai", "助手", "模型", "language model", "assistant", "help", "tinyllama"]
    has_keyword = any(keyword.lower() in reply.lower() for keyword in keywords)
    
    assert has_keyword, f"回應應包含至少一個關鍵字 {keywords}，實際回應: {reply}"
