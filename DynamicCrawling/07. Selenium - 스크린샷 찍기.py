# python "DynamicCrawling/07. Selenium - 스크린샷 찍기.py"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# 크롬 드라이버 자동 업데이트을 위한 모듈
from webdriver_manager.chrome import ChromeDriverManager


# Element 찾는 함수
def find_visible(wait: WebDriverWait, css_selector: str) -> WebDriverWait:
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))


def finds_visible(wait: WebDriverWait, css_selector: str):
    find_visible(wait, css_selector)
    return browser.find_elements(By.CSS_SELECTOR, css_selector)


def find_present(wait: WebDriverWait, css_selector: str) -> WebDriverWait:
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


def finds_present(wait: WebDriverWait, css_selector: str):
    find_present(wait, css_selector)
    return browser.find_elements(By.CSS_SELECTOR, css_selector)


def find_visible_x(wait: WebDriverWait, xpath: str) -> WebDriverWait:
    return wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))


def finds_visible_x(wait: WebDriverWait, xpath: str):
    find_visible_x(wait, xpath)
    return browser.find_elements(By.XPATH, xpath)


# 크롬 브라우저 옵션 지정
chrome_options = Options()

# 불필요한 에러 메시지 삭제
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 브라우저를 백그라운드에서 실행
chrome_options.add_argument("--headless")

# 브라우저 창의 크기 지정
chrome_options.add_argument("--window-size=1280,10000")

# 크롬 드라이버 최신 버전 설정
service = Service(executable_path=ChromeDriverManager().install())


browser = webdriver.Chrome(service=service, options=chrome_options)

# 페이지 로딩 대기
wait = WebDriverWait(browser, 10)
short_wait = WebDriverWait(browser, 3)

# 원하는 페이지에 접속
browser.get("https://www.naver.com/")
find_visible(wait, "input#query").send_keys("패스트캠퍼스\n")

# 특정 요소 찾기
e = finds_visible(wait, 'section.sp_intent_block')[1].find_element(By.CSS_SELECTOR, 'li:nth-of-type(1)')

# 해당 요소의 스크린샷 찍기 - 경로 및 파일명을 인자로 지정
# e.screenshot("./static/img/test01.png")

# 전체 스크린샷 찍기 - 경로 및 파일명을 인자로 지정
# browser.save_screenshot("./static/img/test04.png")

# 해당 요소의 테두리에 빨간 선 추가
browser.execute_script("document.querySelectorAll('section.sp_intent_block')[1].querySelector('li:nth-of-type(1)').setAttribute('style', 'border:10px solid red')")

# body 요소의 스크린샷을 찍기
body = find_visible(wait, "body")
body.screenshot("./static/img/test06.png")

browser.quit()