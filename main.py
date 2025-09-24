import os
import cohere
from dotenv import load_dotenv

load_dotenv()

def main():
    co = cohere.ClientV2(api_key=os.getenv("COHERE_API_KEY"))
    response = co.chat(
        model = os.getenv("COHERE_DEFAULT_MODEL"),
        messages = [{"role": "user", "content": "Hello World?"}]
    )
    print(response)


if __name__ == "__main__":
    main()
