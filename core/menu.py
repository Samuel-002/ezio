from core.theme import BOLD, GREEN, CYAN, YELLOW, RED, RESET, title

def show_menu():
    title("EZIO OPTIONS MENU")

    print(f"""
{BOLD}{GREEN}[1]{RESET} Header & Security Scan
{BOLD}{GREEN}[2]{RESET} JavaScript Endpoint Extraction
{BOLD}{GREEN}[3]{RESET} Parameter Mining
{BOLD}{GREEN}[4]{RESET} Auth Context Test
{BOLD}{GREEN}[5]{RESET} Build Attack Chains
{BOLD}{GREEN}[6]{RESET} AI Vulnerability Reasoning

{BOLD}{CYAN}[7]{RESET} Full Recon (1–6)
{BOLD}{YELLOW}[8]{RESET} Manual AI Analysis
{BOLD}{RED}[0]{RESET} Exit
""")

    return [x.strip() for x in input(f"{BOLD}Select option(s): {RESET}").split(",")]
