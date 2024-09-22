import asyncio      # 异步IO库，用于处理并发操作
from time import monotonic  # monotonic用于精确计时

import httpx
from rich.console import Console    # Rich库的Console类，用于在控制台输出彩色文本

console = Console()

url_list = """
http://194.36.209.122:8081/v1/chat/completions
http://45.152.113.138:8443/v1/chat/completions
http://45.154.3.33:1212/v1/chat/completions
http://193.43.94.167:8123/v1/chat/completions
http://45.152.84.223:8444/v1/chat/completions
http://107.172.57.90:8444/v1/chat/completions
""".strip().splitlines()    # 去掉前后的空白字符，然后按行分割，得到一个URL列表

models = """
claude-3-5-sonnet-20240620
claude-3-opus-20240229
claude-3-sonnet-20240229
claude-3-haiku-20240307
claude-2.1
claude-2.0
claude-1.3
claude-instant-1.2
claude-instant-1.1
""".strip().splitlines()

async def main():
    client = httpx.AsyncClient()    # 创建一个异步HTTP客户端
    coros = []

    # for url in ["http://107.172.57.90:8444/v1/chat/completions"]:
    # for url in url_list[9:10]:
    for url in url_list:
        for model in models[:1]:
            coro = client.post(
                url.strip(),
                json={
                    "model": model.strip(),
                    "messages": [{"role": "user", "content": "Say this is a test!"}],
                },
                timeout=20,
                # headers={"Authorization": "Bearer any"}
            )
            coros.append(coro)
    # asyncio.gather并发执行所有的请求，并存储所有结果
    res_list = await asyncio.gather(*coros, return_exceptions=True) 
    for url, res in zip(url_list, res_list):
        if isinstance(res, httpx.ConnectTimeout):
            console.print(f"❌： {url}, 20秒超时")
        elif isinstance(res, Exception):
            console.print(f"❌： {url}, {res}")
        else:
            if b"content" in res.content:
                console.print(f"✅： {url}, {res.json()}")
            elif isinstance(res, httpx.Response):
                console.print(f"❌： {url}, {res}")
            else:
                console.print(f"𐄂： {url}, {res}")


if __name__ == "__main__":
    then = monotonic()  # 获取当前时间，并在程序结束时计算运行时间
    asyncio.run(main()) # 启动异步主函数
    console.print(f"{monotonic() - then:.2f} s", style="green") # 打印总耗时