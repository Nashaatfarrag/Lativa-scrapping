import requests
from bs4 import BeautifulSoup
import json

from datetime import datetime
start=datetime.now()

#Statements


result = requests.get("https://www.ss.com/lv/real-estate/")
print(result.status_code)
rc = result.content
# print(rc)
soup = BeautifulSoup(rc,"html.parser")
# print(soup)
links = soup.find_all("a" , class_="a_category")
# print(links)
output = []
def fixDomain(subdomain):
    return "https://www.ss.com" + subdomain

i = 0
def handelFinalAds(link,item):
    Page = requests.get(link)
    soupfinal = BeautifulSoup(Page.content,"lxml")
    ads_lins =  soupfinal.find_all("a" , class_="am")
    print(len(ads_lins))
    for ad_link in ads_lins :
        finalAd = requests.get(fixDomain(ad_link.attrs['href']))
        soup2 = BeautifulSoup(finalAd.content,"lxml")
        # item["ad_description"] = soup2.find("div", { "id" : "msg_div_msg" }).text
        item["price"] = ( soup2.find("td" , class_="ads_price").text if soup2.find("td" , class_="ads_price") else  0 )
        output.append(item)
            # print(soup2.find("div", { "id" : "msg_div_msg" }).text)
            # file = open(ad_link.,"w")
            # file.write(finalAd.content)
            # file.close()

    next_page_link = soupfinal.find("a", {"rel" : "next"})
    if(next_page_link):
        myLink = fixDomain(next_page_link.attrs['href'])
        print(myLink)
        if(myLink[-1] == 'l'):
            handelFinalAds(myLink,item)

category = ["main_cat" , "second_cat" , "third_cat" , "forth_cat"]
def handleCategories(myLinks):
    for link in myLinks[15:17]:
        print( "category : " + link.text)
        item = dict({})
        nextPage = requests.get(fixDomain(link.attrs['href']))
        soup1 = BeautifulSoup(nextPage.content,"lxml")
        links1 = soup1.find_all("a" , class_="a_category")
        if(len(links1) == 0):

            handelFinalAds(fixDomain(link.attrs['href']),item)
        else:
            handleCategories(links1)


handleCategories(links)
    # for i in links1 :
    #     print(i.text)

    # print(link.href)
    # print(result1.status_code)

with open('hi.json', 'w' ,encoding='ascii') as fout:
    json.dump(output , fout)

print( (datetime.now()-start ))
print(len(output))
print( (datetime.now()-start ) / len(output))
# with open('hi.json',encoding='ascii') as f:
#         data = json.load(f)
# print(data)
# result = requests.get("https://www.whitehouse.gov/briefings-statements/")
# print(result.status_code)
# rc = result.content
# # print(rc)
# soup = BeautifulSoup(rc,"html.parser")
# print(soup.a.attrs)
# # urls = []
# # for h2_tag in soup.find_all("h2" ):
# #     a_tag = h2_tag.find("a")
# #     print(a_tag.text)
# #     urls.append(a_tag.attrs["href"])

# # print(links)


