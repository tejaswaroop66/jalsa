

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("KODEKEY_API_KEY")

if not api_key:
    raise ValueError("KodeKey API key not found in .env")

    client = OpenAI(
                api_key=api_key,
                    base_url=os.getenv("KODEKEY_BASE_URL")
                    )

    model = os.getenv("KODEKEY_MODEL")
