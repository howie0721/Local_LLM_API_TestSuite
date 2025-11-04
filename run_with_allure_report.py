import os
import datetime
import subprocess
import sys

def main():
    # 依據 pytest 測試目錄自動分類歸檔
    test_types = [
        ("unit", "tests/unit"),
        ("integration", "tests/integration"),
        ("error_handling", "tests/error_handling"),
        ("boundary", "tests/boundary"),
        ("compatibility", "tests/compatibility"),
        ("regression", "tests/regression"),
        ("security", "tests/security"),
        ("usability", "tests/usability"),
        ("performance", "tests/performance"),
    ]
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    allure_root = "allure-report"
    for type_name, test_path in test_types:
        if os.path.exists(test_path):
            result_dir = os.path.join(allure_root, type_name, now)
            os.makedirs(result_dir, exist_ok=True)
            # 執行 pytest 指定目錄
            code = subprocess.call([sys.executable, "-m", "pytest", test_path, f"--alluredir={result_dir}", "-v"])
            if code == 0:
                print(f"[{type_name}] 測試完成，Allure 結果已存於 {result_dir}")
            else:
                print(f"[{type_name}] 測試失敗，請檢查 pytest 輸出。Allure 結果仍存於 {result_dir}")
            # 產生 Allure HTML 報告
            html_dir = os.path.join(result_dir, "report")
            allure_path = r"C:\Users\howie\Dev\Tools\Allure\allure-2.35.1\bin\allure.bat"
            code2 = subprocess.call([allure_path, "generate", result_dir, "-o", html_dir, "--clean"])
            if code2 == 0:
                print(f"[{type_name}] Allure HTML 報告已產生於 {html_dir}")
            else:
                print(f"[{type_name}] Allure 報告產生失敗，請檢查 allure 是否安裝正確。")
    # 自動開啟 performance 報告
    perf_html_dir = os.path.join(allure_root, "performance", now, "report")
    if os.path.exists(perf_html_dir):
        import threading
        import webbrowser
        import time
        os.chdir(perf_html_dir)
        def start_server():
            import http.server, socketserver
            Handler = http.server.SimpleHTTPRequestHandler
            with socketserver.TCPServer(("", 8080), Handler) as httpd:
                print("Serving at port 8080...")
                httpd.serve_forever()
        t = threading.Thread(target=start_server, daemon=False)
        t.start()
        time.sleep(1)
        webbrowser.open("http://localhost:8080/index.html")
        try:
            while t.is_alive():
                t.join(1)
        except KeyboardInterrupt:
            print("\n伺服器已手動關閉。")
            os._exit(0)

if __name__ == "__main__":
    main()
