import requests
import urllib
form_data = {
'startStation':'f2519629-5973-4d08-913b-479cce78a356',
'endStation':'977abb69-413a-4ccf-a109-0272c24fd490',
'theDay':'2019%2F03%2F09',
'timeSelect':'22%3A00',
'waySelect':'DepartureInMandarin',
'RestTime':'',
'EarlyOrLater':'',

}
#'maxDateSet':'2019/04/01'
re=requests.session()
header={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'168',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'AcceptThsrcCookiePolicyTime=Fri%20Mar%2001%202019%2020:50:59%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93); ak_bmsc=DDAE5FDBAB28BDA5A627250B7D4B6B5D17372E64404D0000C9697E5CBF36E75A~plaC+uub4EkuBMkdYby/5usGOq37XGKMaYfBrohU3bVFyKd2mu4saxjHKkdEX/B09N9/aZa/FkLXjErIvnUVH9xHi8x/vQRant5vMvm5TzmxveKnL1ilSUoYF0QmnNi38CBF1r8qYsFRFBZArb0Vcg3PLCdSqgMI/aWOTZVhEos+/S1LaWPQbacJUxCDCKwOmygj1HJUSLpU1/0zXbL4EqP7Rf2ojnecu1TtQNIvuSKZ8=; ASP.NET_SessionId=az15bmvvkslbsf55xiysr455; bm_mi=75F0EB16AA404AB776489075DD218EC5~p6uUwLzz/4UXTPu6Pwvjl48KiD07HMlOoYTUlaYhBUmRs2lhFT9GwDA4iVyGxGrxVUuF9ziyCelYLjWYf9vlRCY4h/YaHbp2p6gnvinak7xHiUOV6rFcQTw+9ehBcpzXncBaMpkSk3Odvr4idv4yah56uCCHF9Bhgq1TT6El9NvTT50r5zOKLu7ZUhYFZNYL/1CMPSxk40jKEubC/bB2HFQG9KWySF6ipqfIKvCDuFs=; bm_sv=B323786DE405FF2248BB1AB73F785EFE~Dnsg7Asw4H5mSAgyyQeLvQADGfoEBskDq26mr2FjrKQcJpsM4S+M+Z0mvjtZqNEzpvEAbLpnWIywjBZZIv9Q+RTyRtbks6f6wyBTItz2lTbtRHiAYjaGEj43jzT4sRJmgN8LVHCt7SEovJ68p9Wx8IWdiW+cgFp0meOs1UICwK4=; TS01ce71a1=013b146f10cafdf6223fc29285bd3637b8bfad7db13f0b38c5efe48d749753898fab915b1be9dcd6273d40929832bfcc8153c59138',
'Host':'m.thsrc.com.tw',
'Origin':'https://m.thsrc.com.tw',
'Referer':'https://m.thsrc.com.tw/tw/timetable/searchresult',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

res=re.get("http://www.thsrc.com.tw/tw/TimeTable/SearchResultList",headers=header)
print(res)




head={
'Cookie':'AcceptThsrcCookiePolicyTime=Fri%20Mar%2001%202019%2020:50:59%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93); ASP.NET_SessionId=3zd2axq1kxpn4h55ifazknvh; TS01ce71a1=013b146f10328020c40d3061e082e1648e77afb4f06ecd2bcc7ed08e7647d053ee87e485cec0c62982a7c9ffb0ed0438062a141c8c',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',''
'Host':'m.thsrc.com.tw',
'Origin':'https://m.thsrc.com.tw',
'Referer':'https://m.thsrc.com.tw/tw/timetable/searchresult'
}
res1=re.post( "https://m.thsrc.com.tw/tw/TimeTable/SearchResult",data=form_data,headers=head)
print(res1)