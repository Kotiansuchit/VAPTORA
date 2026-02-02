import os
import argparse
from urllib.parse import urlparse

from banner import grab_banner
from headers import headers_check
from clickjack import clickjack_check
from methods import methods_check
from xss import xss_check

# -----------------------------
# Result storage
# -----------------------------
results = []

def save(msg):
    results.append(msg)
    print(msg)

# -----------------------------
# Argument parser (HELP)
# -----------------------------
parser = argparse.ArgumentParser(
    description="VAPTORA - Mini Web VAPT Toolkit",
    epilog="""
Examples:
  python vaptora.py https://example.com

Checks Performed:
  - Banner Grabbing
  - Security Headers Analysis
  - Clickjacking Detection
  - HTTP Methods Check
  - Reflected XSS Test

Disclaimer:
  Use this tool only on applications you own or have permission to test.
""",
    formatter_class=argparse.RawTextHelpFormatter
)

parser.add_argument(
    "url",
    help="Target URL (include http:// or https://)"
)

args = parser.parse_args()
url = args.url.strip()

# -----------------------------
# Extract domain
# -----------------------------
parsed = urlparse(url)
domain = parsed.netloc.replace("www.", "")

if not domain:
    print("[-] Invalid URL format")
    exit(1)

# -----------------------------
# Create Results/domain/
# -----------------------------
result_dir = os.path.join("Results", domain)
os.makedirs(result_dir, exist_ok=True)

result_file = os.path.join(result_dir, "vaptora_results.txt")

# -----------------------------
# ASCII Banner
# -----------------------------
print(r"""
██╗   ██╗ █████╗ ██████╗ ████████╗ ██████╗ ██████╗  █████╗
██║   ██║██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗██╔══██╗
██║   ██║███████║██████╔╝   ██║   ██║   ██║██████╔╝███████║
╚██╗ ██╔╝██╔══██║██╔═══╝    ██║   ██║   ██║██╔══██╗██╔══██║
 ╚████╔╝ ██║  ██║██║        ██║   ╚██████╔╝██║  ██║██║  ██║
  ╚═══╝  ╚═╝  ╚═╝╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
        VAPTORA - Mini Web VAPT Toolkit
""")

print(f"[+] Target: {url}")
print(f"[+] Results Directory: {result_dir}\n")

# -----------------------------
# Run checks
# -----------------------------
total = 5
done = 0

grab_banner(url, save);                     done += 1
headers_check(url, save);                  done += 1
clickjack_check(url, save, result_dir);    done += 1
methods_check(url, save);                  done += 1
xss_check(url, save);                      done += 1

# -----------------------------
# Save results
# -----------------------------
with open(result_file, "w") as f:
    f.write("\n".join(results))

percentage = int((done / total) * 100)

print("\n" + "-" * 45)
print(f"[✔] Scan Completed: {percentage}%")
print(f"[✔] Results saved to: {result_file}")
print("-" * 45)
