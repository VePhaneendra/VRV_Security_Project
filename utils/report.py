def generate_report(analysis_results, report_file):
    with open(report_file, "w") as f:
        f.write("Log Analysis Report\n")
        f.write("===================\n\n")

        # Status counts
        f.write("Status Counts:\n")
        for status, count in analysis_results.get("status_counts", {}).items():
            f.write(f"{status}: {count}\n")

        # Endpoint hits
        f.write("\nEndpoint Hits:\n")
        for endpoint, count in analysis_results.get("endpoint_hits", {}).items():
            f.write(f"{endpoint}: {count}\n")

        # Login failures
        f.write("\nLogin Failures:\n")
        login_failures = analysis_results.get("login_failures", {})
        if login_failures:
            for ip, count in login_failures.items():
                f.write(f"{ip}: {count}\n")
        else:
            f.write("No login failures recorded.\n")
