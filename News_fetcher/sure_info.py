import os
import re
import csv
import time
import logging
import requests
import pandas as pd
from bs4 import BeautifulSoup

class sure_info(object):
    path = os.getcwd()
    path = os.path.dirname(path)
    path = os.path.dirname(path)
    input_path = os.path.join(path, 'result\\Sure\\sure_thread.csv')
    save_path = os.path.join(path, 'result\\Sure\\sure_info.csv')

    logging.basicConfig(level=logging.DEBUG)

    def __init__(self):
        self.fetch_data = []
        self.current_page = 1
        self.finish = False
        self.last_link = ''
        self.count = 0

    def read_latest_save(self):
        try:
            data = pd.read_csv(self.save_path, encoding='utf-8')
            last_link = data.iloc[-1]['link']
            return last_link
        except:
            return ''

    def finished_crawl(self):
        logging.info(f'Crawled {self.count} pages')
        with open(self.save_path, 'a', encoding='utf-8', newline='') as file:
            fieldnames = ['category', 'header', 'content', 'link', 'image', 'time']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if self.last_link != '':
                writer.writerows(self.fetch_data)
            else:
                writer.writeheader()
                writer.writerows(self.fetch_data)

    def fetch_page(self):
        urls = []
        self.last_link = self.read_latest_save()

        with open(self.input_path, 'r', encoding='utf-8') as file:
            data = file.readlines()

            for obj in data:
                if obj != '\n':
                    obj = obj.split(',')
                    urls.append(obj[1])

        new_urls = []
        for url in range(len(urls) - 1, 0, -1):
            new_urls.append(urls[url])

        for url in new_urls:
            if url == self.last_link:
                break
            else:
                self.count += 1
                time.sleep(0.5)
                self.crawl_page(url)

        self.finished_crawl()

    def crawl_page(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        header = soup.h1.text.strip()
        header = re.sub(',', ' ', header)
        time = (soup.find('div', class_='entry-meta')).text
        time = ' '.join(time.split()[:-1])
        time = re.sub(',', ' ', time)
        entry_content = soup.find('div', class_='entry-content')
        
        try:
            category = entry_content.find_all('strong')[1].text
        except:
            category = None
        
        try:
            content_blog = entry_content.select('p')
            content = [(i.text).strip() for i in content_blog]
            content = ' '.join(content)
            content = re.sub(',', ' ', content)
        except:
            content = None

        try:
            image = (soup.find('div', class_='thumb').find('img'))['data-src']
        except:
            image = None

        data = {
            'category': category,
            'header': header,
            'content': content,
            'link': url,
            'image': image,
            'time': time
        }

        self.fetch_data.insert(0, data)

if __name__ == '__main__':
    sure = sure_info()
    sure.fetch_page()