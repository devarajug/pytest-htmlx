import os
from jinja2 import Environment, FileSystemLoader
from pytest_htmlx.reporter.utils import extract_suite_summary, pct

class HTMLReporter:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, report_path="report_default.html"):
        if self._initialized:
            return
        self.report_path = report_path
        self.results = []
        self._initialized = True

    def add_result(self, outcome):
        self.results.append(outcome)

    def generate_report(self):
        base_dir = os.path.dirname(__file__)
        template_dir = os.path.join(base_dir, "templates")

        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template("base.html")

        passed = sum(1 for r in self.results if r.get("outcome", "").lower() == "passed")
        failed = sum(1 for r in self.results if r.get("outcome", "").lower() == "failed")
        skipped = sum(1 for r in self.results if r.get("outcome", "").lower() == "skipped")
        total = passed + failed + skipped
        
        # Prepare data for the bar chart

        suites, passed_by_suite, failed_by_suite, skipped_by_suite = extract_suite_summary(self.results)
        test_suites = suites if suites else ["No Suites Found"]

        # Prepare data for the duration chart
        test_names = [t["test_name"] for t in self.results]
        durations = [round(t["duration"], 6) for t in self.results]
        

        html = template.render(
            results=self.results,
            passed=passed,
            failed=failed,
            skipped=skipped,
            total=total,
            passed_pct=pct(passed, total),
            failed_pct=pct(failed, total),
            skipped_pct=pct(skipped, total),
            test_suites=test_suites,  # Example test suites
            passed_by_suite=passed_by_suite,
            failed_by_suite=failed_by_suite,
            skipped_by_suite=skipped_by_suite,
            tests_duration=durations,
            test_names=test_names,
        )

        with open(self.report_path, "w", encoding="utf-8") as f:
            f.write(html)

    def display_results(self):
        # Optional: print results to console
        for result in self.results:
            print(result)
