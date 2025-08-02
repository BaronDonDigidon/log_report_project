from typing import List, Dict, Any, Tuple
from .utils import filter_by_date

@filter_by_date
def analyze(logs: List[Dict[str, Any]], date=None) -> Dict[str, Dict[str, float]]:
    """
    Обрабатывает json файл и выводит словарь с эндпоинтами, общим количеством
    заропос и сумарным временем отклика по ним. Необязательный параметр date для получения
    информации по эндпоинтам на определенную дату.
    :param logs:
    :type logs: List[Dict[str, Any]]
    :param date: дата запроса эндпоинта (необязательный параметр)
    :type date: str
    :return: словарь с эндпоинтами, общим количеством заропос и сумарным временем отклика по ним.
    :rtype: Dict[str, Dict[str, float]]
    """
    stats = {}
    for entry in logs:
        url = entry.get("url")
        if url:
            if url not in stats:
                stats[url] = {"count": 0, "response_time": 0.0}
            stats[url]["count"] += 1
            stats[url]["response_time"] += entry.get("response_time", 0.0)
    return stats


def average_stats(stats_dict: Dict[str, Dict[str, int]]) -> List[Tuple[str, int, float]]:
    """
    Создает список списков с общим количеством запросов по эндпоинтам и средним временем отлика.
    :param stats_dict:
    :type stats_dict:
    :return: список списков с общим количеством запросов по эндпоинтам и средним временем отлика.
    :rtype: List[List[str, int, float]]
    """
    avg_stats = []
    for path, data in stats_dict.items():
        avg_response_time = data["response_time"] / data["count"]
        avg_stats.append([path, data["count"], round(avg_response_time, 3)])
    return avg_stats