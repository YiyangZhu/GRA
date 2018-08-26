import urllib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

quote_page = Request('https://www.glassdoor.com/Overview/Working-at-Apple-EI_IE1138.11,16.htm', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(quote_page)
soup = BeautifulSoup(page.read(),'html.parser')
print(soup.prettify())

name_box = soup.find('div', attrs={"class", "ratingNum"})
print(name_box)
print("namebox", name_box)
name = name_box.text.strip()
print("name", name)
'''
i.e.  <div class="basic-quote"> → 
<div class="price-container up"> → <div class="price">.

price_box = soup.find(‘div’, attrs={‘class’:’price’})
price = price_box.text
print price


<span class="priceText__1853e8a5">2,874.69</span>

<a href="/questions/16627227/http-error-403-in-python-3-web-scraping" class="question-hyperlink">HTTP error 403 in Python 3 Web Scraping</a>


<div class="ratingNum">4.0</div>

'''
