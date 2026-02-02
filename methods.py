import requests

def methods_check(url, save):
    save("\n[*] HTTP Methods Check")

    try:
        r = requests.options(url, timeout=5, headers={"User-Agent": "VAPTORA"})
        methods = r.headers.get("Allow")

        if methods:
            save(f"[INFO] Allowed Methods: {methods} (LOW)")
            if "PUT" in methods or "DELETE" in methods:
                save("[-] Dangerous HTTP Methods Enabled (HIGH)")
        else:
            save("[INFO] Server does not disclose HTTP methods (INFO)")

    except requests.exceptions.RequestException:
        save("[!] HTTP Methods check blocked or restricted by server (INFO)")

