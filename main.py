import requests
import json
import time
import threading
from colorama import Fore, Back, Style, init

print(Fore.RED + """
           _       _               
  /\   /\ (_) ___ (_)  ___   _ __  
  \ \ / / | |/ __|| | / _ \ | '_ \ 
   \ V /  | |\__ \| || (_) || | | |
    \_/   |_||___/|_| \___/ |_| |_|
             __   __
             \ \ / /
              \ V / 
              / _ \ 
             / / \ \\
             \/   \/
        """)

webhook_url= input("Enter your Webhook: ")

message_1 = input("Enter your Message:")
message_2 = input("Enter your Message 2:")
message_3 = input("Enter your Message 3: ")





messages = [
    message_1,
    message_2,
    message_3
]

def send_message(message_content):
    message = {
        'content': message_content
    }
    payload = json.dumps(message)
    response = requests.post(webhook_url, data=payload, headers={'Content-Type': 'application/json'})
    if response.status_code == 200:
        print(f'Message sent: {message_content}')
    else:
        print(f'|: Made By VisionX: {message_content}')
        print(response.text)
    time.sleep(2)

while True:
    threads = []
    for message_content in messages:
        thread = threading.Thread(target=send_message, args=(message_content,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()