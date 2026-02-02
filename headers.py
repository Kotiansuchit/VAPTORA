import requests

def headers_check(url, save):
    save("\n[*] Security Headers Check")
    try:
        r = requests.get(url, timeout=5, headers={"User-Agent": "VAPTORA"})
        headers = [
            "X-Frame-Options",
            "Content-Security-Policy",
            "X-Content-Type-Options",
            "Strict-Transport-Security"
        ]
        for h in headers:
            if h in r.headers:
                save(f"[+] {h} present (LOW)")
            else:
                save(f"[-] Missing {h} (MEDIUM)")
    except requests.exceptions.RequestException:
        save("[!] Security headers check skipped due to network/DNS issue (INFO)")

