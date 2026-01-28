import os
from core.theme import BOLD, RESET, YELLOW

def show_banner():
    os.system("clear" if os.name != "nt" else "cls")

    print(f"""{BOLD}{YELLOW}
████████████████████████████████████████████████
█                                              █
█   ███████╗███████╗██╗ ██████╗               █
█   ██╔════╝╚══███╔╝██║██╔═══██╗              █
█   █████╗    ███╔╝ ██║██║   ██║              █
█   ██╔══╝   ███╔╝  ██║██║   ██║              █
█   ███████╗███████╗██║╚██████╔╝              █
█   ╚══════╝╚══════╝╚═╝ ╚═════╝               █
█                                              █
█        MENU-DRIVEN WEB RECON & AI TOOL        █
█                                              █
████████████████████████████████████████████████
{RESET}""")
