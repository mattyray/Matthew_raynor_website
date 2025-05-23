# chatwidget/openai_utils.py

import os
import json
from django.conf import settings
from openai import OpenAI

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def load_knowledge_base():
    base_path = os.path.join(os.path.dirname(__file__), "data")
    knowledge = []

    if not os.path.exists(base_path):
        return knowledge

    for filename in os.listdir(base_path):
        if filename.endswith(".json"):
            try:
                with open(os.path.join(base_path, filename), "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        knowledge.extend(data)
                    elif isinstance(data, dict):
                        knowledge.append(data)
            except Exception as e:
                print(f"Error loading {filename}: {e}")
    return knowledge

def get_openai_response(user_message):
    context_blocks = load_knowledge_base()
    system_prompt = "You are a helpful assistant. Use the following context to answer questions:\n\n"

    for block in context_blocks:
        system_prompt += f"- {block.get('title', '')}: {block.get('content', '')}\n"

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content.strip()
