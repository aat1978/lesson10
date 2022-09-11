import json


def load_candidates():
    """
    загрузит данные из файла
    :return:
    """
    with open('candidates.json', mode='r', encoding='utf-8') as json_data:
        d = json.load(json_data)
        return d


def get_all():
    """
    покажет всех кандидатов
    :return:
    """
    return load_candidates()


def get_by_pk(pk):
    """
    вернет кандидата по pk
    :param pk:
    :return:
    """
    for candidate in load_candidates():
        if candidate.get("pk") == pk:
            return candidate
    return "not found"


def get_by_skill(skill_name):
    """
    вернет кандидатов по навыку
    :param skill_name:
    :return:
    """
    result = []
    for candidate in load_candidates():
        skills = candidate['skills'].lower().split(", ")
        if skill_name in skills:
            result.append(candidate)
    return result

