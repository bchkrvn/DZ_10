import json

FILE_NAME = 'candidates.json'


def load_candidates():
    with open(FILE_NAME, encoding='utf-8') as file:
        candidates = json.load(file)

    return candidates


def get_by_pk(pk):
    candidates = load_candidates()

    for candidat in candidates:
        if candidat['pk'] == pk:
            return candidat


def get_by_skill(skill_name):
    candidates = load_candidates()
    candidates_with_skill = []

    for candidat in candidates:
        if skill_name.lower() in candidat['skills'].lower().split(', '):
            candidates_with_skill.append(candidat)

    return candidates_with_skill
