"""Verify the installed package loads without credentials or API access."""

import os
import subprocess
import sys


def test_installed_package_imports_without_credentials() -> None:
    env = {key: value for key, value in os.environ.items() if "KEY" not in key}
    result = subprocess.run(
        [sys.executable, "-I", "-c", "import pipeline_integrity_bench"],
        env=env,
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    assert result.returncode == 0, result.stderr
