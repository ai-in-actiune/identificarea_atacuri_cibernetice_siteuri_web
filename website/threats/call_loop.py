import requests 
import time

urls = [
    'http://127.0.0.1:5000',
    'http://127.0.0.1:5000/login',
    'http://127.0.0.1:5000/sign-up'
]


while True:
    for url in urls:
        response = requests.get(url)
        print(f"Accessed {url}, status code:{response.status_code}")
        time.sleep(2) # 2 sec pause between requests