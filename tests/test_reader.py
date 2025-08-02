import pytest
from log_parser.reader import load_logs

def test_load_logs(tmp_path):
    test_log = tmp_path / "log.json"
    test_log.write_text('{"url": "/test", "response_time": 0.2, "@timestamp": "2025-08-01T10:00:00"}\n')
    logs = load_logs([str(test_log)])
    assert len(logs) == 1
    assert logs[0]["url"] == "/test"