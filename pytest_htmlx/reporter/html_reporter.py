import os
import shutil
from jinja2 import Environment, FileSystemLoader

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
        assets_dir = os.path.join(template_dir, "assets")
        output_dir = os.path.dirname(os.path.abspath(self.report_path))
        output_assets_dir = os.path.join(output_dir, "assets")

        # Copy assets (CSS/JS) to output directory
        if os.path.exists(assets_dir):
            if os.path.exists(output_assets_dir):
                shutil.rmtree(output_assets_dir)
            shutil.copytree(assets_dir, output_assets_dir)

        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template("base.html")

        passed = sum(1 for r in self.results if r.get("outcome", "").lower() == "passed")
        failed = sum(1 for r in self.results if r.get("outcome", "").lower() == "failed")
        skipped = sum(1 for r in self.results if r.get("outcome", "").lower() == "skipped")
        total = len(self.results)

        # Calculate percentages
        def pct(count):
            return round((count / total) * 100, 1) if total else 0

        html = template.render(
            results=self.results,
            passed=passed,
            failed=failed,
            skipped=skipped,
            total=total,
            passed_pct=pct(passed),
            failed_pct=pct(failed),
            skipped_pct=pct(skipped),
            assets_path="assets",
        )

        with open(self.report_path, "w", encoding="utf-8") as f:
            f.write(html)

    def display_results(self):
        # Optional: print results to console
        for result in self.results:
            print(result)
