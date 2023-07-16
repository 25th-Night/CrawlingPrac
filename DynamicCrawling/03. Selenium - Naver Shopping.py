
# python "DynamicCrawling/03. Selenium - Naver Shopping.py"

# 크롬 드라이버 기본 모듈
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 크롬 드라이버 자동 업데이트을 위한 모듈
from webdriver_manager.chrome import ChromeDriverManager

import time


# Selenium이 Chrome Driver를 만듦
# Driver가 하나의 프로그램이니까, 프로그램의 위치를 지정해줘야 함

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 삭제
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 크롬 드라이버 최신 버전 설정
service = Service(executable_path=ChromeDriverManager().install())


browser = webdriver.Chrome(service=service, options=chrome_options)
time.sleep(3)
browser.close()