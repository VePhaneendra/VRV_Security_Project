def analyze_logs(logs):
    results = {
        "status_counts": {},    # Status code counts
        "endpoint_hits": {},    # Endpoint hit counts
        "login_failures": {},   # Login failures per IP
    }

    for log in logs:
        # Count status codes
        status = log["status"]
        results["status_counts"][status] = results["status_counts"].get(status, 0) + 1

        # Count endpoint hits
        endpoint = log["endpoint"]
        results["endpoint_hits"][endpoint] = results["endpoint_hits"].get(endpoint, 0) + 1

        # Track login failures by IP
        if endpoint == "/login" and status == 401:
            ip = log["ip"]
            results["login_failures"][ip] = results["login_failures"].get(ip, 0) + 1

    return results
