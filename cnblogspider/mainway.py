from getAllUrls import GetAllUrl
import time
from getCodeFromOnePage import getCode
import os

#设置一些常量
header={
"Accept": "application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "zh-cn",
"Accept-Encoding": "gzip, deflate",
"Connection": "keep-alive",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15"
}

start_url = "https://www.cnblogs.com/ghosteq/category/2100349.html?page=1"
out_dir = 'AllPATCPPCode'

#存储
def store_lists_to_a_file(lists,file_names = "lists.txt"):
    
    fo = open(file_names,"w",encoding = "utf8",newline="")
    for i in lists:
        fo.writelines(str(i))
    fo.close()
    return 0

#设置相应的文件路径
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

#获取网页的信息
t1 = time.time()
ga = GetAllUrl()
urldic = ga.getUrlsDic(start_url)
t2 = time.time()
print('获取网址部分耗时 {} 秒'.format(t2-t1))

#获取存储页面内代码
for k,v in urldic.items():
    code = getCode(v)
    filespath = out_dir + "\\" + k +".cpp"
    store_lists_to_a_file(code,filespath)
t1 = time.time()
print('获取代码部分耗时 {} 秒'.format(t1-t2))

