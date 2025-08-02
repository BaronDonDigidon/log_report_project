from typing import List
from tabulate import tabulate

def sorted_average_stats(avg_stats_list: List[any], sorted_row: int = 1) -> List:
    """
    Сортирует список, по убыванию количества запросов.
    :param avg_stats_list:
    :type avg_stats_list:
    :param sorted_row:
    :type sorted_row:
    :return:
    :rtype:
    """
    avg_stats_list.sort(key=lambda row: row[sorted_row], reverse=True)
    return avg_stats_list


def print_info(avg_stats_list: List) -> None:
    """
    Выводит данные отчёта на экран
    :param avg_stats_list: лист с количеством запросов по эндпоинту и среднему времени отклика.
    :type avg_stats_list: List[any]
    """
    header = ["handler", "total", "avg_response_time"]
    print(tabulate(avg_stats_list, header))