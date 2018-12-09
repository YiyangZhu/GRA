import urllib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import time

line = "https://www.glassdoor.com/Reviews/Agree-Realty-Corporation-Reviews-E2645.htm"
print("Company link is:",line)
quote_page = Request(line, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(quote_page)
soup = BeautifulSoup(page.read(),'html.parser')
        
        #<p class="h1 strong tightAll" title="" data-company="ABIOMED"> ABIOMED </p>
        #get company name
name_box = soup.find('p',attrs={"class","h1 strong tightAll"})
name = name_box.text.strip()
print("company name is:",name)
        #<div class="ratingNum">4.0</div>
        #get company overall rating
rating_box = soup.find('div', attrs={"class", "ratingNum"})
print(type(rating_box))
print(rating_box)
if rating_box != None:
    rate = rating_box.text.strip()
    print("Company rating is:",rate)