import discord
import openai
import config

# OpenAI API 키 설정
openai.api_key = config.OPENAI_API_KEY

# 디스코드 클라이언트 설정
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!질문'):
        prompt = message.content[len('!질문 '):]
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        await message.channel.send(response.choices[0].text.strip())

client.run(config.DISCORD_TOKEN)
