"""
TC-REGRESSION-0003: LLM 回應格式穩定性回歸測試
目標：驗證同一 prompt 多次呼叫，回應格式（如 JSON 結構、欄位順序）是否穩定
"""
"""
TC-REG-0003: LLM 回應格式穩定性回歸測試
目標：驗證 LLM 回應 JSON 格式是否穩定（關鍵欄位不應變動或遺失）
"""
import pytest
import allure

pytestmark = pytest.mark.regression

@allure.title("TC-REGRESSION-0003 LLM 回應格式穩定性回歸")
def test_TC_REGRESSION_0003_output_format_regression(batch_helper, test_helper):
    prompt = "請用 JSON 格式產生一個用戶資料範例，欄位包含 name, age, email。"
    messages = [{"role": "user", "content": prompt}]
    
    # 執行 3 次並收集結果
    results = []
    responses = batch_helper.execute_batch(messages, count=3, timeout=120)
    
    for response in responses:
        data = response.json()
        reply = data["choices"][0]["message"]["content"]
        user_json = test_helper.extract_json_from_response(reply)
        results.append(user_json)
    
    # 驗證三次回傳的欄位順序與結構一致
    keys_list = [list(r.keys()) for r in results]
    assert all(keys == keys_list[0] for keys in keys_list), f"多次回傳欄位順序不一致: {keys_list}"
