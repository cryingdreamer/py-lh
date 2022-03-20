import requests
from bs4 import BeautifulSoup
from datetime import datetime
import traceback
import os
import re
i=1
newsind=1
for j in range(3):
    url="https://search.cctv.com/search.php?qtext=%E4%B8%A4%E4%BC%9A&sort=relevance&type=web&vtime=&datepid=1&channel=&page="
 #抓取页面，这里我们只是演示所以之抓取3页
    httpheaders={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
    url=url+str(j+1)#通过每次循环j来改变url地址实现访问1、2、3页（j依次为0、1、2）
    print(url)
    p=requests.get(url,headers=httpheaders)
    p.encoding='UTF-8'
    #编码要与抓取网页的编码一致
    lh=p.text
    
    #提取超链接
    url_list=re.findall('span lanmu1="https://news.cctv.com/[0-9]+/[0-9]+/[0-9]+/[0-9a-zA-Z/.]+shtml"',lh)
    urllist=[]
    for u in url_list:
        urllist.append(u[13:len(u)-1])
    #抓新闻网页
    for u in urllist:
     print(u)
     res = requests.get(u)
     res.encoding = 'utf-8'
     soup = BeautifulSoup(res.text, 'lxml')
 # 正文
     news_article = soup.select('p')
     tmp_str = ''
     for i in range(len(news_article)-1):
       tmp_str += news_article[i].text+ '\n'

     #显示正文
     #print(tmp_str)
     f=open("newstext"+str(newsind)+".txt","wb")
     f.write(tmp_str.encode("utf-8"))
     f.close()
     newsind=newsind+1
     
