import pytest

pytestmark = pytest.mark.unit

def test_TC_UNIT_0002_version_response_format(ollama_client, validator):
    """
    TC-UNIT-0002: 驗證 /api/version 回傳 JSON 結構與型別
    """
    response = ollama_client.get_version(timeout=5)
    validator.assert_status_code(response, 200)
    
    data = response.json()
    assert "version" in data, "缺少 version 欄位"
    assert isinstance(data["version"], str), f"version 欄位型別錯誤: {type(data['version'])}"
