from typing import Callable, List, Dict, Any
from datetime import datetime, date

def filter_by_date(func) -> Callable:
    """
    Декоратор для функции analyze, при добавлении параметра date, функция получает на вход список
    с запросами по эндопинтам только на указанную дату.
    """
    def wrapper(logs, date=None) -> Callable:
        if date:
            logs: List[Dict[str, Any]] = [entry for entry in logs if is_same_date(entry.get("@timestamp", ""), date)]
        return func(logs, date=date)
    return wrapper

def is_same_date(timestamp: str, date_str: str) -> bool:
    """
    Проверяет дату на соотвествие.
    :param timestamp: дата в словаре.
    :param date_str: искомая дата.
    :return: bool
    """
    try:
        log_date: date = datetime.fromisoformat(timestamp).date()
        filter_date: date = datetime.fromisoformat(date_str).date()
        return log_date == filter_date
    except Exception as e:
        print(f"[ERROR] {e}")
        return False