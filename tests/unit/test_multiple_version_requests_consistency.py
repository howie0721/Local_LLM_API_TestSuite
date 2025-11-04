import pytest

pytestmark = pytest.mark.unit

def test_TC_UNIT_0005_multiple_version_requests_consistency(ollama_client, validator):
    """
    TC-UNIT-0005: 連續多次呼叫 /api/version，回傳型別與內容一致
    """
    versions = set()
    for _ in range(3):
        response = ollama_client.get_version(timeout=5)
        validator.assert_status_code(response, 200)
        
        data = response.json()
        assert "version" in data
        assert isinstance(data["version"], str)
        versions.add(data["version"])
    assert len(versions) == 1, f"多次回傳 version 不一致: {versions}"
