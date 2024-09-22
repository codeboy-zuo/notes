"""
功能： 测试deeplx API 接口的可用性
"""
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm  # 导入 tqdm 库

# DeepLX接口列表
deepl_urls = [
    "http://82.157.137.187:1188/translate",
"https://api.deeplx.org/translate",
"https://deeplx.vercel.app/translate",
"https://deeplxpro.vercel.app/translate",
"https://deeplx.llleman.com/translate",
"https://translates.me/v2/translate",
"https://deeplx.papercar.top/translate",
"https://dlx.bitjss.com/translate",
"https://deeplx.ychinfo.com/translate",
"https://free-deepl.speedcow.top/translate",
"https://deeplx.keyrotate.com/translate",
"https://deepx.dumpit.top/translate",
"https://deepl.wuyongx.uk/translate",
"https://ghhosa.zzaning.com/translate",
"https://deeplx.he-sb.top/translate",
"https://deepl.aimoyu.tech/translate",
"https://deepl.tr1ck.cn/translate",
"https://translate.dftianyi.com/translate",
"https://deeplx.2077000.xyz:2087/translate"
]

# 测试请求参数
test_data = {
    "text": "Hello, world!",
    "source_lang": "EN",
    "target_lang": "ZH"
}

# 用来收集可用接口及其响应时间
available_endpoints = []

# 定义请求函数
def check_endpoint(url):
    try:
        start_time = time.time()
        response = requests.post(url, json=test_data, timeout=5)
        latency = time.time() - start_time  # 计算请求延迟
        # 确保服务真正可用
        if response.status_code == 200 and ('data' in response.json() and len(str(response.json().get("data"))) > 0):
            return (url, latency)
    except requests.exceptions.RequestException:
        return None  # 返回 None 表示请求失败

# 使用多线程检查每个接口的可用性和延迟
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(check_endpoint, url): url for url in deepl_urls}
    
    # 使用 tqdm 显示进度条
    for future in tqdm(as_completed(futures), total=len(futures), desc="Checking endpoints"):
        result = future.result()
        if result:
            available_endpoints.append(result)

# 根据延迟时间排序接口
available_endpoints.sort(key=lambda x: x[1])

# 打印界面美化
print("\nAvailable DeepLX Endpoints with Latencies:")
print("-" * 60)
for endpoint, delay in available_endpoints:
    print(f"🚀 ({delay:.2f}s) {endpoint}")
print("-" * 60)

# 打印所有可用的接口，按延迟排序，格式为"DeepLX👌：(count)"
if available_endpoints:
    formatted_endpoints = ",".join([endpoint[0] for endpoint in available_endpoints])
    print(f"\nDeepLX👌: ({len(available_endpoints)}) {formatted_endpoints}\n")
else:
    print("No available endpoints found.\n")