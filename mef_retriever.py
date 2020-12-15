#!/usr/bin/python3
import requests
import os
import re
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url = 'https://home.army.mil/bragg/index.php/www-wx'



res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')


title = soup.title.text
body = soup.body
head = soup.head

links = soup.select('a')
# [4].text

full_html_of_link = ''

for i in links:
    if 'MEF' in i.text:
        full_html_of_link = i
        break

print(full_html_of_link)


full_html_of_link = str(full_html_of_link)


just_url = ''
just_url = re.findall(r'"([^"]*)"', full_html_of_link)
just_url = str(just_url)

just_url = just_url[2:len(just_url)-2]
print("just   ", just_url)


file_name = ''

os.system("pkill okular")
#os.system("rm weathermap")

cmd = "wget " + just_url + " -O weathermap"
os.system(cmd)


os.system("okular weathermap --presentation")
