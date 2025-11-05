"""
TC-INT-0002: LLM 多階段生成與後處理整合測試
目標：驗證 LLM 先產生內容，再進行後處理（如翻譯/摘要），流程串接正確
"""
import pytest
import allure

pytestmark = pytest.mark.integration

@allure.title("TC-INT-0002 LLM 多階段生成與後處理整合測試")
def test_TC_INT_0002_multi_stage_generate_postprocess(ollama_client, validator):
    # 第一步：請 LLM 產生一段英文自我介紹
    messages1 = [{"role": "user", "content": "Please introduce yourself in 2-3 sentences in English."}]
    response1 = ollama_client.chat(messages=messages1, timeout=60, temperature=0)
    validator.assert_status_code(response1, 200)
    
    data1 = response1.json()
    intro_en = data1["choices"][0]["message"]["content"].strip()
    allure.attach(intro_en, name="英文自我介紹", attachment_type=allure.attachment_type.TEXT)
    assert intro_en != "", "第一次回應內容為空"

    # 第二步：將英文自我介紹翻譯成中文
    messages2 = [{"role": "user", "content": f"請將下列英文翻譯成中文，只輸出翻譯結果：\n{intro_en}"}]
    response2 = ollama_client.chat(messages=messages2, timeout=60, temperature=0)
    validator.assert_status_code(response2, 200)
    
    data2 = response2.json()
    intro_zh = data2["choices"][0]["message"]["content"].strip()
    allure.attach(intro_zh, name="中文翻譯", attachment_type=allure.attachment_type.TEXT)
    
    # 驗證翻譯結果有相關關鍵字，放寬條件
    keywords = ["我", "AI", "助手", "模型", "語言", "model", "assistant", "是", "我們"]
    has_keyword = any(kw in intro_zh for kw in keywords)
    assert has_keyword, f"翻譯結果應包含相關關鍵字，實際: {intro_zh}"
