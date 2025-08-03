import pytest
from pytest_htmlx.reporter.html_reporter import HTMLReporter

def pytest_addoption(parser):
    parser.addoption("--htmlx", action="store", default="report.html", help="Path to save HTML report")

def pytest_configure(config):
    if not hasattr(config, "htmlx_reporter"):
        config.htmlx_reporter = HTMLReporter(config.getoption("--htmlx"))

def pytest_runtest_logreport(report):
    reporter = HTMLReporter()

    if report.when == "call":
        outcome = {
            "name": report.nodeid,
            "outcome": report.outcome,
            "duration": report.duration,
            "longrepr": str(report.longrepr) if report.failed else "",
        }
        
        reporter.add_result(outcome)

def pytest_sessionfinish(session, exitstatus):
    reporter = getattr(session.config, "htmlx_reporter", None)
    reporter.display_results()
    if reporter is not None:
        reporter.generate_report()
