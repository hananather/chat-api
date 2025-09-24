import os
import cohere
from dotenv import load_dotenv

load_dotenv()

prompt = """
Alice has 3 brothers and she also has 2 sisters. How many sisters does Alice's brother have?
"""


def cohere_reasoning():
    co = cohere.ClientV2(api_key=os.getenv("COHERE_API_KEY"))
    response = co.chat(
        model="command-a-reasoning-08-2025",
        messages=[{"role": "user", "content": prompt}]
    )
    for content in response.message.content:
        if content.type == "thinking":
            print("Thinking:", content.thinking)
        
        if content.type == "text":
            print("Response:", content.text)

if __name__ == "__main__":
    cohere_reasoning()
