import scrapy

class face(scrapy.Spider):
    name = 'face'

    start_urls = [
        'https://www.antifakenewscenter.com/%e0%b8%82%e0%b9%88%e0%b8%b2%e0%b8%a7%e0%b8%9b%e0%b8%a5%e0%b8%ad%e0%b8%a1-%e0%b8%ad%e0%b8%a2%e0%b9%88%e0%b8%b2%e0%b9%81%e0%b8%8a%e0%b8%a3%e0%b9%8c-%e0%b8%84%e0%b8%9d-%e0%b8%97%e0%b8%b5%e0%b9%88%e0%b8%96%e0%b8%b9%e0%b8%81%e0%b8%a2%e0%b8%b4%e0%b8%87%e0%b9%80%e0%b8%82%e0%b9%89%e0%b8%b2%e0%b8%a8%e0%b8%a3%e0%b8%b5%e0%b8%a9%e0%b8%b0%e0%b8%9a%e0%b8%a3%e0%b8%b4%e0%b9%80%e0%b8%a7%e0%b8%93%e0%b9%81%e0%b8%9f%e0%b8%a5%e0%b8%95%e0%b8%94%e0%b8%b4%e0%b8%99%e0%b9%81%e0%b8%94%e0%b8%87-%e0%b9%80%e0%b8%9b%e0%b9%87%e0%b8%99%e0%b8%81%e0%b8%b2%e0%b8%a3%e0%b8%a2%e0%b8%b4%e0%b8%87%e0%b8%9e%e0%b8%a5%e0%b8%b2%e0%b8%94%e0%b8%82%e0%b8%ad%e0%b8%87%e0%b8%95%e0%b8%b3%e0%b8%a3%e0%b8%a7%e0%b8%88-%e0%b8%97%e0%b8%b5%e0%b9%88%e0%b8%95%e0%b8%b1%e0%b9%89%e0%b8%87%e0%b9%83%e0%b8%88%e0%b8%88%e0%b8%b0%e0%b8%a2%e0%b8%b4%e0%b8%87%e0%b8%9b%e0%b8%a3%e0%b8%b0%e0%b8%8a%e0%b8%b2%e0%b8%8a%e0%b8%99/'
    ]

    def parse(self, response):
        print(type(response.status))

            
