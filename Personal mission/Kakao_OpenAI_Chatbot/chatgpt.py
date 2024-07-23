# chatgpt.py
import os
import time
from openai import OpenAI
from dotenv import load_dotenv

# .env 파일에서 환경 변수를 로드
load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY')
# OpenAI API 클라이언트 설정
client = OpenAI(api_key=OPENAI_KEY)

def send_to_chatGpt(messages, model="gpt-3.5-turbo"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=500,
            temperature=0.5,
        )
        message = response.choices[0].message.content
        print(message)
        messages.append({"role": "assistant", "content": message})
        return message
    except Exception as e:
        if "Rate limit" in str(e):
            print("쿼터 초과. 플랜 및 결제 내역을 확인하세요.")
            time.sleep(60)  # 60초 대기 후 재시도
            return "쿼터 초과. 나중에 다시 시도해주세요."
        else:
            print(f"오류 발생: {e}")
            return "요청 처리 중 오류가 발생했습니다. 나중에 다시 시도해주세요."