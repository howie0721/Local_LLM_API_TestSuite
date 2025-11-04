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
    messages = [{"role": "user", "content": "請用一句話介紹你自己。"}]
    response = ollama_client.chat(messages=messages, timeout=60)
    validator.assert_status_code(response, 200)
    
    data = response.json()
    reply = data["choices"][0]["message"]["content"].strip()
    # 允許部分彈性（如只要有 LLaMA、AI、助手、模型等關鍵字即可通過）
    validator.assert_contains_keywords(reply, ["LLaMA", "AI", "助手", "模型", "language model"])
    # 如需嚴格比對，可改為 assert reply == BASELINE_REPLY
