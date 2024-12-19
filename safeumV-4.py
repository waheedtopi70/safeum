import requests
import random
import json
import sys
import time
import os
from gzip import decompress
from random import choice, choices
from concurrent.futures import ThreadPoolExecutor
from websocket import create_connection
from ssl import CERT_NONE
try:
    from licensing.models import *
    from licensing.methods import Key, Helpers
except:
    os.system('pip install licensing')

RSAPubKey = "<RSAKeyValue><Modulus>wt6jgQrioMrme/T6wKvWuyJM9eqn3RsNvdYgRbM/kQ6s8dTkq+3cKDuhoWLUHudmIb4TPnlMdtW7HqthYO5HDS11ejRbMUqkfBDvB4cJNA7rtyuRjnVMZRoptM3/FvmrZDFwFcjRZIJIgBbGVmMTe8ZMM8NjpTWULa2aoIuS5dOSwLlNuF3QRS6L7T9Yq8k1DYHbNqRlPypd0M8H6HyxdY3m4v2pv5Oj0eoTs6pbVBxJKinXivWT3RU/dUA4dD9vUWmP9IAwSYV8wvGrbc8mVlGEsmGZzjAw9P8j4F4FqeHF6wcW+Emuvvtw552QMnHUnW7im3VC9SyAcYwWsh3bPQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"# ENTER RSAKEY
auth = "WyI5ODQwNDAwMSIsIkxxTnkxdjFNc2FubENuMXZwcFZjS2pYbm5tNmZ5bjI1SWJUcmZWd3UiXQ=="  # AUTHKEY WITH ACTIVATE!
def Authkey():
    key ='GDHUU-ZGQJL-ZVCZN-NBKHL'
    result = Key.activate(token=auth,\
        rsa_pub_key=RSAPubKey,\
        product_id='28127', \
        key=key,\
        machine_code=Helpers.GetMachineCode())

    if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
    # an error occurred or the key is invalid or it cannot be activated
    # (eg. the limit of activated devices was achieved)
        print("'\033[0;31m\033[1;47m  The tool is disabled. Contact @AA8DQ to activate it  \033[0m'".format(result[1]))
        exit()
    else:
     #everything went fine if we are here!
        print('''\033[0;30m\033[1;42m Activated VIP ✅️\033[0m''''\n' )
        pass
Authkey()

L = '\033[1;33m'
C = "\033[1;97m"
Y = '\033[1;34m'
G = '\033[1;32m'
R = '\033[1;31m'
reset = "\033[0m"


failed = 0
success = 0
retry = 0
processed = 0  
total_tasks = 0  
accounts = []


def get_telegram_info():
    bot_token = input(" \033[0;30m\033[1;47m● أدخل توكن بوتك : \033[0m\n\n")
    chat_id = input(" \033[0;30m\033[1;47m ● ادخل الأيدي الخاص بك :\033[0m \n\n")
    return bot_token, chat_id

TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID = get_telegram_info()


def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print(f"Error sending message to Telegram: {response.text}")
    except Exception as e:
        print(f"Telegram send error: {e}")


def work(rate_limit=None, user_input=None):
    global failed, success, retry, processed

  
    if processed >= total_tasks:  
        return

    # إنشاء اسم مستخدم عشوائي
    username = (user_input if user_input else choice('qwertyuioplkjhgfdsazxcvbnm')) + ''.join(choices('qwertyuioplkjhgfdsazxcvbnm1234567890', k=13))

    headers = {
        "app": "com.safeum.android",
        "host": None,
        "remoteIp": "134.209.93.148",
        "remotePort": str(8080),
        "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195",
        "time": "2023-04-30 12:13:32",
        "url": "wss://51.79.208.190/Auth"
    }

    data0 = {
        "action": "Register",
        "subaction": "Desktop",
        "locale": "ar_EG",
        "gmt": "+03",
        "password": {
            "m1x": "ca06a3ac0f6472133f552618a1b7a4c48a379ce121379f959241c4ec8b2a0b7d",
            "m1y": "cb9803745d0b13a2716af440d7ab12e33e480eee42a865eae82bd9319e7ab371",
            "m2": "f5bf646c275b778e6e25811c9ba4dea23d00ae50b22c3e845fd3c7093a6fccb1",
            "iv": "53f31e7f0d7b78325d2219b728bca3c3",
            "message": "162c47c5b4a2632aa81da79bd95564680e4f136769da04cbaad4e9c466180a316723eaa46d6cc4c3ad6376e5387314dc6cb8606c585b38631ae2af10013ed692d2aeee889a0b8121e943bd00577cd33a"
        },
        "magicword": {
            "m1x": "212d24f6b16857856621c3d1dd9eca41e6b28627e3c637f6470a14cd422536f8",
            "m1y": "389e8a7538763ae1a115f752293fde8421d7bb3b27ba5fa592aa839927097490",
            "m2": "4b8d8c1cd062460659bebb1545d25b68459584cf906760d248c3cfd19b862239",
            "iv": "bacf4b6a0ca75c6d28cd771ceef636c5",
            "message": "4ff4cf3137e8224a8ea7cac54e97bdbe"
        },
        "magicwordhint": "0000",
        "login": str(username),
        "devicename": "Xiaomi 21061110AG",
        "softwareversion": "1.1.0.1640",
        "nickname": "telegramsandavex",
        "os": "AND",
        "deviceuid": "8cd7ef3808db0e2b",
        "devicepushuid": "*f1daDAunSnKvOEe8NlbvXZ:APA91bF7OG_YNopCXey89iuOBgTmXC1KZGBvfbk-XKOc8BrlTeWb78udkLpI3__t90CK46kgZy7RC_pPwfBfLs7p_T6qloho3PTJGXwOepDaxXpaQtNeGlA",
        "osversion": "and_13.0.0",
        "id": "722263729"
    }

    try:
        
        ws = create_connection("wss://51.79.208.190/Auth", header=headers, sslopt={"cert_reqs": CERT_NONE})
        ws.send(json.dumps(data0))
        result = ws.recv()

      
        if isinstance(result, str):
            result = result.encode()
        decoded_data = decompress(result).decode('utf-8')

       
        if '"comment":"Exists"' in decoded_data:
            failed += 1
        elif '"status":"Success"' in decoded_data:
            success += 1
            account = f"{username}:aa8dq"
            accounts.append(account)
            with open('@AA8DQ.txt', 'a') as f:
                f.write(f"{account} | TG : @sandaveX\n")
            send_telegram_message(f"✅️ حساب ناجح : @AA8DQ {account}")
        elif '"comment":"Retry"' in decoded_data:
            retry += 1
        processed += 1

    except Exception as e:
        retry += 1
        processed += 1


def validate_input():
    while True:
        print("\033[0;34m\033[1;47m ★ ادخل عدد الحسابات التي تريد فحصها من : (1 إلى 5000):\033[0m")
        try:
            total_tasks = int(input("\033[1;37m>>> \033[0m"))
            if 1 <= total_tasks <= 5000:
                return total_tasks
            else:
                print("\033[0;37m\033[1;41m⚠️ لا تدخل رقم اكبر من 5000 .\033[0m\n")
        except ValueError:
            print("\033[0;37m\033[1;41m⚠️ اختيار خاطئ حط رقم مثلا : ( 400 او 1200 الى 5000 )\033[0m\n")


def main():
    global processed, total_tasks
    total_tasks = validate_input()
    
    executor = ThreadPoolExecutor(max_workers=1000)
    while processed < total_tasks:
        executor.submit(work)
        os.system('cls' if os.name == 'nt' else 'clear')
        progress = (processed / total_tasks) * 100
        completed_length = int(progress // 2)
        remaining_length = 50 - completed_length

        bar = f"[{G}{'▓' * completed_length}{R}{'▒' * remaining_length}{reset}]"
        print('''\033[0;34m\033[1;40m▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▒░░▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒░░▒▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▒░▒▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▒░░▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▒░▒▓▓▓▓▓▒░░░░░▒▒▓▓▓▓▓▒▒░░░░░▓▓▓▓▓▓░░▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▒░▒▓▓▓▓▓▒░░░░▒▓▓▓▒▒▓▓▓▓░░░░░▓▓▓▓▓▓░░▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▒░▒▓▓▓▓▓▒▒▒▒▒▓▓▓▓░░▒▓▓▓▓▒▒▒▒▓▓▒▒▓▓░░▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▒░▒▓▓▓▒░▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓░░▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▒░▒▓▓▓░▒░░░░░░░░▒▓▓▓░░░░░░░░▒░▓▓▓▓░░▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▒░▒▓▓▓░▒░░░░░░░░▒▓▓▒░░░░░░░░▒░▓▓▓▒░░▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▒░▒▓▓▓▒▒░░░░░░░░▒▓▓▒░░░░░░░░▒░▓▓▓▒░░▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▒░▒▓▓▓▒▒░░░░░░░░▒▓▓▒░░░░░░░░▒░▓▓▓▓░░▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▒░▒▓▓▓▒▒░░░░░░░░▒▓▓░░░░░░░░░▒░▓▓▓▒░░▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▒░▒▓▓▓▒▒░░░░░░░░░▒▓▒░░░░░░░░▒░▓▓▓▓░░▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▒░▒▓▓▓▒▒▒░░░░░░░░░▒░░░░░▒░░░▒░▓▓▓▓░░▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▒░▒▓▓▓▓▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒░▒▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓░░▒▓▓▓▓▓▓▓░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▒░░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░░▒▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n\033[0m''')
        print(f"\033[0;37m\033[1;42mصحيح✅️:\033[0m {G}{success}{reset}, \033[0;37m\033[1;41mخطأ ❌️: \033[0m{R}{failed}{reset}, \033[0;37m\033[1;44m الفحص ♻️\033[0m {Y}{retry}{reset}\n")
        print(f"{bar} {progress:.2f}%\n")
        print('\033[1;36m@AA8DQ | @sandaveX | @aayco\033[0m\n')
        
        for account in accounts:
            print(f"{G}{account}{reset}")

        time.sleep(0.1)

    print(f"\033[1;32mتم فحص {total_tasks} حساب بنجاح عد مرة اخرى👏🌸...\033[0m")

if __name__ == "__main__":
    main()
