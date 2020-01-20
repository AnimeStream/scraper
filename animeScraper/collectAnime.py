import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chromeDriver="C:/Program Files/webdriver/chromedriver"
browser = webdriver.Chrome(chromeDriver)
anime = "boku-no-hero-academia/ep-1"
browser.get('https://9anime.xyz/watch/%s' % anime) # Optional argument, if not specified will search path.
links = browser.find_elements_by_xpath("""//*[@id="load_ep"]/ul""")
print(links.text)


# driver.get('http://www.google.com/')
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()

