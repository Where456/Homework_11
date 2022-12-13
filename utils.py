import json


def load_candidates_from_json():
    with open("candidates.json", 'r', encoding='utf-8') as f:
        text = json.load(f)
    return text


def get_candidate(candidate_id):
    text = load_candidates_from_json()
    for candidate in text:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    spisok = []
    text = load_candidates_from_json()
    for candidate in text:
        if candidate["name"] == candidate_name:
            spisok.append(candidate)
    return spisok


def get_candidates_by_skill(skill_name):
    spisok = []
    text = load_candidates_from_json()
    for i in text:
        if skill_name.lower() in i["skills"].lower():
            spisok.append(i)
    return spisok

