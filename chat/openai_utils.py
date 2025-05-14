import openai
import os
import json
from pathlib import Path
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

DATA_DIR = Path(__file__).resolve().parent.parent / "chat" / "data"

def load_knowledge_snippets():
    combined = []

    for file in DATA_DIR.glob("*.json"):
        with open(file) as f:
            data = json.load(f)
            # Flatten JSON (basic example, you can improve this per schema)
            for key, value in data.items():
                if isinstance(value, str):
                    combined.append(value)
                elif isinstance(value, list):
                    combined.extend(value)
                elif isinstance(value, dict):
                    combined.extend(value.values())

    for file in DATA_DIR.glob("*.txt"):
        with open(file) as f:
            combined.append(f.read())

    return "\n\n".join(combined)

def get_openai_response(prompt):
    system_context = load_knowledge_snippets()

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_context},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message["content"]
