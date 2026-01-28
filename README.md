# 🗡️ EZIO

**EZIO** is a **menu-driven, AI-assisted web reconnaissance and analysis CLI tool** built for **bug bounty hunters, penetration testers, and security learners**.

It focuses on **signal over noise** by combining **automated recon**, **attack-chain building**, and **AI-driven reasoning**, while keeping everything **human-readable directly in the terminal**.

---

## ✨ Key Features

- ✅ Interactive **menu-driven CLI**
- ✅ **Orange ASCII banner** with colorful terminal UI
- ✅ Runs as a native command: `ezio`
- ✅ Header & security misconfiguration checks
- ✅ JavaScript endpoint extraction (scope-aware)
- ✅ Parameter mining
- ✅ Auth vs unauth response comparison
- ✅ Attack chain generation
- ✅ AI-powered vulnerability reasoning (Gemini)
- ✅ Manual AI analysis mode
- ✅ **CLI report output** (no need to open files)
- ✅ JSON & Markdown reports for documentation
- ✅ SSL-safe requests (handles broken certificates)
- ✅ No heavy dependencies (no colorama)

---

## 🚀 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Samuel-002/ezio.git
cd ezio

🐍 Virtual Environment (Recommended)

Using a virtual environment helps avoid dependency conflicts.

Create venv
python3 -m venv venv

Activate venv

Linux / macOS / Kali

source venv/bin/activate


Windows (PowerShell)

venv\Scripts\Activate

Install dependencies
pip install -r requirements.txt


To deactivate:

deactivate


🔐 AI Setup (Required for AI Features)

EZIO uses Google Gemini for vulnerability reasoning.

Linux / macOS / Kali
export GEMINI_API_KEY="your_api_key_here"

Windows (PowerShell)
setx GEMINI_API_KEY "your_api_key_here"


Restart your terminal after setting the key.

🧰 Running EZIO
Local (development)
python3 ezio.py

System-wide (Linux / Kali)
chmod +x ezio
sudo mv ezio /usr/local/bin/


Then run from anywhere:

ezio

📋 Options Menu
[1] Header & Security Scan
[2] JavaScript Endpoint Extraction
[3] Parameter Mining
[4] Auth Context Test
[5] Build Attack Chains
[6] AI Vulnerability Reasoning

[7] Full Recon (1–6)
[8] Manual AI Analysis
[0] Exit


Menu and status output are bold and color-coded for clarity.

🔍 Example Workflow
$ ezio

Enter target URL: https://example.com
Select option(s): 7


EZIO will:

Perform full reconnaissance

Build attack chains

Analyze findings with AI

Print a full report in the CLI

Save JSON & Markdown reports


📊 CLI Report Output

After execution, EZIO prints a structured report directly in the terminal:

Headers & missing security controls

Discovered endpoints

Parameters

Attack chains

AI reasoning & manual test suggestions

No need to open files unless you want to.


📁 Output Files

EZIO automatically generates:

📄 ezio_output.json — structured, machine-readable

📄 ezio_report.md — human-readable report

Useful for:

Bug bounty submissions

Notes & documentation

Automation workflows


🔐 Scope & Safety

Domain-only JavaScript analysis

No brute-force attacks

No payload exploitation

Designed for authorized testing only

SSL errors are handled gracefully (no crashes)


🧠 Philosophy

EZIO is built around:

Logic flaws over payload spam

Human-style attack thinking

AI-assisted decision support

Clean, explainable output

It does not replace skill — it amplifies it.


📌 Requirements

Python 3.9+

Internet connection (for AI)

Valid Gemini API key


⚠️ Disclaimer

EZIO is intended only for educational purposes and authorized security testing.

The author is not responsible for misuse.

Always follow legal guidelines and program scope.


🛠️ Roadmap

--no-color / --no-banner

Animated intro

Severity scoring

HTML report export

pip installation

Plugin system


🤝 Contributing

Contributions are welcome.

Please keep all contributions:

Ethical

Documented

In scope


⭐ Final Note

If you use EZIO for:

Bug bounty

Learning

Research

Portfolio projects

Give the repo a ⭐ and hack responsibly 🗡️