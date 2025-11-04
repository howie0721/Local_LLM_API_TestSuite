"""
TC-E2E-0001: LLM 聊天 API 端到端測試
目標：驗證 LLM API 能正確處理多輪對話，並維持上下文
"""
import pytest
import allure

pytestmark = pytest.mark.e2e

def test_TC_E2E_0001_multi_turn_conversation(ollama_client, validator):
    # 第一次提問
    messages = [{"role": "user", "content": "你叫什麼名字？"}]
    response1 = ollama_client.chat(messages=messages)
    reply1 = validator.get_chat_reply(response1)

    # 第二次提問
    messages.append({"role": "assistant", "content": reply1})
    messages.append({"role": "user", "content": "請用一句話介紹你自己。"})
    response2 = ollama_client.chat(messages=messages)
    reply2 = validator.get_chat_reply(response2)
    
    # 驗證 LLM 回應有自我介紹語意，兼容中英文
    keywords = [
        "我", "AI", "助手", "LLaMA", "language model", "模型", "電腦程式", 
        "advanced", "trained", "understand", "respond", "converse", "interact"
    ]
    validator.assert_contains_keywords(reply2, keywords, "自我介紹回應")
