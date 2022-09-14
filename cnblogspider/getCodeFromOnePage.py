import win32clipboard
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import pyperclip


header={
"Accept": "application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "zh-cn",
"Accept-Encoding": "gzip, deflate",
"Connection": "keep-alive",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15"
}
executable_path='driver\\chromedriver.exe'
#chrome_options = Options()
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument('--headless')

def getCode(url):
    #获取url内的代码
    codetexts = ''
    browser = webdriver.Chrome(executable_path=executable_path)
    browser.get(url)
    time.sleep(1)
    copybotton = browser.find_elements_by_css_selector("[class='clipboard code-copay-btn hljs-comment']")[-1]
    ActionChains(browser).move_to_element(copybotton).click().click().perform()
    time.sleep(1)
    codetexts=pyperclip.paste()
    browser.close()
    return codetexts
#实现过程中win32clipboard无法达到于其效果，报错 Specified clipboard format is not available，且难以解决
#因此改用pyperclip，但若息屏或设置不显示Chorme时无法复制
#    win32clipboard.OpenClipboard()
#    win32clipboard.EmptyClipboard()
#    browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=executable_path)

#    ActionChains(browser).key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
#    win32clipboard.CloseClipboard()
#    win32clipboard.OpenClipboard()
#    data=win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    
#    win32clipboard.CloseClipboard()
    #输出粘贴板内容
#    data = data.decode('utf-8')


    
if __name__ == '__main__': 
    url = "https://www.cnblogs.com/ghosteq/p/16691733.html"
    print(getCode(url))
#    win32clipboard.CloseClipboard()
#    contextUrlsList = getUrlsList(url,header)
#    print(contextUrlsList)
#    print(len(contextUrlsList))
#    win32clipboard.OpenClipboard()
#    #清空粘贴板
##    win32clipboard.EmptyClipboard()
#    data=win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
#    win32clipboard.CloseClipboard()
    #输出粘贴板内容
#    data = data.decode('utf-8')
#    print(data)
#    print(type(data))
