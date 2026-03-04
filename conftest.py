import pytest
from datetime import  datetime

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d__%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/reports_{now}.html"

@pytest.fixture(scope = "session",autouse=True)
def setup_teardown():
    print("starting")
    yield
    print("finishing")
