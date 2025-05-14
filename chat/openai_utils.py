import json
import os
from django.conf import settings
from openai import OpenAI

client = OpenAI(api_key=settings.OPENAI_API_KEY)

# Load all knowledge base files in chat/data
def load_knowledge_base():
    base_path = os.path.join(settings.BASE_DIR, "chat", "data")
    knowledge = []

    for filename in os.listdir(base_path):
        if filename.endswith(".json"):
            with open(os.path.join(base_path, filename), "r") as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        knowledge.extend(data)
                    elif isinstance(data, dict):
                        knowledge.append(data)
                except Exception as e:
                    print(f"Error loading {filename}: {e}")
    return knowledge

# Build system prompt with injected knowledge base
def get_openai_response(user_message):
    context_blocks = load_knowledge_base()
    system_content = "You are a helpful assistant on MatthewRaynor.com. Use the following context when answering questions:\n\n"

    for block in context_blocks:
        system_content += f"- {block.get('title', '')}: {block.get('content', '')}\n"

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content.strip()
