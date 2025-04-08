# survey_app/utils.py
import json
import os

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
