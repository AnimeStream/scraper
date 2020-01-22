import time
from selenium import webdriver
import re
from selenium.webdriver.chrome.options import Options


def init_browser():
    chromeDriver = "C:/Program Files/webdriver/chromedriver"
    options = Options()
    options.add_argument(' -- headless')
    options.add_argument(' -- disable-gpu')
    browser = webdriver.Chrome(chromeDriver)

    return browser

def episode_iterator(anime, browser):
    parsedName = anime.replace(" ", "-")
    ep = 1

    try:
       browser.get(f'http://vidstreaming.io/videos/{parsedName}-episode-{ep}') 
    except:
        print('title not found')
    
    time.sleep(3)

    list = []
    videoBlock = browser.find_element_by_xpath("//ul[@class = 'listing items lists']");
    list = videoBlock.find_elements_by_class_name('video-block')
    
    epLen = len(list)
    episodes = []

    for x in range(1, epLen + 1):
        episodes.append({
            'title':parsedName, 
            'link': f'http://vidstreaming.io/videos/{parsedName}-episode-{x}', 
            'ep':x
        })

        
    return episodes

    

def crawl(anime):
    browser = init_browser()
    targets = episode_iterator(anime, browser)
    srcs = []
    for x in targets:
        browser.get(x.get('link'))

        try:
            title = browser.find_element_by_xpath('/html/body/div[1]/section/div[1]/div[5]/div/div[1]/h1')
            links = browser.find_element_by_xpath('/html/body/div[1]/section/div[1]/div[5]/div/div[1]/div[1]/div[1]/iframe')
            imgPlaceholder = browser.find_elements_by_xpath("//div[@class = 'video-info-left xh-highlight']//li[1]//a[1]//div[1]//div[1]//img[1]")
            
            for x in imgPlaceholder:
                print("sup",x.get_attribute('src'))
                
        except:
            print("element not found")
            break 

        srcs.append({
            'title': x.get('title'), 
            'episode': x.get('ep'), 
            'link':links.get_attribute("src")
        })

        time.sleep(3)

    print(srcs)


    

if __name__ == "__main__":
    crawl('black clover tv')