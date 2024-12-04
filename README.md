# Log Analyzer

A Python project that parses web server logs, analyzes them, and generates a report summarizing endpoint hits and login failures. This project is designed to help understand and monitor user behavior and failed login attempts based on server logs.

## Features
  ### Log Parsing: Parses structured log data from logs.txt to extract useful information.
  
   ### Analysis: Provides insights into:
   ### Most accessed endpoints.
   ### Failed login attempts grouped by IP addresses.
   ### Report Generation: Outputs a detailed report in report.txt.

## Directory Structure
    Myproject/
    │
    ├── utils/
    │   ├── parser.py       # Contains functions for parsing logs.
    │   ├── analyzer.py     # Contains functions for analyzing parsed logs.
    │
    ├── logs.txt            # Input log file.
    ├── main.py             # Main script to execute the project.
    ├── report.py           # Functions for generating reports.
    ├── requirements.txt    # Python dependencies for the project.
    ├── README.md           # Project documentation.

## Input Format
    <IP address> - - [<timestamp>] "<HTTP method> <endpoint> <protocol>" <status code> <response size>
## Example Log Entries:
     192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
    203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
    10.0.0.2 - - [03/Dec/2024:10:12:36 +0000] "GET /about HTTP/1.1" 200 256

    
    
## Output

  The report.txt file contains:

   Endpoint hits sorted by popularity.
   Login failure attempts grouped by IP addresses.
    
### Example Format: 
    Endpoint Hits:
    1. /home: 10 hits
    2. /login: 8 hits
    3. /about: 5 hits

    Login Failures:
    1. 203.0.113.5: 4 attempts
    2. 192.168.1.1: 2 attempts


