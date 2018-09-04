import urllib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


file = open("CompanyLinks.txt", "r")

theEnd = False
while not theEnd:
    line = file.readline()
    if line != "":
        line = line.strip()
        print("Company link is:",line)
        quote_page = Request(line, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(quote_page)
        soup = BeautifulSoup(page.read(),'html.parser')
        #print(soup.prettify())
        
        #<p class="h1 strong tightAll" title="" data-company="ABIOMED"> ABIOMED </p>
        name_box = soup.find('p',attrs={"class","h1 strong tightAll"})
        #print("name box:",name_box)
        name = name_box.text.strip()
        print("company name is:",name)

        #<div class="ratingNum">4.0</div>
        rating_box = soup.find('div', attrs={"class", "ratingNum"})
        #print("rating box:",rating_box)
        rate = rating_box.text.strip()
        print("Company rating is:", rate)
        print()       
    else:
        theEnd = True
file.close()
'''
quote_page = Request('https://www.glassdoor.com/Overview/Working-at-Apple-EI_IE1138.11,16.htm', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(quote_page)
soup = BeautifulSoup(page.read(),'html.parser')
print(soup.prettify())

#<div class="ratingNum">4.0</div>
rating_box = soup.find('div', attrs={"class", "ratingNum"})
print("rating box:", rating_box)
rate = rating_box.text.strip()
print("Company rating is:", rate)
'''

'''
i.e.  <div class="basic-quote"> → 
<div class="price-container up"> → <div class="price">.

price_box = soup.find(‘div’, attrs={‘class’:’price’})
price = price_box.text
print price


<span class="priceText__1853e8a5">2,874.69</span>

<a href="/questions/16627227/http-error-403-in-python-3-web-scraping" class="question-hyperlink">HTTP error 403 in Python 3 Web Scraping</a>

'''
