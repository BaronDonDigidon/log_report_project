from typing import List, Dict
import json
import os

def load_logs(filepaths: str) -> List[Dict[str, int]]:
    """
    Обрабатывает файлы логов и возвращает их в качестве списка.
    :param filepaths: список путей к файлам.
    :type filepaths: List[str]
    :return: список словарей с логами.
    :rtype: List[Dict[str, int]]
    """
    all_logs: List = []
    for filepath in filepaths:
        try:
            with open(os.path.abspath(filepath), "r", encoding="UTF-8") as file:
                for line in file:
                    logs = json.loads(line)
                    all_logs.append(logs)
        except FileNotFoundError as e:
            print(f"Файл по пути - {filepath} не найден.\n"
                  f"Ошибка: {e}")
    return all_logs