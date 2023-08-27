from ai_assignment_marker.cli import cli
import os

class TestCLI:
    def test_cli(self):
        exit_code = os.system("python ai_assignment_marker/cli.py")
        assert exit_code == 0