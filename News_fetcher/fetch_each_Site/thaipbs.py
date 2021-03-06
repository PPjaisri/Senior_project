import re
import logging
from matplotlib.image import thumbnail
import requests
from bs4 import BeautifulSoup
from . import tools


def thaipbs(url, reference):
    logging.debug(f'Crawing at {url}')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    header = soup.find('h1').text.strip()
    header = re.sub(',', ' ', header)

    main = soup.find('article', class_='entry-content')

    content = main.text.strip()
    content = ' '.join(content.split())
    content = re.sub(',', ' ', content)

    images = main.find_all('img')
    images = [image['src'] for image in images]

    time = soup.find('div', class_='content-meta').text.strip()
    time = time.split('|')[1].strip().split()
    time[1] = re.sub(time[1], tools.return_month(time[1]), time[1])
    time = ' '.join(time)
    time = tools.time_format(time)

    data = {
        "category": "ข่าวจริง",
        "header": header,
        "content": content,
        "link": url.strip(),
        "img": images,
        "reference": reference,
        "time": time
    }

    return data
