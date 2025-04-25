import configparser
import json
import logging
from openai import OpenAI

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

def load_prompt(preset_name):
    """从JSON文件加载预设提示"""
    try:
        with open(config['SystemPrompt'][preset_name], 'r', encoding='utf-8') as f:
            preset = json.load(f)
            return preset['rules']
    except Exception as e:
        logging.error(f"加载预设提示失败: {e}")
        return "默认系统提示"

# 获取API配置
API_KEY = config['OneAPI']['ApiKey']
API_URL = config['OneAPI']['ApiUrl']
MODEL = config['OneAPI']['Model']

# 初始化OpenAI客户端
client = OpenAI(api_key=API_KEY, base_url=API_URL)

def chat_with_ai(message, messages_history=None, preset_name='Preset1'):
    """
    与AI聊天
    :param message: 用户输入的消息
    :param messages_history: 对话历史记录
    :param preset_name: 当前使用的预设名称
    :return: AI的回复
    """
    if messages_history is None:
        messages_history = [
            {"role": "system", "content": load_prompt(preset_name)}
        ]
    
    # 获取当前本地时间和天气
    from datetime import datetime
    from SearchWeather import SearchWeather
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        weather = SearchWeather().get_current_weather(config['WeatherAPI']['CityCode'])
    except Exception as e:
        logging.error(f"天气查询失败: {e}")
        weather = "天气信息获取失败"
    
    message_with_time = f"[当前时间: {current_time} 天气: {weather}] {message}"
    
    messages_history.append({"role": "user", "content": message_with_time})
    
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages_history,
            stream=False,
            timeout=30  # 增加超时时间
        )
        assistant_message = response.choices[0].message
        messages_history.append(assistant_message)
        
        # 处理分段回复
        split_char = config['ResponseFormat']['SplitCharacter']
        max_sentences = int(config['ResponseFormat']['MaxSentences'])
        
        # 按反斜杠分割并限制句子数量
        sentences = assistant_message.content.split(split_char)
        filtered_sentences = [s.strip() for s in sentences[:max_sentences] if s.strip()]
        
        # 检查是否包含图片标记
        keywords = config['Keywords']['Images'].split(',')
        image_matches = []
        for keyword in keywords:
            matches = [s for s in filtered_sentences if keyword in s]
            if matches:
                image_matches.append(keyword)
                
        if image_matches:
            return {
                'text': filtered_sentences,
                'image': f'image/{image_matches[0]}'
            }
        
        return filtered_sentences
    except Exception as e:
        print(f"API请求出错: {str(e)}")
        if "timed out" in str(e):
            return "请求处理中，请稍后再试"  # 优化超时提示
        return "消息处理出错"

if __name__ == "__main__":
    messages_history = [
        {"role": "system", "content": load_prompt('Preset1')}
    ]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        reply = chat_with_ai(user_input, messages_history)
        print(f"AI: {reply}")
