from bs4 import BeautifulSoup
from datetime import datetime
import sys
import os
# 提取指定目录下已经抓取的新闻txt文件
def get_news(file):
    try:
        f=open(file,'r',encoding='utf-8') 
        txt=f.read()
        f.close()
    except Exception as e:
        print(e)
        return None
    return txt
# 保存文本
def save_text(file, newscontent):
    # 输出
    f = open(file, "wb")
    for fc in newscontent:
       f.write((fc+'\n').encode("utf-8"))
    f.close()

dir=input("输入txt文件的目录 ：")#输入所要合并的txt文件所在目录，
list = os.listdir(dir)  #列出目录下的所有文件和目录
news_recs=[]#新建一个列表用来存放每个txt文件中的文本，一个[]对应一个文本
for line in list:
      filepath = os.path.join(dir,line) #构成全路径文件
      if line[-3:]=='txt':#判断文件是否为txt
        print(filepath)#如果是那么输出文件的全路径
        newstext=get_news(filepath)#提取这个文件里的文本
        news_recs.append(newstext)#将其存储到列表中

allnews=sys.path[0]+os.sep+'allnews.txt'#编写合并后文档的存储路径，这里存放在与新闻正文相同的路径下
save_text(allnews, news_recs)#保存合并后的文档
print("保存新闻记录：",allnews)#输出保存的路径
