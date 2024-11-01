'''
Real-World Example :: Multithreading for I/O-bound tasks
Scenario : Web Scraping
Web scraping often involves making numerous network requests to fetch web pages. These tasks are I/O-bound because they spend a lot of time waiting for resposes from servers. Multithreading can significantly improve the performance of web scraping tasks by allowing multiple requests to be made concurrently.

'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://python.langchain.com/v0.2/docs/concepts/',
    'https://python.langchain.com/v0.2/docs/tutorials/'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('All web pages fetched successfully')