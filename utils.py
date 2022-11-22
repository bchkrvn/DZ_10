import json

FILE_NAME = 'candidates.json'


def load_candidates() -> list:
    """
    Загружает список кандидатов из json-файла
    Returns: список кандидатов

    """
    with open(FILE_NAME, encoding='utf-8') as file:
        candidates = json.load(file)

    return candidates


def get_by_pk(pk: int) -> dict | None:
    """
    Позволяет получит информацию о кандидаты по его pk
    Args:
        pk: personal key

    Returns: словарь с информацией о кандидате, если он есть в базе

    """
    candidates = load_candidates()

    for candidat in candidates:
        if candidat['pk'] == pk:
            return candidat


def get_by_skill(skill_name: str) -> list:
    """
    Позволяет получить список кандидатов, обладающих указанным навыком
    Args:
        skill_name: навык

    Returns: список с кандидатами

    """
    candidates = load_candidates()
    candidates_with_skill = []

    for candidat in candidates:
        if skill_name.lower() in candidat['skills'].lower().split(', '):
            candidates_with_skill.append(candidat)

    return candidates_with_skill
