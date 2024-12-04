from utils.parser import parse_logs
from utils.analyzer import analyze_logs
from utils.report import generate_report

def main():
    log_file = "logs.txt"  # Ensure your sample log data is saved in this file
    logs = parse_logs(log_file)
    print("Parsed Logs:", logs)  # Debug: Inspect parsed logs
    
    analysis_results = analyze_logs(logs)
    print("Analysis Results:", analysis_results)  # Debug: Inspect analysis results
    
    generate_report(analysis_results, "report.txt")
    print("Report generated: report.txt")

if __name__ == "__main__":
    main()
