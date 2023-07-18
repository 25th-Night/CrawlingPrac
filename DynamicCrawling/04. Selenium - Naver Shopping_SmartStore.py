# python "DynamicCrawling/04. Selenium - Naver Shopping_SmartStore.py"

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

import pyperclip

# 크롬 드라이버 자동 업데이트을 위한 모듈
from webdriver_manager.chrome import ChromeDriverManager

# 크롬 브라우저 옵션 지정
chrome_options = Options()

# 불필요한 에러 메시지 삭제
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 크롬 드라이버 최신 버전 설정
service = Service(executable_path=ChromeDriverManager().install())

browser = webdriver.Chrome(service=service, options=chrome_options)

# 페이지 로딩 대기
wait = WebDriverWait(browser, 10)
short_wait = WebDriverWait(browser, 3)

browser.get("https://shopping.naver.com")


# Element 찾는 함수
def find_v(wait: WebDriverWait, css_selector: str):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))


def find_p(wait: WebDriverWait, css_selector: str):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


# 로그인 버튼 찾아서 클릭
find_v(wait, "a#gnb_login_button").click()

# ID, PW 입력창 찾기
input_id = find_v(wait, "input#id")
input_pw = find_v(wait, "input#pw")

# .env 파일 로드
load_dotenv()

# ID, PW 입력 후 엔터 버튼 누르기
# 1. ID를 클립보드에 복사
pyperclip.copy(os.getenv("NAVER_ID"))
# 2. 클립보드로부터 ID를 붙여넣기
input_id.send_keys(Keys.CONTROL, "v")  # MacOS는 Keys.COMMAND
# 3. PW를 클립보드에 복사
pyperclip.copy(os.getenv("NAVER_PW"))
# - 클립보드로부터 PW를 붙여넣기
input_pw.send_keys(Keys.CONTROL, "v")  # MacOS는 Keys.COMMAND
# 4. 엔터 누르기
input_pw.send_keys("\n")

# 정상 로그인 여부 체크 - 로그아웃 버튼 유무 확인
find_p(short_wait, "a#gnb_logout_button")

# 검색 창에 검색어 입력 후 엔터
# 1. 검색 창
search = find_v(short_wait, 'input[type="text"][title="검색어 입력"]')
# 2. 검색어 입력
search.send_keys("아이폰 케이스")
# 3. 잠시 대기
time.sleep(1)
# 4. Enter 키 입력
search.send_keys("\n")

time.sleep(3)

browser.close()