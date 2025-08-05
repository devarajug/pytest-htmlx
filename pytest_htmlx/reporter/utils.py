from collections import Counter

def extract_suite_summary(test_data):
    # Count outcomes per suite
    suite_counters = {}

    for test in test_data:
        suite = test['test_suite']
        outcome = test['outcome']

        if suite not in suite_counters:
            suite_counters[suite] = Counter()

        suite_counters[suite][outcome] += 1

    # Create one list of suites and one nested list of data for Chart.js
    suites = list(suite_counters.keys())
    passed = [suite_counters[suite].get('passed', 0) for suite in suites]
    failed = [suite_counters[suite].get('failed', 0) for suite in suites]
    skipped = [suite_counters[suite].get('skipped', 0) for suite in suites]

    return suites, passed, failed, skipped


# Calculate percentages
def pct(count, total):
    return round((count / total) * 100, 1) if total else 0