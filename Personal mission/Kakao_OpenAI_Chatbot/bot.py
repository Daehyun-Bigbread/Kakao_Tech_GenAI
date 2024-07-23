# bot.py
import os
import discord
from dotenv import load_dotenv
from chatgpt import send_to_chatGpt

# .env 파일에서 환경 변수를 로드
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name}로 로그인되었습니다.')

@client.event
async def on_message(message):
    # 봇 자신의 메시지는 무시하고 다른 사용자의 메시지만 응답
    if message.author == client.user:
        return

    # OpenAI API 응답
    messages = [{"role": "user", "content": message.content}]
    response = send_to_chatGpt(messages)
    # 응답을 메시지로 전송
    await message.channel.send(response)

# 봇 시작
client.run(DISCORD_TOKEN)
