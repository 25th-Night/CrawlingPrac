
# python "DynamicCrawling/02. Selenium 셋팅 - Docker.py"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# 필요한 경우 옵션을 추가할 수 있습니다.
# options.add_argument("--headless")  # 헤드리스 모드로 실행할 경우

browser = webdriver.Remote("http://127.0.0.1:4444/wd/hub", options=options)
browser.get("http://naver.com")
print(browser.title)
browser.quit()