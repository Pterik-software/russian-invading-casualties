#crawl the page https://index.minfin.com.ua/ua/russian-invading/casualties/
import requests
from urllib.request import urlopen
from lxml import etree

import os
import time
from pprint import pprint


# get html from site and write to local file
#url = 'https://www.starwars.com/news/15-star-wars-quotes-to-use-in-everyday-life';
#headers = {'Content-Type': 'text/html', };
#response = requests.get(url, headers=headers);
#html = response.text;
#with open('star_wars.html', 'w') as f:
#    f.write(html);

# read local html file and set up lxml html parser
#local = 'file:///home/pterik/github/russian-invading-casualties/star_wars.html';
#response = urlopen(local);
#htmlparser = etree.HTMLParser();
#tree = etree.parse(response, htmlparser);

url = 'https://index.minfin.com.ua/ua/russian-invading/casualties/2022-02/'
headers = {'Content-Type': 'text/html', };
response = requests.get(url, headers=headers);
html = response.text;
with open('loss-02-2022.html', 'w') as f:
    f.write(html);
local = 'file:///home/pterik/github/russian-invading-casualties/loss-02-2022.html';
response = urlopen(local);
htmlparser = etree.HTMLParser();
tree = etree.parse(response, htmlparser);
tree.xpath('//li[@class="gold"]')
# <li class='gold'> span class='black'

