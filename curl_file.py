#crawl the page https://index.minfin.com.ua/ua/russian-invading/casualties/

from urllib.request import Request, urlopen
#url = 'https://index.minfin.com.ua/ua/russian-invading/casualties/'
req = Request(
    url='https://index.minfin.com.ua/ua/russian-invading/casualties/', 
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()
print(webpage)