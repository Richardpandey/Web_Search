# sensitive_files.py
import requests

def run(url, log=print):
    log("[*] Checking for Sensitive Files...")

    # Ensure URL starts with http:// or https://
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    files = ["/.env", "/config.php", "/backup.zip", "/db.sql"]
    found = False

    for f in files:
        try:
            r = requests.get(url + f, timeout=3)
            if r.status_code == 200:
                log(f"[!] Found sensitive file: {url}{f}")
                found = True
        except:
            pass

    if not found:
        log("[*] No sensitive files found.")

    log("[*] Sensitive Files Scan Completed.\n")
