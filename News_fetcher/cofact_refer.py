import os
import re
import sys
import csv
import logging
import pandas as pd
try:
    from . import fetch_each_site as site
except:
    import fetch_each_site as site

class cofact_refer(object):
    path = os.getcwd()
    path = os.path.dirname(path)
    path = os.path.dirname(path)
    file_path = os.path.join(path, 'result\\Cofact\\cofact_info_ref.csv')
    save_path = os.path.join(path, 'result\\Cofact\\cofact_refer.csv')

    logging.basicConfig(level=logging.DEBUG)

    def __init__(self):
        self.fetch_data = []
        self.saved_data = []
        self.last_link = ''
        self.count = 0
        self.add = False

    def read_latest_save(self):
        try:
            data = pd.read_csv(self.save_path, encoding='utf-8')
            last_link = data.iloc[-1]['link']
            return last_link
        except:
            return ''

    def finished_crawl(self):
        logging.info(f'Crawled {self.count} pages')
        fieldnames = ['category', 'header',
                      'content', 'link', 'img', 'reference', 'time']

        with open(self.save_path, 'a', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if self.last_link != '':
                writer.writerows(self.fetch_data)
            else:
                writer.writeheader()
                writer.writerows(self.fetch_data)

    def check_domain(self, link):
        # url start at 'https://' or 'http://'
        if len(link.split('//')) > 1:
            domain = link.split('//')[1]
            domain = domain.split('/')[0]
            domain = re.sub('www.', '', domain)
        # url start at 'www.'
        else:
            domain = link.split('/')[0]
            domain = re.sub('www.', '', domain)
        return domain

    def checkDuplicate(self, reference):
        result = False
        try:
            refer_data = self.saved_data['reference'].array
            if reference in refer_data:
                result = True
        except:
            pass
        
        return result

    def fetch_page(self):
        self.last_link = self.read_latest_save()
        try:
            self.saved_data = pd.read_csv(self.save_path, encoding='utf-8')
        except:
            pass
        urls = []
        with open(self.file_path, 'r', encoding='utf-8') as fp:
            data = fp.readlines()

        for data_dict in data:
            urls.append(
                (data_dict.split(',')[-1].strip(), data_dict.split(',')[-2]))

        new_urls = []
        for url in range(len(urls) - 1, 0, -1):
            new_urls.append(urls[url])
            
        for url, ref in new_urls:
            self.count += 1
            try:
                if self.last_link == url.strip():
                    break
                self.crawl_page(url, ref)
            except:
                continue
            
        self.finished_crawl()

    def crawl_page(self, url, reference):
        print(f'Crawing at {url}')
        link = self.check_domain(url)
        isDuplicate = self.checkDuplicate(reference)

        if isDuplicate:
            return

        if link == 'posttoday.com':
            try:
                res = site.postToday(url, reference)
                if res != None:
                    self.fetch_data.insert(0, res)
            except:
                pass
        elif link == 'sanook.com':
            try:
                res = site.sanook(url, reference)
                if res != None:
                    self.fetch_data.insert(0, res)
            except:
                pass
        elif link == 'bbc.com':
            try:
                res = site.bbc(url, reference)
                if res != None:
                    self.fetch_data.insert(0, res)
            except:
                pass
        elif link == 'pptvhd36.com':
            try:
                res = site.pptv(url, reference)
                if res != None:
                    self.fetch_data.insert(0, res)
            except:
                pass
        elif link == 'dailynews.co.th':
            try:
                res = site.dailyNews(url, reference)
                if res != None:
                    self.fetch_data.insert(0, res)
            except:
                pass
        elif link == 'komchadluek.net':
            try:
                res = site.komchadluek(url, reference)
                if res != None:
                    self.fetch_data.insert(0, res)
            except:
                pass
        # elif link == 'oryor.com':
        #     try:
        #         res = site.oryor(url, reference)
        #         if res != None:
        #             self.fetch_data.insert(0, res)
        #     except:
        #         pass
        # elif link == 'sure.oryor.com':
        #     try:
        #         res = site.sureOryor(url, reference)
        #         if res != None:
        #             self.fetch_data.insert(0, res)
        #     except:
        #         pass
        elif link == 'matichon.co.th':
            try:
                res = site.matichon(url, reference)
                if res != None:
                    self.fetch_data.insert(0, res)
            except:
                pass
        elif link == 'thansettakij.com':
            try:
                res = site.thanSettakij(url, reference)
                if res != None:
                    self.fetch_data.insert(0, res)
            except:
                pass
        elif link == 'thairath.co.th':
            try:
                res = site.thairath(url, reference)
                if res != None:
                    self.fetch_data.insert(0, res)
            except:
                pass
        elif link == 'tnnthailand.com':
            try:
                res = site.tnn(url, reference)
                if res != None:
                    self.fetch_data.insert(0, res)
            except:
                pass
        elif link == 'mgronline.com':
            try:
                res = site.mgr(url, reference)
                if res != None:
                    self.fetch_data.insert(0, res)
            except:
                pass
        elif link == 'news.thaipbs.or.th':
            try:
                res = site.thaipbs(url, reference)
                if res != None:
                    self.fetch_data.insert(0, res)
            except:
                pass
        elif link == 'antifakenewscenter.com':
            try:
                res = site.antifakenews(url, reference)
                if res != None:
                    self.fetch_data.insert(0, res)
            except:
                pass
        else:
            return


if __name__ == '__main__':
    cofact = cofact_refer()
    cofact.fetch_page()
