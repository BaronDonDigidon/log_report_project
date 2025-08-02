import subprocess
import os

def test_main_script_runs():
    log_path_1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "data", "example1.log"))
    log_path_2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "data", "example2.log"))
    result = subprocess.run(
        ["python", "main.py", "--file", log_path_1, log_path_2, "--report", "average", "--data", "2025-06-22"],
        capture_output=True,
        text=True,
        cwd=os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    )
    print(result.stderr)
    print(result.stdout)
    assert "handler" in result.stdout