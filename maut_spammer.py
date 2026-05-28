#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║            MAUT SPAMMER                         ║
║         Super Simple NGL Tool                   ║
╚══════════════════════════════════════════╝
"""

import requests
import random
import string
import time
import os

R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
W = '\033[0m'
BOLD = '\033[1m'

def gen_did():
    """Generate device ID - standard UUID format"""
    return f"{''.join(random.choices(string.ascii_lowercase+string.digits, k=8))}->

UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gec>
    "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like >
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (>
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, li>
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/12>
]

def header_gen(username):
    """Generate headers for each request"""
    return {
        'accept': '*/*',
        'accept-language': random.choice(['en-US,en;q=0.9', 'en-US,en;q=0.9,fr;q=0>
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://ngl.link',
        'referer': f'https://ngl.link/{username}',
        'sec-ch-ua': random.choice([
            '"Google Chrome";v="125", "Chromium";v="125", "Not-A.Brand";v="99"',
            '"Microsoft Edge";v="125", "Chromium";v="125", "Not-A.Brand";v="99"',
            '"Chromium";v="125", "Not-A.Brand";v="99", "Google Chrome";v="125"',
        ]),
        'sec-ch-ua-mobile': random.choice(['?0', '?1']),
        'sec-ch-ua-platform': random.choice(['"Windows"', '"macOS"', '"Android"', >
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': random.choice(UAS),
        'x-forwarded-for': f"{random.randint(1,255)}.{random.randint(0,255)}.{rand>
        'x-requested-with': 'XMLHttpRequest',
    }

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"""{C}
╔══════════════════════════════════════════╗
║     ███╗   ███╗ █████╗ ██╗   ██╗████████╗║
║     ████╗ ████║██╔══██╗██║   ██║╚══██╔══╝║
║     ██╔████╔██║███████║██║   ██║   ██║   ║
║     ██║╚██╔╝██║██╔══██║██║   ██║   ██║   ║
║     ██║ ╚═╝ ██║██║  ██║╚██████╔╝   ██║   ║
║     ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ║
║              MAUT SPAMMER                 ║
║         Simple & Verbose Edition         ║
╚══════════════════════════════════════════╝{W}
""")

    # ─── Inputs ───
    username = input(f"{C}[?] NGL username: {W}").strip()
    msg = input(f"{C}[?] Message: {W}").strip()

    try:
        count = int(input(f"{C}[?] How many times: {W}").strip())
    except:
        count = 50

    try:
        delay = float(input(f"{C}[?] Delay (0 = fastest): {W}").strip())
    except:
        delay = 0

    # ─── Verify first ───
    print(f"\n{Y}[*] Checking if user exists...{W}")
    try:
        r = requests.get(f"https://ngl.link/{username}", timeout=10, headers={'Use>
        if r.status_code == 200:
            print(f"{G}[✓] User found!{W}")
else:
            print(f"{Y}[!] Status {r.status_code} — might not exist but trying any>
    except Exception as e:
        print(f"{Y}[!] Error checking: {e}{W}")

    # ─── Get initial cookies ───
    print(f"\n{C}[*] Getting session cookie...{W}")
    sess = requests.Session()
    try:
        sess.get('https://ngl.link', timeout=10, headers={'User-Agent': random.cho>
        print(f"{G}[✓] Got session cookie{W}")
    except Exception as e:
        print(f"{Y}[!] Could not get cookie: {e}{W}")

    # ─── Ready ───
    print(f"\n{G}[*] Ready to send {count} messages to {username}{W}")
    input(f"{Y}[*] Press ENTER to start{W}")

    sent = 0
    failed = 0

    # ─── Main loop ───
    while sent < count:
        msg_to_send = msg
        device_id = gen_did()
        headers = header_gen(username)

        data = {
            'username': username,
            'question': msg_to_send,
            'deviceId': device_id,
            'gameSlug': '',
            'referrer': '',
        }

        try:
            r = sess.post('https://ngl.link/api/submit', headers=headers, data=dat>

            send_num = sent + 1

            if r.status_code == 200:
                sent += 1
                print(f"{G}[#{send_num:04d} ✓]{W} Sent! | deviceId: {device_id[:16>
            elif r.status_code == 429:
                failed += 1
                print(f"{Y}[#{send_num:04d} ~]{W} Rate limited (429){W}")
                time.sleep(5)
            elif r.status_code == 403:
                failed += 1
                print(f"{R}[#{send_num:04d} ✗]{W} Forbidden (403) - Session expire>
                # Refresh session
                sess = requests.Session()
                sess.get('https://ngl.link', timeout=10, headers={'User-Agent': ra>
                time.sleep(2)
            elif r.status_code == 400:
                failed += 1
                print(f"{R}[#{send_num:04d} ✗]{W} Bad Request (400) - Response: {r>
            else:
                failed += 1
                print(f"{R}[#{send_num:04d} ✗]{W} Status: {r.status_code} - {r.tex>

            if delay > 0:
                time.sleep(delay)
            else:
                time.sleep(0.01)

        except KeyboardInterrupt:
            print(f"\n{Y}[!] Stopped by user{W}")
            break
        except Exception as e:
            failed += 1
            print(f"{R}[#{sent+failed:04d} !]{W} Error: {e}{W}")
            time.sleep(2)

    print(f"\n{B}{'='*40}")
    print(f"{G}Done!{W}")
    print(f"  Sent:   {G}{sent}{W}")
    print(f"  Failed: {R}{failed}{W}")
    print(f"  Total:  {C}{sent+failed}{W}")
    print(f"{B}{'='*40}")

if __name__ == "__main__":
    main()
    
