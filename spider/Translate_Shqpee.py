# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 09:50:36 2020

@author: OSA
"""
import requests
from bs4 import BeautifulSoup
re=requests.get("https://phabricator.wikimedia.org/source/mediawiki/browse/master/languages/data/ZhConversion.php")
re.encoding='UTF-8'
#print(re)
bu=BeautifulSoup(re.text,'html.parser')
val=bu.select(".phabricator-source-code")
Target=[]
Value=[]
reverse=False
for x in range(len(val)):
    try:
        if( (val[x].text)   .index("=>")>0 and reverse==False ):
            X=str(val[x].text.replace("'","").replace("=>","").replace(",",""))
            value,target=(X.split())     
            Target.append(target)
            Value.append(value)
        elif((val[x].text)   .index("=>")>0 and reverse==True):
            X=str(val[x].text.replace("'","").replace("=>","").replace(",",""))
            target,value=(X.split())     
            Target.append(target)
            Value.append(value)
            
    except ValueError:
            if(x>100):
                reverse=True
#%%
import json
re=requests.Session()
re.encoding='UTF-8'

head={
      'if-none-match': '7b8bdd9c471e89ba02e4b2f2030f2a89',
      'if-none-match-': '55b03-e175879bb710cf8bc49b43c7c119cb76',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
      }
re2=re.get("https://shopee.tw/api/v2/search_items/?brandids=5005&by=relevancy&fe_categoryids=2185&limit=50&locations=-1&newest=0&order=desc&page_type=search&rating_filter=4&version=2"
           ,allow_redirects=False,headers=head  )
data=re2.json()
str_f=""
for y in range(len(data)):
    name=str(data['items'][y]['name']).replace(" ","").replace("\t","")
    price=str(data['items'][y]['price']).replace(" ","").replace("\t","")
    str_f+= (name+":"+price)

for z in range(len(target)):
    if(Target[z] in str_f):
        str_f=str_f.replace(Target[z],Value[z])
print(str_f)