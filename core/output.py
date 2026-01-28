import json
from core.theme import CYAN, PURPLE, RESET

def save_json(data, name="ezio_output.json"):
    with open(name, "w") as f:
        json.dump(data, f, indent=2)

def save_md(data, name="ezio_report.md"):
    with open(name, "w") as f:
        for k, v in data.items():
            f.write(f"## {k}\n{v}\n\n")

def print_cli_report(data, target):
    print(f"\n{CYAN}===== EZIO REPORT ====={RESET}")
    print(f"Target: {target}\n")

    for k, v in data.items():
        print(f"{PURPLE}[{k.upper()}]{RESET}")
        if isinstance(v, list):
            for i in v:
                print(f" - {i}")
        elif isinstance(v, dict):
            for a, b in v.items():
                print(f"{a}: {b}")
        else:
            print(v)
        print()
