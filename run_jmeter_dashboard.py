import os
import subprocess
import glob
import datetime
import webbrowser
import time

def run_jmeter_and_generate_report(jmx_path, result_dir, report_dir, jmeter_path="jmeter"):
    os.makedirs(result_dir, exist_ok=True)
    os.makedirs(report_dir, exist_ok=True)
    # 執行 JMeter 非互動模式
    jtl_file = os.path.join(result_dir, os.path.splitext(os.path.basename(jmx_path))[0] + ".jtl")
    print(f"執行 JMeter 測試: {jmx_path}")
    code = subprocess.call([jmeter_path, "-n", "-t", jmx_path, "-l", jtl_file])
    if code != 0:
        print(f"[失敗] JMeter 測試失敗: {jmx_path}")
        return None
    print(f"[成功] 測試結果已存於 {jtl_file}")
    # 產生 HTML Dashboard 報表
    print(f"產生 HTML Dashboard 報表: {report_dir}")
    code2 = subprocess.call([jmeter_path, "-g", jtl_file, "-o", report_dir])
    if code2 == 0:
        print(f"[成功] 報表已產生於 {report_dir}")
        return report_dir
    else:
        print(f"[失敗] 報表產生失敗，請檢查 JMeter 安裝與 jtl 檔案。")
        return None

def main():
    # 支援 performance 與 stability 兩個資料夾
    test_types = [
        # ("performance", "tests/performance/*.jmx"),
        ("stability", "tests/stability/*.jmx"),
    ]
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    jmeter_path = r"C:\Users\howie\Dev\Tools\Jmeter\apache-jmeter-5.6.3\bin\jmeter.bat"  # 已指定 JMeter 安裝路徑
    base_report_root = "jmeter-dashboard-report"
    for type_name, pattern in test_types:
        jmx_files = glob.glob(pattern)
        if not jmx_files:
            print(f"[{type_name}] 找不到 JMeter 測試腳本: {pattern}")
            continue
        for jmx_path in jmx_files:
            result_dir = os.path.join(base_report_root, type_name, now, os.path.splitext(os.path.basename(jmx_path))[0])
            report_dir = os.path.join(result_dir, "report")
            html_dir = run_jmeter_and_generate_report(jmx_path, result_dir, report_dir, jmeter_path)
            if html_dir and os.path.exists(os.path.join(html_dir, "index.html")):
                print(f"自動開啟報表: {html_dir}/index.html")
                # 延遲 1 秒確保檔案寫入完成
                time.sleep(1)
                webbrowser.open(f"file://{os.path.abspath(os.path.join(html_dir, 'index.html'))}")

if __name__ == "__main__":
    main()