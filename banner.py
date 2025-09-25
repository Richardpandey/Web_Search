# banner.py
import pyfiglet
from termcolor import colored

def show_banner():
    # Pick a clean, readable font
    banner = pyfiglet.figlet_format("Web Search", font="jazmine")
    print(colored(banner, "green"))

    print(colored("🔹 A Full Website + Port Scanner", "cyan"))
    print()
    print(colored("👤 Author: Richard | GitHub: Richardpandey", "green"))
    print()
    print(colored(" Version: 1.0", "green"))
    print()
    print(colored("------------------------------------------------------------\n", "white"))
