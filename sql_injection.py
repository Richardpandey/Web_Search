# sql_injection.py
import requests

def run(url, log=print):
    log("[*] Checking SQL Injection...")

    # Ensure URL starts with http:// or https://
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    # Only test if URL has query parameters
    if "?" not in url:
        log("[*] No query parameters to test SQL Injection")
        log("[*] SQL Injection Scan Completed.\n")
        return

    try:
        test_url = url + "' OR '1'='1"
        r = requests.get(test_url, timeout=3)
        if "error" in r.text.lower() or "sql" in r.text.lower():
            log("[!] Possible SQL Injection vulnerability")
        else:
            log("[OK] No obvious SQL Injection found")
    except:
        log("[!] Could not test SQL Injection")

    log("[*] SQL Injection Scan Completed.\n")
