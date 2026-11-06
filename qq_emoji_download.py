# -*- coding: utf-8 -*-
"""
实验 1-1：QQ 表情包图片下载（代码重构可复用版）
教材《数据采集与预处理》第 3 章 3.4 案例 1

重构思路：把「请求信息」「发送请求」「保存文件」拆成独立可复用单元，
再由 main 流程组合，做到调用代码与通用函数分离。
"""
from pathlib import Path
from urllib.parse import urlparse

import requests

# ==================== ① 定义请求信息 ====================
# 教材原站点 www.bspider.top 已失效，这里替换为 QQ 官方表情资源，
# 请求方式与教材完全一致（GET -> 二进制内容 -> 写文件）。
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}
TIMEOUT = 10

URL_LIST = [
    "https://qzonestyle.gtimg.cn/qzone/em/e100.gif",
    "https://qzonestyle.gtimg.cn/qzone/em/e101.gif",
    "https://qzonestyle.gtimg.cn/qzone/em/e102.gif",
    "https://qzonestyle.gtimg.cn/qzone/em/e103.gif",
    "https://qzonestyle.gtimg.cn/qzone/em/e104.gif",
]

SAVE_DIR = Path(__file__).parent / "images"


# ==================== ② 发送请求并获得响应 ====================
def get_image(url, headers=HEADERS, timeout=TIMEOUT):
    """获取单张图片的二进制数据；失败返回 None"""
    try:
        r = requests.get(url, headers=headers, timeout=timeout)
        r.raise_for_status()          # 非 200 抛异常，避免把错误页当图片保存
        return r.content              # 图片是二进制数据，用 content 而非 text
    except Exception as err:
        print("请求失败:", url, err)
        return None


# ==================== ③ 将响应图片存储到本地 ====================
def save_image(path, content):
    """把图片二进制数据写入本地文件"""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:       # wb：二进制写入
        f.write(content)
    return path


def get_filename(url):
    """从 URL 中取出原始文件名，例如 e100.gif"""
    return Path(urlparse(url).path).name or "emoji.gif"


def download_emojis(url_list=URL_LIST, save_dir=SAVE_DIR):
    """主流程：可复用，换 URL 列表或保存目录即可批量下载"""
    saved = []
    for url in url_list:
        content = get_image(url)
        if content is None:
            continue
        path = save_image(save_dir / get_filename(url), content)
        saved.append(path)
        print("已保存:", path)
    return saved


if __name__ == "__main__":          # main 流程控制，调用代码与函数分离
    files = download_emojis()
    print("共下载", len(files), "张表情包 ->", SAVE_DIR)
