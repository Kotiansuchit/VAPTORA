🛡️ VAPTORA – Mini Web VAPT Toolkit

VAPTORA is a lightweight, Python-based Web Vulnerability Assessment & Penetration Testing (VAPT) assistant designed for initial security assessment of web applications.

It automates common reconnaissance and misconfiguration checks while maintaining ethical behavior, stability, and clear result organization.

🚀 Features

VAPTORA performs the following checks:

Banner Grabbing

Identifies server banner when disclosed

Security Headers Analysis

Checks for missing HTTP security headers

Clickjacking Detection

Detects absence of frame protection

Generates an iframe-based Proof of Concept (PoC)

HTTP Methods Check

Attempts to identify allowed HTTP methods

Reflected XSS Testing

Uses a small curated payload list

Detects unsafe reflection without exploitation

📁 Project Structure
vaptora/
│
├── vaptora.py
├── banner.py
├── headers.py
├── clickjack.py
├── methods.py
├── xss.py
│
├── payloads/
│   └── xss_payloads.txt
│
└── Results/
    └── example.com/
        ├── vaptora_results.txt
        └── example.com_clickjacking.html

🧰 Requirements

Python 3.x

requests library

Install dependency:

pip install requests

▶️ Usage

Run the tool with a target URL:

python vaptora.py https://example.com


Help menu:

python vaptora.py --help

📊 Output Handling

All scan results are stored under a single Results/ directory

Each target gets its own folder

Proof-of-Concept files (e.g., clickjacking) are saved alongside scan results

Example:

Results/testphp.vulnweb.com/
├── vaptora_results.txt
└── testphp.vulnweb.com_clickjacking.html

🎯 Project Objective

This project demonstrates:

Understanding of common web vulnerabilities

Safe automation of security checks

Proper error handling for real-world environments

Professional result organization

Ethical approach to vulnerability testing

👨‍💻 Author

Suchit Kotian
