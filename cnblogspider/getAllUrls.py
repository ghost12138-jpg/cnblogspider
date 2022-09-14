import requests
from bs4 import BeautifulSoup as BS

class GetAllUrl(object):
    
    header={
    "Accept": "application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-cn",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15"
    }
    def __init__(self,h=None):
        if(h is not None):
            self.header=h
               
    def getAllPagesUrl(self,pagesUrlsList,bs_s, header=header):
        #对于多页的情况，获取每一页的url 
        bs_s_url = bs_s.find(class_="pager").find_all("a")
        for u in bs_s_url:
            if u["href"] not in pagesUrlsList:
                pagesUrlsList.append(u["href"])
        return pagesUrlsList
    
    def getAllUrlListInPages(self,pagesUrlsList, header=header):
        #获取页面表内，全部的文章链接，返回一个列表
        contextUrlsList = []
        for pages in pagesUrlsList:
            r_s = requests.get(pages, header)
            bs_s = BS(r_s.text,"lxml")
            urls = bs_s.find_all(class_="entrylistItemTitle")
            
            for u in urls:
                if u["href"] not in contextUrlsList:
                    contextUrlsList.append(u["href"])
        return contextUrlsList
         
    def getAllUrlDicInPages(self,pagesUrlsList, header=header):
        #获取页面表内，全部的文章链接，返回一个字典，键为文章标题，值为文章链接
        contextUrlsDic = {}
        for pages in pagesUrlsList:
            r_s = requests.get(pages, header)
            bs_s = BS(r_s.text,"lxml")
            urls = bs_s.find_all(class_="entrylistItemTitle")
            
            for u in urls:
                if u.find("span").string not in contextUrlsDic:
                    contextUrlsDic[u.find("span").string]=u["href"]
        return contextUrlsDic
    
    def getUrlsList(self,url,header=header):
        #获取url系列页的所有文章链接，返回一个列表
        pagesUrlsList = []        
        pagesUrlsList.append(url)
        r_s = requests.get(url, header)
        bs_s = BS(r_s.text,"lxml")
        pagesUrlsList = self.getAllPagesUrl(pagesUrlsList,bs_s, header)
        contextUrlsList = self.getAllUrlListInPages(pagesUrlsList,header)
        return contextUrlsList
    
    def getUrlsDic(self,url,header=header):
        #获取url系列页的所有文章链接，返回一个字典，键为文章标题，值为文章链接
        pagesUrlsList = []
        pagesUrlsList.append(url)
        r_s = requests.get(url, header)
        bs_s = BS(r_s.text,"lxml")
        pagesUrlsList = self.getAllPagesUrl(pagesUrlsList,bs_s, header)
        contextUrlsList = self.getAllUrlDicInPages(pagesUrlsList,header)
        return contextUrlsList
if __name__ == '__main__': 
    url = "https://www.cnblogs.com/ghosteq/category/2100349.html?page=1"
    header={
    "Accept": "application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-cn",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15"
    }
    ga = GetAllUrl(header)
    contextUrlsList = ga.getUrlsList(url)
    contextUrlsDic = ga.getUrlsDic(url)
    print(contextUrlsList)
    print(len(contextUrlsList))
    print(contextUrlsDic)
    print(len(contextUrlsDic))
