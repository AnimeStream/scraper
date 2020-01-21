import time
from selenium import webdriver


def initBrowser():
    chromeDriver="C:/webdriver/chromedriver"
    browser = webdriver.Chrome(chromeDriver)

    return browser

def episodeIterator(anime, browser):
    parsedName = anime.replace(" ","-")
    ep = 1
    browser.get(f'http://vidstreaming.io/videos/{parsedName}-episode-{ep}') 
    time.sleep(3)

    list = []
    videoBlock= browser.find_element_by_xpath("//ul[@class='listing items lists']");
    list = videoBlock.find_elements_by_class_name('video-block')
    
    epLen = len(list)
    episodes = []

    for x in range(1,epLen + 1):
        episodes.append({
            'title':parsedName,
            'link': f'http://vidstreaming.io/videos/{parsedName}-episode-{x}',
            'ep':x
        })

        
    return episodes

# links = browser.find_element_by_xpath('/html/body/div[1]/section/div[1]/div[5]/div/div[1]/div[1]/div[1]/iframe')
# print(links.get_attribute("src"))


if __name__ == "__main__":
    browser = initBrowser()
    targets = episodeIterator("boku no hero academia", browser)
    print(targets)
    srcs = []
    for x in targets:
        browser.get(x.get('link'))
        title = browser.find_element_by_xpath('/html/body/div[1]/section/div[1]/div[5]/div/div[1]/h1')
        links = browser.find_element_by_xpath('/html/body/div[1]/section/div[1]/div[5]/div/div[1]/div[1]/div[1]/iframe')
        srcs.append({
            'title': x.get('title'),
            'episode': x.get('ep'),
            'link':links.get_attribute("src")
        })

        time.sleep(3)

    print(srcs)


