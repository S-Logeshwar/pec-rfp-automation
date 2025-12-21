import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def analyze_tender_with_llm(description):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": description}]
    )
    return {'score': 0.8, 'reasoning': response.choices[0].message.content}

def generate_response_with_llm(description):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": description}]
    )
    return response.choices[0].message.content
