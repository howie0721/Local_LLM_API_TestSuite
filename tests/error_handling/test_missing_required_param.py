import pytest
import requests

pytestmark = pytest.mark.error_handling

def test_TC_ERROR_0004_missing_required_param():
    """
    TC-ERROR-0004: 呼叫 /api/generate 時缺少必要參數，應回傳 400 或對應錯誤
    """
    url = "http://localhost:11434/api/generate"
    # 故意缺少 'model' 或 'prompt' 參數
    payload = {"model": "llama3"}  # 缺少 prompt
    response = requests.post(url, json=payload, timeout=5)
    assert response.status_code in (400, 422), f"實際回傳: {response.status_code}, 內容: {response.text}"
