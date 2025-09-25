# main.py
from banner import show_banner
from scan import ports, sql_injection, xss, https, admin_panels, sensitive_files
import sys

def main():
    show_banner()
    
    try:
        target_url = input("Enter target URL (e.g. http://example.com): ").strip()
    except KeyboardInterrupt:
        # Exit silently if Ctrl+C is pressed
        sys.exit(0)

    if not target_url:
        print("No URL entered. Exiting...")
        sys.exit(0)

    print("\n[*] Running all scans...\n")

    ports.run(target_url)
    https.run(target_url)
    admin_panels.run(target_url)
    sensitive_files.run(target_url)
    sql_injection.run(target_url)
    xss.run(target_url)

    print("[*] All Scans Completed.\n")

if __name__ == "__main__":
    main()
