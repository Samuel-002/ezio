RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
GRAY = "\033[90m"

def title(msg):
    print(f"\n{BOLD}{CYAN}=== {msg} ==={RESET}")

def info(msg):
    print(f"{GREEN}[+]{RESET} {msg}")

def warn(msg):
    print(f"{YELLOW}[!]{RESET} {msg}")

def error(msg):
    print(f"{RED}[x]{RESET} {msg}")

def success(msg):
    print(f"{BOLD}{GREEN}[✓]{RESET} {msg}")
