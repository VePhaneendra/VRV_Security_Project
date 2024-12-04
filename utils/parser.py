import re

def parse_logs(log_file):
    logs = []
    log_pattern = re.compile(
        r'(?P<ip>\S+) - - \[(?P<timestamp>[^\]]+)] "(?P<method>\S+) (?P<endpoint>\S+) \S+" (?P<status>\d+) (?P<response_size>\d+)'
    )

    with open(log_file, "r") as f:
        for line in f:
            match = log_pattern.match(line)
            if match:
                log_data = match.groupdict()
                log_data["status"] = int(log_data["status"])  # Convert status to int
                log_data["response_size"] = int(log_data["response_size"])  # Convert size to int
                logs.append(log_data)
    return logs
