from core.theme import title

def show_menu():
    title("EZIO OPTIONS MENU")
    print("""
[1] Header & Security Scan
[2] JavaScript Endpoint Extraction (domain-only)
[3] Parameter Mining
[4] Auth Context Test
[5] Build Attack Chains
[6] AI Vulnerability Reasoning (from recon)
[7] Full Recon (1–6)
[8] Manual AI Analysis (single endpoint)
[0] Exit
""")
    return [x.strip() for x in input("Select option(s): ").split(",")]
