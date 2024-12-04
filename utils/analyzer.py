# utils/analyzer.py

def analyze_logs(logs):
    # Dummy implementation for analyzing logs
    analysis_results = {
        "endpoint_hits": {},
        "login_failures": {}
    }
    
    for log in logs:
        # Example of endpoint hit analysis
        endpoint = log.get("endpoint")
        if endpoint:
            analysis_results["endpoint_hits"][endpoint] = analysis_results["endpoint_hits"].get(endpoint, 0) + 1
        
        # Example of login failure analysis
        status = log.get("status")
        if status == "401":  # Assuming 401 is a login failure
            ip = log.get("ip")
            if ip:
                analysis_results["login_failures"][ip] = analysis_results["login_failures"].get(ip, 0) + 1

    return analysis_results
