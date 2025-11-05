"""
共用測試工具類別（由 conftest.py 提供 fixture）
"""
import requests
from typing import Dict, Any

class ResponseValidator:
    """API 回應驗證工具"""
    @staticmethod
    def assert_status_code(response: requests.Response, expected: int = 200):
        assert response.status_code == expected, \
            f"預期狀態碼 {expected}，實際為 {response.status_code}，回應內容: {response.text}"
    @staticmethod
    def assert_json_field(data: Dict[str, Any], field: str, field_type: type = None):
        assert field in data, f"回應缺少 {field} 欄位，實際內容: {data}"
        if field_type:
            assert isinstance(data[field], field_type), \
                f"{field} 欄位型別錯誤，預期 {field_type}，實際為 {type(data[field])}"
    @staticmethod
    def assert_non_empty_string(value: str, field_name: str = "回應"):
        assert isinstance(value, str), f"{field_name} 應為字串型別"
        assert value.strip() != "", f"{field_name} 不應為空字串"
    @staticmethod
    def assert_contains_keywords(text: str, keywords: list, field_name: str = "回應"):
        assert any(word in text for word in keywords), \
            f"{field_name} 未包含預期關鍵字 {keywords}，實際內容: {text}"
    @staticmethod
    def get_chat_reply(response: requests.Response) -> str:
        ResponseValidator.assert_status_code(response, 200)
        data = response.json()
        ResponseValidator.assert_json_field(data, "choices", list)
        assert len(data["choices"]) > 0, "choices 列表為空"
        reply = data["choices"][0]["message"]["content"]
        ResponseValidator.assert_non_empty_string(reply, "回覆內容")
        return reply
    @staticmethod
    def get_generate_reply(response: requests.Response) -> str:
        ResponseValidator.assert_status_code(response, 200)
        data = response.json()
        ResponseValidator.assert_json_field(data, "response", str)
        reply = data["response"]
        ResponseValidator.assert_non_empty_string(reply, "回覆內容")
        return reply

class TestHelper:
    """測試輔助工具"""
    @staticmethod
    def extract_json_from_codeblock(text: str) -> dict:
        import re, json
        try:
            return json.loads(text)
        except Exception:
            pass
        match = re.search(r"```json\s*(.*?)```", text, re.DOTALL)
        if not match:
            match = re.search(r"```\s*(.*?)```", text, re.DOTALL)
        if not match:
            raise ValueError("回應未包含可解析的 JSON 區塊")
        code = match.group(1).strip()
        return json.loads(code)
    @staticmethod
    def extract_json_from_response(text: str) -> dict:
        """
        與既有測試相容的別名方法：嘗試直接解析文字為 JSON，失敗則從 code block 提取。
        """
        import json
        try:
            return json.loads(text)
        except Exception:
            return TestHelper.extract_json_from_codeblock(text)
    @staticmethod
    def extract_code_from_codeblock(text: str, language: str = None) -> str:
        import re
        if language:
            pattern = f"```{language}\\s*(.*?)```"
        else:
            pattern = r"```(?:\w+)?\s*(.*?)```"
        match = re.search(pattern, text, re.DOTALL)
        if not match:
            raise ValueError(f"回應未包含 {language or '任何'} code block")
        return match.group(1).strip()
    @staticmethod
    def assert_markdown_table(text: str):
        assert "|" in text and "---" in text, "回應未包含 markdown 表格格式"
    @staticmethod
    def assert_markdown_codeblock(text: str):
        assert "```" in text, "回應未包含 markdown code block"
    @staticmethod
    def assert_has_paragraphs(text: str, min_paragraphs: int = 2):
        paragraph_count = text.count("\n\n")
        assert paragraph_count >= min_paragraphs, \
            f"回應段落數不足，預期至少 {min_paragraphs}，實際為 {paragraph_count}"
    @staticmethod
    def assert_has_bullet_points(text: str, min_items: int = 3):
        bullet_count = sum(text.count(bullet) for bullet in ["- ", "* ", "1.", "2.", "3."])
        assert bullet_count >= min_items, \
            f"回應條列項目不足，預期至少 {min_items}，實際為 {bullet_count}"

class SchemaValidator:
    """API Schema 驗證工具"""
    @staticmethod
    def assert_chat_response_schema(data: dict):
        assert "choices" in data, "回應缺少 choices 欄位"
        assert isinstance(data["choices"], list) and len(data["choices"]) > 0, \
            "choices 應為非空 list"
        choice = data["choices"][0]
        assert "message" in choice, "choices[0] 缺少 message 欄位"
        assert "content" in choice["message"], "message 缺少 content 欄位"
        assert isinstance(choice["message"]["content"], str), "content 應為字串"
        assert "role" in choice["message"], "message 缺少 role 欄位"
        assert choice["message"]["role"] in ["assistant", "user", "system"], \
            f"role 不符標準: {choice['message']['role']}"
    @staticmethod
    def assert_generate_response_schema(data: dict):
        required_fields = {
            "response": str,
            "done": bool,
            "done_reason": str
        }
        for field, field_type in required_fields.items():
            assert field in data, f"回應缺少 {field} 欄位"
            assert isinstance(data[field], field_type), \
                f"{field} 欄位型別錯誤，預期 {field_type}，實際為 {type(data[field])}"
    @staticmethod
    def assert_error_response_schema(data: dict):
        assert any(key in data for key in ["error", "message", "code"]), \
            "錯誤回應缺少標準欄位（error/message/code）"
        found = False
        for key in ["error", "message"]:
            val = data.get(key, None)
            if isinstance(val, (str, dict, list)):
                found = True
        assert found, "錯誤訊息內容應為字串或可序列化型別"

class BatchTestHelper:
    """批次測試輔助工具

    同時支援：
    - 以 fixture 注入的 self.ollama_client 寫法（相容既有測試 batch_helper.ollama_client.chat(...)、execute_batch(...)）。
    - 傳入 client 的靜態方法寫法（run_multiple_times / run_with_multiple_prompts）。
    """
    def __init__(self, ollama_client=None):
        self.ollama_client = ollama_client

    def _require_client(self):
        if self.ollama_client is None:
            raise RuntimeError("BatchTestHelper 尚未注入 ollama_client，請於 fixture 傳入或改用靜態方法並傳 client 參數。")

    def execute_batch(self, messages: list, count: int = 3, timeout: int = 60, model: str = None, **kwargs) -> list:
        """相容既有測試的批量執行方法。

        備註：允許傳入額外參數（例如 temperature、max_tokens），將透傳給 chat API，
        以支援在 CI 中設定 temperature=0 等提高穩定性的需求。
        """
        self._require_client()
        results = []
        for _ in range(count):
            response = self.ollama_client.chat(
                messages=messages,
                timeout=timeout,
                model=model,
                **kwargs,
            )
            results.append(response)
        return results

    @staticmethod
    def run_multiple_times(client, method: str, count: int = 3, **kwargs) -> list:
        results = []
        for _ in range(count):
            if method == "chat":
                response = client.chat(**kwargs)
            elif method == "generate":
                response = client.generate(**kwargs)
            else:
                raise ValueError(f"不支援的方法: {method}")
            results.append(response)
        return results

    @staticmethod
    def run_with_multiple_prompts(client, prompts: list, **kwargs) -> list:
        results = []
        for item in prompts:
            if isinstance(item, tuple):
                prompt, label = item
            else:
                prompt, label = item, None
            if "messages" in kwargs:
                messages = [{"role": "user", "content": prompt}]
                response = client.chat(messages=messages, **kwargs)
            else:
                response = client.generate(prompt=prompt, **kwargs)
            results.append((response, label))
        return results
