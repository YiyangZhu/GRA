import urllib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import time

infile = open("EarningsCast/EarningsLink.txt","r")
outfile = open("EarningsCast/Result.txt","w")
lineCount = 0
with infile as f:
    for line in f:
        #line = "https://earningscast.com/search?utf8=%E2%9C%93&query=KO&commit="
        print("Company link is:",line)
        quote_page = Request(line, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(quote_page)
        soup = BeautifulSoup(page.read(),'html.parser')

        #<h3 class="green">
        #<a href="/KO/20181030">Q3 2018 Coca-Cola Co Earnings Call</a>        
        name_box0 = soup.findAll('h3',attrs={"class","green"})
        print(name_box0)       
        outfile.write(str(name_box0))
        title = name_box0       
        lineCount += 1
        print("line count=",lineCount)
        #<span class="sub">
        #07/25/2018 08:30 AM (EDT)
        #</span>
        name_box = soup.findAll('span',attrs={"class","sub"})
        print(name_box)
        outfile.write(str(name_box))

infile.close()
outfile.close()
'''
name = name_box.text.strip()
print("record time is:",name)
        #<div class="ratingNum">4.0</div>
        #get company overall rating
rating_box = soup.find('div', attrs={"class", "ratingNum"})
print(type(rating_box))
print(rating_box)
if rating_box != None:
    record_time = rating_box.text.strip()
    print("record_time is:",record_time)
'''

