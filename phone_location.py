# -*- coding: utf-8 -*-
"""
实验 1-2：手机归属地查询（代码重构可复用版）
教材《数据采集与预处理》第 3 章 3.5 案例 2

使用 requests 发送带参数的 GET 请求，把响应的 HTML 源代码原样保存到本地 html。
"""
import re
from pathlib import Path

import requests

# ==================== ① 定义请求信息 ====================
# 教材原接口 www.bspider.top/ip138 已失效，改用 ip138 官方查询页，参数形式一致。
BASE_URL = "https://www.ip138.com/mobile.asp"
MY_PHONE = "19725167601"          # ←★ 改成你自己的手机号
PARAMS = {"mobile": MY_PHONE, "action": "mobile"}
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}
TIMEOUT = 10

OUT_FILE = Path(__file__).parent / "phone_location.html"


# ==================== ② 发送请求并获得响应 ====================
def get_html(url, params, headers=HEADERS, timeout=TIMEOUT):
    """发送请求，返回响应的 HTML 源代码；失败返回 None"""
    try:
        r = requests.get(url, params=params, headers=headers, timeout=timeout)
        r.raise_for_status()
        r.encoding = r.apparent_encoding   # 按页面真实编码解码，避免中文乱码
        return r.text                     # HTML 是文本，用 text 而非 content
    except Exception as err:
        print("请求失败:", err)
        return None


# ==================== ③ 将响应存储到本地 html ====================
def save_html(path, html):
    """把响应源代码写入本地 html 文件"""
    path = Path(path)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path


def parse_location(html):
    """辅助：从 HTML 中提取归属地文字，便于核对（不影响实验要求）"""
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.S):
        tds = re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)
        if len(tds) >= 2 and "卡号归属地" in tds[0]:
            return re.sub(r"<[^>]+>", "", tds[1]).strip()
    return "请在 HTML 中查看"


def query_phone_location(phone=MY_PHONE, out_file=OUT_FILE):
    """主流程：可复用，换手机号即可查询"""
    params = {"mobile": phone, "action": "mobile"}
    html = get_html(BASE_URL, params)
    if html is None:
        return None
    path = save_html(out_file, html)
    print("查询手机号:", phone)
    print("归属地:", parse_location(html))
    print("HTML 已保存:", path)
    return path


if __name__ == "__main__":
    query_phone_location()
