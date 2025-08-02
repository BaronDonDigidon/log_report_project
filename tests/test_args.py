import sys
from log_parser.args import args_parser

def test_args_parser(monkeypatch):
    test_args = ["main.py", "--file", "test1.json", "--report", "average"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = args_parser()
    assert args.file == ["test1.json"]
    assert args.report == "average"