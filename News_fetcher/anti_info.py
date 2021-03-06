import os
import re
import csv
import time
import logging
import requests
import pandas as pd
from bs4 import BeautifulSoup
try:
    from .fetch_each_site import tools
except:
    from fetch_each_site import tools


class anti_info(object):
    path = os.getcwd()
    path = os.path.dirname(path)
    path = os.path.dirname(path)

    input_path = os.path.join(path, 'result\\Anti\\anti_thread.csv')
    save_path = os.path.join(path, 'result\\Anti\\anti_info.csv')

    logging.basicConfig(level=logging.DEBUG)

    def __init__(self):
        self.fetch_data = []
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
            fieldnames = ['category', 'header',
                          'content', 'link', 'image', 'time']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if self.last_link != '':
                writer.writerows(self.fetch_data)
            else:
                writer.writeheader()
                writer.writerows(self.fetch_data)

        logging.info('finished crawling')

    def fetch_page(self):
        urls = []
        self.last_link = self.read_latest_save()

        with open(self.input_path, 'r', encoding='utf-8') as file:
            data = file.readlines()

            for obj in data:
                if obj != '\n':
                    obj = obj.split(',')
                    urls.append(obj[2])

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
        soup = BeautifulSoup(response.text, 'html.parser')

        try:
            header = soup.h1.text.strip()
            header = ' '.join(header.split())
            header = re.sub(',', ' ', header)
        except:
            header = None

        try:
            time = soup.time['datetime'].strip()
            time = tools.time_format(time)
        except:
            time = None

        try:
            category = soup.find_all('div', class_='blog-tag')[0].text.strip()
        except:
            category = None

        try:
            content_blog = soup.find('div', class_='td-post-content')
            content = content_blog.text.strip()
            content = ' '.join(content.split())
        except:
            content = None

        try:
            image_list = soup.select('div.tdb-block-inner p img')
            image = [re.sub('', '', i['src']) for i in image_list]
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
    anti = anti_info()
    anti.fetch_page()
