# 大数据采集与处理 实验 1

- 姓名：张欣
- 学号：112403110105
- 班级：软件1241
- GitHub 用户名：chengranxx
- 仓库地址：https://github.com/chengranxx/bigdata-collection-labs-112403110105

> 本文件是 GitHub 仓库首页（提交说明第 2 节要求），**不是**要交的 Word 实验报告。

## 实验内容

参考教材《数据采集与预处理》第 3 章，使用 `requests` 完成两个任务，均编写为代码重构可复用版。

| 任务 | 代码文件 | 运行后产物 |
|---|---|---|
| 3.4 案例 1 · QQ 表情包图片下载 | `qq_emoji_download.py` | `images/` 下 5 张 GIF 表情 |
| 3.5 案例 2 · 手机归属地查询 | `phone_location.py` | `phone_location.html`（响应源代码） |

## 目录结构

```text
.
├── README.md                 本文件
├── qq_emoji_download.py      任务 1：定义请求信息 / 发送请求 / 保存图片
├── phone_location.py         任务 2：定义请求信息 / 发送请求 / 保存 html
├── phone_location.html       任务 2 抓取到的响应源代码（含本人手机号与归属地）
└── images/                   任务 1 下载的表情包
    ├── e100.gif
    ├── e101.gif
    ├── e102.gif
    ├── e103.gif
    └── e104.gif
```

## 运行环境

- 开发语言：Python 3.13（Anaconda base）
- 调用的包：`requests`；标准库 `pathlib` / `urllib.parse` / `re`
- 调试和运行环境：VSCode + Anaconda + Windows

## 说明

教材原站点 `www.bspider.top` 已失效（HTTP 403 / 404），故替换为 QQ 官方表情资源
`qzonestyle.gtimg.cn` 与 ip138 官方查询页 `www.ip138.com/mobile.asp`，
请求方式、参数形式与三段式代码结构与教材案例一致。
