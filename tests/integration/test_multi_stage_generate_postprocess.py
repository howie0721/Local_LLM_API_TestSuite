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
    messages1 = [{"role": "user", "content": "Please introduce yourself in English."}]
    response1 = ollama_client.chat(messages=messages1, timeout=60)
    validator.assert_status_code(response1, 200)
    
    data1 = response1.json()
    intro_en = data1["choices"][0]["message"]["content"].strip()
    assert intro_en != "", "第一次回應內容為空"

    # 第二步：將英文自我介紹翻譯成中文
    messages2 = [{"role": "user", "content": f"請將下列英文翻譯成中文：{intro_en}"}]
    response2 = ollama_client.chat(messages=messages2, timeout=60)
    validator.assert_status_code(response2, 200)
    
    data2 = response2.json()
    intro_zh = data2["choices"][0]["message"]["content"].strip()
    # 驗證翻譯結果有「我是」或「AI」等關鍵字
    validator.assert_contains_keywords(intro_zh, ["我是", "AI", "助手", "模型"])
