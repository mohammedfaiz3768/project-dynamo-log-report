import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def test_report_exists():
    """The agent produced a report file."""
    assert REPORT_PATH.exists(), "no report.json found"


def test_report_is_valid_json():
    """The report file contains valid JSON."""
    data = json.loads(REPORT_PATH.read_text())
    assert isinstance(data, dict), "report.json root is not a JSON object"


def test_total_requests():
    """The report contains the correct total request count."""
    data = json.loads(REPORT_PATH.read_text())
    assert data.get("total_requests") == 6, (
        f"expected total_requests=6, got {data.get('total_requests')}"
    )


def test_unique_ips():
    """The report contains the correct number of unique client IPs."""
    data = json.loads(REPORT_PATH.read_text())
    assert data.get("unique_ips") == 3, (
        f"expected unique_ips=3, got {data.get('unique_ips')}"
    )


def test_top_path():
    """The report identifies the most-requested path."""
    data = json.loads(REPORT_PATH.read_text())
    assert data.get("top_path") == "/index.html", (
        f"expected top_path='/index.html', got {data.get('top_path')}"
    )
