import requests, os

def clickjack_check(url, save, result_dir):
    save("\n[*] Clickjacking Test")
    try:
        r = requests.get(url, timeout=5, headers={"User-Agent": "VAPTORA"})
        if "X-Frame-Options" not in r.headers:
            save("[-] Clickjacking Possible (HIGH)")
            domain = os.path.basename(result_dir)
            poc = os.path.join(result_dir, f"{domain}_clickjacking.html")
            with open(poc, "w") as f:
                f.write(f"<iframe src='{url}' width='800' height='600'></iframe>")
            save(f"[+] PoC saved: {poc}")
        else:
            save("[+] Clickjacking Protection Enabled (LOW)")
    except requests.exceptions.RequestException:
        save("[!] Clickjacking check skipped due to network/DNS issue (INFO)")

