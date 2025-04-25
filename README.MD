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
bash
git clone https://github.com/rio4raki/TelegramBotV1.1.git

2. 安装依赖
bash
pip install -r requirements.txt

3. 配置`config.ini`文件（见下方配置说明）

4. 运行机器人

python main.py


## 配置文件说明

编辑`config.ini`文件进行配置：

```ini
[TelegramBot]
Token = 你的Telegram机器人Token

[OneAPI]
ApiKey = 你的OneAPI密钥
ApiUrl = https://api.siliconflow.cn/v1/   #这里是使用硅基流动的API进行举例，你也可以使用不同中转站/官方API
Model = deepseek-ai/DeepSeek-V3

[WeatherAPI]
Key = 高德地图天气API Key
CityCode = 城市代码(6位数字)

[Whitelist]
IDs = 你的Telegram用户ID(多个用逗号分隔)





#关于发送图片功能的特殊说明
本项目支持TelegramBot，程序可以查找AI返回结果的特定关键词来发送图片，特定关键词格式为[示例图片.jpg]，存放到IMAG文件夹中。
提示词示例：你需要根据讨论的话题来选择照片，需要已有照片和目前的聊天内容必须相近才可以输出

#关于天气与时间的特殊说明
天气系统通过接入高德地图的API进行获取，目前支持特定地区/温度/湿度/风速，高德地图支持每天500次的免费调用
时间系统通过获取系统的本地时间

#关于模拟打字时间的特殊说明
程序通过设定每一个字的打字间隔来实现“正在输入...”，具体可以在Config.ini进行配置，你也可以修改为0.01来达到关闭秒回复的效果。

#关于提示词/分段回复的特殊说明
目前提供的提示词可以让系统进行最基本的功能，更多功能的实现需要特定的提示词来达成。分段回复功能通过解析特定符号来实现分段

#未来计划添加功能

1.预设热切换
2.记忆提炼/浓缩
3.API热切换
4.Token消耗统计
5.更加卓越的性能架构


## 命令列表

- `/start` - 启动机器人
- `/help` - 显示帮助信息
- `/newchat` - 重置对话历史

## 项目结构

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




## 注意事项

1. 本项目仅限非商业用途
2. 禁止未经授权共享或分发
3. 使用前请确保已获得所有必要的API密钥

## 许可证

本项目为私有项目，未经许可不得分发。

