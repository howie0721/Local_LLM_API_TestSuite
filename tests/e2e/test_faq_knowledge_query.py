"""
TC-E2E-0003: FAQ/知識查詢情境
目標：驗證 LLM 能根據前後文給出連貫答案
"""
import pytest
import allure

pytestmark = pytest.mark.e2e

def test_TC_E2E_0003_faq_knowledge_query(ollama_client, validator):
    # 第一次提問
    messages = [{"role": "user", "content": "你支援哪些功能？"}]
    response1 = ollama_client.chat(messages=messages, timeout=120)
    validator.assert_status_code(response1, 200)
    
    data1 = response1.json()
    reply1 = data1["choices"][0]["message"]["content"]
    validator.assert_contains_keywords(
        reply1,
        ["功能", "可以", "支援", "用途", "能力", "function", "functions", "support", "can", "ability"]
    )

    # 第二次提問
    messages.append({"role": "assistant", "content": reply1})
    messages.append({"role": "user", "content": "請舉一個例子。"})
    response2 = ollama_client.chat(messages=messages, timeout=120)
    validator.assert_status_code(response2, 200)
    
    data2 = response2.json()
    reply2 = data2["choices"][0]["message"]["content"]
    validator.assert_contains_keywords(
        reply2,
        ["例如", "像是", "舉例", "例如說", "for example", "such as", "let's say", "you could ask me", "here are some examples"]
    )
