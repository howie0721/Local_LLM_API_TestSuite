
import pytest

pytestmark = pytest.mark.unit

def test_TC_UNIT_0001_connection(ollama_client, validator):
	"""
	TC-UNIT-0001: 測試本地 Ollama API 是否可連線並正確回應版本資訊
	"""
	try:
		response = ollama_client.version()
	except Exception as e:
		pytest.fail(f"無法連線到 Ollama API: {e}")
	
	validator.assert_status_code(response, 200)
	data = response.json()
	validator.assert_json_field(data, "version")
