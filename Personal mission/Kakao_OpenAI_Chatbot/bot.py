# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
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

@client.command(name='일정')
async def schedule(ctx, action: str, *, details: str = None):
    if action == '추가':
        # 일정 추가 로직
        await ctx.send(f"일정이 추가되었습니다: {details}")
    elif action == '조회':
        # 일정 조회 로직
        await ctx.send("일정 조회 결과입니다: ...")
    elif action == '삭제':
        # 일정 삭제 로직
        await ctx.send(f"일정이 삭제되었습니다: {details}")
    else:
        await ctx.send("알 수 없는 액션입니다. 사용 가능한 액션: 추가, 조회, 삭제")

@client.command(name='과제')
async def assignment(ctx, *, action: str):
    if action == '제출기한':
        # 과제 제출기한 안내 로직
        await ctx.send("다음 과제 제출 기한은 7월 30일입니다.")
    elif action == '제출방법':
        # 과제 제출 방법 안내 로직
        await ctx.send("과제 제출 방법은 다음과 같습니다: ...")
    else:
        await ctx.send("알 수 없는 액션입니다. 사용 가능한 액션: 제출기한, 제출방법")

@client.command(name='자료')
async def materials(ctx, *, topic: str):
    # 학습 자료 제공 로직
    await ctx.send(f"{topic}에 대한 학습 자료 링크입니다: ...")

@client.command(name='공지')
async def notice(ctx):
    # 공지사항 전달 로직
    await ctx.send("공지사항: ...")

# 봇 시작
client.run(DISCORD_TOKEN)
