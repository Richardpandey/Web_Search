# admin_panels.py
import requests

def run(url, log=print):
    log("[*] Checking for Admin Panels...")

    # Ensure URL starts with http:// or https://
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    panels = ["/admin", "/login", "/administrator", "/wp-admin"]
    found = False
    for panel in panels:
        try:
            r = requests.get(url + panel, timeout=3)
            if r.status_code == 200:
                log(f"[!] Found admin panel: {url}{panel}")
                found = True
        except:
            pass

    if not found:
        log("[*] No common admin panels found.")

    log("[*] Admin Panel Check Completed.\n")
