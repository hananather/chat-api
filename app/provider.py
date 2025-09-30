import os
import cohere
from dotenv import load_dotenv
from abc import ABC, abstractmethod

load_dotenv()

class Provider(ABC):
    @abstractmethod
    def chat(self, message: str) -> str:    
        pass

class CohereProvider(Provider):
    """Basic test provider that echoes the input message."""
    name = "cohere-0"

    def chat(self, message: str) -> str:
        co = cohere.ClientV2(api_key=os.getenv("COHERE_API_KEY"))
        response = co.chat(
            model=os.getenv("COHERE_DEFAULT_MODEL"),
            messages=[{"role": "user", "content": message}]
        )

        # extract text from all content items
        text_parts = []
        for item in response.message.content:
            if item.type == "text":
                text_parts.append(item.text)
        return ''.join(text_parts)
