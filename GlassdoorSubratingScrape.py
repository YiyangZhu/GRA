import urllib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import time

file = open("CompanyLinks.txt", "r")
f = open("CompanyNameRatings.txt","w")
theEnd = False
while not theEnd:
    line = file.readline()
    if line != "":
        line = line.strip()
        print("Company link is:",line)
        f.write("Company link is:"+str(line)+"\n")
        quote_page = Request(line, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(quote_page)
        soup = BeautifulSoup(page.read(),'html.parser')
        
        #<p class="h1 strong tightAll" title="" data-company="ABIOMED"> ABIOMED </p>
        #get company name
        name_box = soup.find('p',attrs={"class","h1 strong tightAll"})
        name = name_box.text.strip()
        print("company name is:",name)
        f.write("company name is:"+str(name)+"\n")

        #<div class="ratingNum">4.0</div>
        #get company overall rating
        rating_box = soup.find('div', attrs={"class", "ratingNum"})
        rate = rating_box.text.strip()
        print("Company rating is:",rate)
        f.write("Company rating is:"+str(rate)+"\n")
        indexOfReviews = line.index("Reviews-E")
        indexOfHtm = line.index(".htm")
        id = line[indexOfReviews + 9:indexOfHtm]
                
        #get company subratings
        beginPart = "https://www.glassdoor.com/api/employer/"
        endPart = "-rating.htm?locationStr=&jobTitleStr=&filterCurrentEmployee=false&filterEmploymentStatus=REGULAR&filterEmploymentStatus=PART_TIME"
        subratingPage = beginPart + id + endPart
        quote_page2 = Request(subratingPage, headers={'User-Agent': 'Mozilla/5.0'})
        page2 = urlopen(quote_page2)
        soup2 = BeautifulSoup(page2.read(),'html.parser')
        f.write("Company subrating page is: "+subratingPage+"\n")
        print(soup2.prettify()+"\n")
        f.write(soup2.prettify()+"\n\n")
        
        #let Python rest for 10 seconds
        time.sleep(10)
    else:
        theEnd = True
        
file.close()
f.close()
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