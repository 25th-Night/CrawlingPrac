
# python "DynamicCrawling/02. Selenium 셋팅 - Docker.py"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()


browser = webdriver.Remote("http://127.0.0.1:4444/wd/hub", options=chrome_options)
browser.get("http://naver.com")
print(browser.title)
browser.quit()