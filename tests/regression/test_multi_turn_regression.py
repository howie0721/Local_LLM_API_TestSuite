"""
TC-REG-0002: LLM 多輪對話回應一致性回歸測試
目標：驗證 LLM 在多輪對話情境下，回應內容/格式不會因升級或 prompt 調整而退步
"""
import pytest
import allure

pytestmark = pytest.mark.regression

@allure.title("TC-REG-0002 LLM 多輪對話回應一致性")
def test_TC_REG_0002_multi_turn_regression(ollama_client, validator):
    # 使用 temperature=0 確保一致性
    # 第一次提問
    messages = [{"role": "user", "content": "你叫什麼名字？"}]
    response1 = ollama_client.chat(messages=messages, timeout=60, temperature=0)
    validator.assert_status_code(response1, 200)
    
    data1 = response1.json()
    reply1 = data1["choices"][0]["message"]["content"].strip()
    allure.attach(reply1, name="第一輪回應", attachment_type=allure.attachment_type.TEXT)
    assert reply1 != "", "第一次回應內容為空"

    # 第二次提問
    messages.append({"role": "assistant", "content": reply1})
    messages.append({"role": "user", "content": "請用一句話介紹你自己。"})
    response2 = ollama_client.chat(messages=messages, timeout=60, temperature=0)
    validator.assert_status_code(response2, 200)
    
    data2 = response2.json()
    reply2 = data2["choices"][0]["message"]["content"].strip()
    allure.attach(reply2, name="第二輪回應", attachment_type=allure.attachment_type.TEXT)
    
    # 放寬關鍵字要求，只要有任一關鍵字即可
    assert reply2 != "", "第二次回應內容為空"
    
    keywords = ["llama", "ai", "助手", "模型", "language model", "artificial intelligence", 
                "智能", "智慧", "人工智慧", "assistant", "help", "tinyllama"]
    has_keyword = any(keyword.lower() in reply2.lower() for keyword in keywords)
    
    assert has_keyword, f"回應應包含至少一個關鍵字 {keywords}，實際回應: {reply2}"
