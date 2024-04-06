import requests
from bs4 import BeautifulSoup
import csv
url ='https://resanskrit.com/blogs/blog-post/bhagavad-gita-most-useful-quotes-hindi-english'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

with open('shlokas3.csv', mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Shlok'])
    
    
    response = requests.get(url)

    shlok_elements = soup.find_all('div', class_='shlok')

    for shlok_element in shlok_elements:
        shlok = shlok_element.text.strip()
        writer.writerow([shlok])
       