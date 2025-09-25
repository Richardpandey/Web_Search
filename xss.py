# xss.py
import requests

def run(url, log=print):
    log("[*] Checking XSS...")

    # Ensure URL starts with http:// or https://
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    # Only test if URL has query parameters
    if "?" not in url:
        log("[*] No query parameters to test XSS")
        log("[*] XSS Scan Completed.\n")
        return

    try:
        test_url = url + "?q=<script>alert(1)</script>"
        r = requests.get(test_url, timeout=3)
        if "<script>alert(1)</script>" in r.text:
            log("[!] Possible XSS vulnerability")
        else:
            log("[OK] No obvious XSS found")
    except:
        log("[!] Could not test XSS")

    log("[*] XSS Scan Completed.\n")
