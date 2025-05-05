# survey_app/utils.py
import json
import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def load_chatbot_prompt():
    file_path = os.path.join(os.path.dirname(__file__), 'chatbot_prompt.txt')
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def ask_llama3(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": load_chatbot_prompt()},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def load_survey_definition():
    file_path = os.path.join(os.path.dirname(__file__), 'survey_questions.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def load_page_links():
    file_path = os.path.join(os.path.dirname(__file__), 'pageLinks.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
