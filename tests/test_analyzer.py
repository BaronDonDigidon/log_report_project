import pytest
from log_parser.analyzer import analyze, average_stats


# Пример логов
logs = [
    {
        "url": "/api/v1/user",
        "response_time": 120,
        "@timestamp": "2025-08-01T10:00:00"
    },
    {
        "url": "/api/v1/user",
        "response_time": 80,
        "@timestamp": "2025-08-01T11:00:00"
    },
    {
        "url": "/api/v1/order",
        "response_time": 200,
        "@timestamp": "2025-07-30T09:30:00"
    }
]


def test_analyze_all_logs():
    result = analyze(logs)
    assert result["/api/v1/user"]["count"] == 2
    assert result["/api/v1/user"]["response_time"] == 200
    assert result["/api/v1/order"]["count"] == 1
    assert result["/api/v1/order"]["response_time"] == 200


def test_analyze_with_date_filter():
    result = analyze(logs, date="2025-08-01")
    assert "/api/v1/order" not in result
    assert "/api/v1/user" in result
    assert result["/api/v1/user"]["count"] == 2
    assert result["/api/v1/user"]["response_time"] == 200


def test_analyze_with_empty_date():
    result = analyze(logs, date="2025-08-15")
    assert result == {}


def test_average_stats():
    input_data = {
        "/api/test": {
            "count": 2,
            "response_time": 1.0  # Суммарно
        }
    }
    result = average_stats(input_data)
    assert result == [["/api/test", 2, 0.5]]
