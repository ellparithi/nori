
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

conversation_history = []

def generate_reply(user_input):
    conversation_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are Nori, a warm, friendly human speaking in a natural, casual tone. Keep responses short, expressive, and emotionally human — like talking to a close friend or family member. Do not sound like a chatbot or assistant"}] + conversation_history,
        max_tokens=60,
        temperature=0.7
    )

    reply = response.choices[0].message.content.strip()
    conversation_history.append({"role": "assistant", "content": reply})
    return reply
