"""
TC-E2E-0002: LLM 多語言切換端到端測試
目標：驗證 LLM API 能根據用戶指示切換語言並正確回應
"""
import pytest
import allure

pytestmark = pytest.mark.e2e

def test_TC_E2E_0002_multilingual_switch(ollama_client, validator):
    # 第一次提問：請用英文自我介紹
    messages = [{"role": "user", "content": "Please introduce yourself in English."}]
    response1 = ollama_client.chat(messages=messages, timeout=120)
    validator.assert_status_code(response1, 200)
    
    data1 = response1.json()
    reply1 = data1["choices"][0]["message"]["content"]
    validator.assert_contains_keywords(reply1, ["I am", "My name", "AI", "assistant"])

    # 第二次提問：再用中文說一次
    messages.append({"role": "assistant", "content": reply1})
    messages.append({"role": "user", "content": "再用中文說一次。"})
    response2 = ollama_client.chat(messages=messages, timeout=120)
    validator.assert_status_code(response2, 200)
    
    data2 = response2.json()
    reply2 = data2["choices"][0]["message"]["content"]
    validator.assert_contains_keywords(reply2, ["我", "AI", "助手"])
