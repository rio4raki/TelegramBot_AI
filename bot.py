import configparser
import logging
import re
import asyncio
import json
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

def load_prompt(preset_name):
    """从JSON文件加载预设提示"""
    try:
        with open(config['SystemPrompt'][preset_name], 'r', encoding='utf-8') as f:
            preset = json.load(f)
            return preset['rules']
    except Exception as e:
        logging.error(f"加载预设提示失败: {e}")
        return "默认系统提示"

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

# 获取打字模拟配置
typing_enabled = config['TypingSimulation'].getboolean('Enabled')
base_delay = float(config['TypingSimulation']['BaseDelay'])

# 配置日志
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
TOKEN = config['TelegramBot']['Token']

async def start(update: Update, context):
    await update.message.reply_text('你好！我是你的Telegram机器人。')
    
async def help(update: Update, context):
    await update.message.reply_text('本程序为个人私有工具，仅限本人（使用者）非商业用途。禁止以任何形式共享、分发或允许第三方访问，否则由此产生的风险和责任由使用者自行承担。')
    
async def newchat(update: Update, context):
    # 清空当前用户的对话历史
    context.user_data['messages_history'] = [
        {"role": "system", "content": load_prompt('Preset1')}
    ]
    await update.message.reply_text('对话历史已清空，开始新的对话。')

async def echo(update: Update, context):
    from ai_chat import chat_with_ai
    
    # 验证用户ID是否在白名单中
    user_id = str(update.message.from_user.id)
    if user_id not in config['Whitelist']['IDs'].split(','):
        await update.message.reply_text('未授权用户')
        return
        
    # 为每个用户维护独立的对话历史
    if 'messages_history' not in context.user_data:
        context.user_data['messages_history'] = [
            {"role": "system", "content": load_prompt('Preset1')}
        ]
    replies = chat_with_ai(update.message.text, context.user_data['messages_history'])
    
    # 处理带图片的回复
    if isinstance(replies, dict):
        for reply in replies['text']:
            hanzi_count = len(re.findall(r'[\u4e00-\u9fa5]', reply))
            delay = hanzi_count * base_delay
            
            if typing_enabled:
                await context.bot.send_chat_action(
                    chat_id=update.effective_chat.id,
                    action='typing'
                )
            await update.message.reply_text(reply)
        
        with open(replies['image'], 'rb') as photo:
            await update.message.reply_photo(photo)
        return
    
    # 处理普通文本回复
    for reply in replies:
            # 计算汉字数量
            hanzi_count = len(re.findall(r'[\u4e00-\u9fa5]', reply))
            delay = hanzi_count * base_delay
            
            # 模拟打字效果
            if typing_enabled:
                await context.bot.send_chat_action(
                    chat_id=update.effective_chat.id,
                    action='typing'
                )
                # 更精确的延迟计算，每个汉字0.5秒基础延迟
                hanzi_count = len(re.findall(r'[\u4e00-\u9fa5]', reply))
                delay = max(1.0, hanzi_count * base_delay)  # 至少1秒延迟
                await asyncio.sleep(delay)
            await update.message.reply_text(reply)

def main():
    application = Application.builder().token(TOKEN).build()

    # 添加命令处理器
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("newchat", newchat))
    
    # 添加消息处理器
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # 启动轮询
    application.run_polling()

if __name__ == "__main__":
    main()
