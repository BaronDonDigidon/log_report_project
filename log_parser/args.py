import argparse

def args_parser() -> argparse.Namespace:
    """
    Обработчик командной строки, запрашивает путь к файлу (файлов может быть несколько) и тип отчёта.
    :return: пути к файлам, тип отчета и дату запроса(необязательный параметр)
    :rtype: argparse.Namespace
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Описание программы")
    parser.add_argument(
        "--file", nargs="+", required=True,
        help="Путь к файлу"
    )
    parser.add_argument(
        "--report", required=True, choices=["average"],
        help="Тип отчёта "
    )
    parser.add_argument(
        "--data", default=None,
        help="Дата записи в формате: yyyy-mm-dd (необязательный параметр)"
    )
    return parser.parse_args()