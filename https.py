import requests

def run(url, log=print):
    log("[*] Checking HTTPS...")

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    try:
        r = requests.get(url, timeout=3)
        if url.startswith("https://"):
            log("[OK] HTTPS is enabled")
        else:
            log("[!] Warning: Target does not use HTTPS")
    except:
        log("[!] Warning: Target does not use HTTPS")

    log("[*] HTTPS Check Completed.\n")
