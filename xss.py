import requests, os

PAYLOAD_FILE = os.path.join("payloads", "xss_payloads.txt")
MAX_PAYLOADS = 10

def xss_check(url, save):
    save("\n[*] Reflected XSS Test")

    try:
        with open(PAYLOAD_FILE) as f:
            payloads = [p.strip() for p in f if p.strip()][:MAX_PAYLOADS]
    except FileNotFoundError:
        save("[!] XSS payload file not found (INFO)")
        return

    for p in payloads:
        try:
            r = requests.get(url, params={"q": p}, timeout=5,
                             headers={"User-Agent": "VAPTORA"})
            if p in r.text:
                save("[-] Possible Reflected XSS detected (HIGH)")
                save(f"[!] Payload: {p}")
                return
        except requests.exceptions.RequestException:
            save("[!] XSS check skipped due to network/DNS issue (INFO)")
            return

    save("[+] No reflected XSS detected with tested payloads (LOW)")

