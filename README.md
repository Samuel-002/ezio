# 🗡️ EZIO

**EZIO** is a **menu-driven, AI-assisted web reconnaissance and analysis tool** built for **bug bounty hunters, penetration testers, and security learners**.

It focuses on **signal over noise** by helping you discover **high-value attack surfaces** and understand **what to test next**, instead of blindly running scanners.

---

## ✨ Features

- ✅ Menu-based interactive CLI (easy to use)
- ✅ Runs as a native command: `ezio`
- ✅ Header & security misconfiguration checks
- ✅ JavaScript endpoint extraction (scope enforced)
- ✅ Parameter mining
- ✅ Auth vs unauth behavior testing
- ✅ Attack chain generation
- ✅ AI-powered vulnerability reasoning (Gemini)
- ✅ Manual AI analysis for single endpoints
- ✅ Automatic JSON & Markdown reports
- ✅ Lightweight (minimal dependencies)

---

## 🚀 Installation

1️⃣ Clone the repository

```bash

git clone https://github.com/Samuel-002/ezio.git
cd ezio

2️⃣ Install dependencies
pip install -r requirements.txt


## 🐍 Virtual Environment (Recommended)

Using a virtual environment is **strongly recommended** to avoid dependency conflicts.

### Create virtual environment
```bash
python -m venv venv

Activate it

Linux / macOS / WSL

source venv/bin/activate


Windows (PowerShell)

venv\Scripts\Activate

Install dependencies

pip install -r requirements.txt


To deactivate:

deactivate



3️⃣ Set Gemini API key

export GEMINI_API_KEY="your_api_key_here"


Windows (PowerShell)

setx GEMINI_API_KEY "your_api_key_here"


Restart the terminal after setting the key.

🧰 Run EZIO as a Command

Linux / macOS / WSL
mv ezio.py ezio
chmod +x ezio
sudo mv ezio /usr/local/bin/


Now you can run EZIO from anywhere:

ezio

🖥️ Usage
Start EZIO
ezio


You will be prompted to:

Enter a target URL

Choose recon/analysis options from the menu

📋 Options Menu
[1] Header & Security Scan
[2] JavaScript Endpoint Extraction (domain-only)
[3] Parameter Mining
[4] Auth Context Test
[5] Build Attack Chains
[6] AI Vulnerability Reasoning (from recon)
[7] Full Recon (1–6)
[8] Manual AI Analysis (single endpoint)
[0] Exit

🔍 Example Workflow
$ ezio

Enter target URL: https://example.com
Select option(s): 7


EZIO will:

Perform full reconnaissance

Extract endpoints and parameters

Build attack chains

Analyze findings with AI

Save results automatically


🤖 AI Analysis (How It Works)

You enter the target URL once

EZIO performs recon automatically

Discovered endpoints and chains are sent to AI


AI explains:

Likely vulnerability classes

Why the endpoint is risky

What to test manually

Manual AI Mode
Select option: 8
Enter endpoint / URL for manual AI analysis:
/api/v1/user/profile?id=FUZZ


🔐 Scope & Safety

Domain-only JavaScript analysis

No brute forcing

No payload exploitation

Analysis-focused and bug bounty safe

Intended only for authorized testing



📌 Requirements

Python 3.9+

Internet access (for AI analysis)

Valid Gemini API key


⚠️ Disclaimer

EZIO is intended only for educational purposes and authorized security testing.

The author is not responsible for misuse of this tool.

Always follow legal guidelines and program scope.

🛠️ Roadmap

Preset modes (ezio recon, ezio ai)

Session save/load

Non-interactive mode

pip installation

Man page (man ezio)

Plugin system

🤝 Contributing

Contributions, ideas, and improvements are welcome.

Please keep contributions:

Ethical

Documented

In-scope

⭐ Final Note

If you use EZIO for:

Bug bounty

Learning

Research

Portfolio projects

Give the repo a ⭐ and build responsibly 🗡️