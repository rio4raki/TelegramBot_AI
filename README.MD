# TelegramBotV1.1 智能聊天机器人

一个基于Python的TelegramBOT聊天机器人，集成天气查询和AI对话功能。

## 功能特点

- 🤖 智能AI对话（支持OneApi格式）
- ⛅ 实时天气查询（使用高德地图API）
- 🖼️ 支持关键词触发图片回复
- ⌨️ 打字效果模拟
- 🔒 白名单用户授权机制
- 💬 多角色预设支持 （未来支持）

## 技术栈

- Python 3.x
- python-telegram-bot 20.6
- OpenAI 1.12.0
- 高德地图天气API

## 快速开始

1. 克隆仓库
```bash
git clone https://github.com/your-repo/TelegramBotV1.1.git
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置`config.ini`文件（见下方配置说明）

4. 运行机器人
```bash
python main.py
```

## 配置文件说明

编辑`config.ini`文件进行配置：

```ini
[TelegramBot]
Token = 你的Telegram机器人Token

[OneAPI]
ApiKey = 你的OneAPI密钥
ApiUrl = https://api.siliconflow.cn/v1/
Model = deepseek-ai/DeepSeek-V3

[WeatherAPI]
Key = 高德地图天气API Key
CityCode = 城市代码(6位数字)

[Whitelist]
IDs = 你的Telegram用户ID(多个用逗号分隔)
```

## 命令列表

- `/start` - 启动机器人
- `/help` - 显示帮助信息
- `/newchat` - 重置对话历史

## 项目结构

```
TelegramBotV1.1/
├── Roles/                # 角色预设文件夹
│   └── 1.json           # 角色预设文件
├── image/                # 图片资源
├── ai_chat.py            # AI聊天核心逻辑
├── bot.py                # Telegram机器人主逻辑
├── config.ini            # 配置文件
├── main.py               # 程序入口
├── SearchWeather.py       # 天气查询模块
└── requirements.txt      # 依赖列表
```

## 注意事项

1. 本项目为个人私有工具，仅限非商业用途
2. 禁止未经授权共享或分发
3. 使用前请确保已获得所有必要的API密钥

## 许可证

本项目为私有项目，未经许可不得分发。
```

这个README文件包含了项目的主要信息，您可以根据需要进一步调整内容。需要特别注意：

1. 请确保替换所有`[输入你的...]`占位符为实际配置值
2. 角色预设文件(`Roles/1.json`)可以根据需要添加更多
3. 图片资源应放在`image/`目录下，并在`config.ini`的`[Keywords]`部分配置触发关键词

