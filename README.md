# Web_Search
This scanner performs automated security checks including port scanning, vulnerability detection, and security configuration analysis. It's designed for quick security assessments and educational purposes.

<img width="582" height="763" alt="Screenshot 2025-09-26 at 02 11 42" src="https://github.com/user-attachments/assets/5c08130c-1601-412b-ab36-f28e5d8216b7" />


A simple Python-based web security scanner that performs basic vulnerability assessments.

## Features

- Port Scanning: Checks common ports (21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389)

- HTTPS Check: Verifies if the target uses HTTPS

- Admin Panel Discovery: Scans for common admin panel paths

- Sensitive File Detection: Looks for exposed sensitive files

- SQL Injection Testing: Basic SQL injection vulnerability check

- XSS Testing: Basic Cross-Site Scripting vulnerability check

## Installation

### 1. Download the git file
```bash
git clone https://github.com/Richardpandey/Web_Search.git
```

### 2. Move to the Directory
```bash
cd Web_Search
```

### 3. Install dependencies
```bash
pip3 install -r requirements.txt
```

### 4. Run the tool.
```bash
python3 main.py
```
### Enter the target URL when prompted (e.g., http://example.com or https://example.com)

The scanner will automatically run all security checks and display the results.

### Modules

- main.py - Main program orchestrator

- ports.py - Port scanning functionality

- https.py - HTTPS verification

- admin_panels.py - Admin panel discovery

- sensitive_files.py - Sensitive file detection

- sql_injection.py - Basic SQL injection testing

- xss.py - Basic XSS testing

### Disclaimer
This tool is for educational and authorized testing purposes only. Only use on websites you own or have explicit permission to test. Unauthorized scanning may be illegal in your jurisdiction. The author is not responsible for misuse.



