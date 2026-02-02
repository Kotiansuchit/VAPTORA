import requests

def grab_banner(url, save):
    save("\n[*] Banner Grabbing")

    try:
        r = requests.head(url, timeout=5, headers={"User-Agent": "VAPTORA"})
        server = r.headers.get("Server")
        if server:
            save(f"[INFO] Server Banner (HEAD): {server} (LOW)")
            return
    except:
        pass

    try:
        r = requests.get(url, timeout=5, headers={"User-Agent": "VAPTORA"})
        server = r.headers.get("Server")
        if server:
            save(f"[INFO] Server Banner (GET): {server} (LOW)")
            return
    except:
        pass

    save("[!] Server banner not disclosed by server (INFO)")

