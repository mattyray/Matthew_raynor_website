import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant for Matthew Raynor’s personal website. Be concise, helpful, and kind. You help people understand Matt’s story, his projects, how to log in, use the site, or donate."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message["content"]
