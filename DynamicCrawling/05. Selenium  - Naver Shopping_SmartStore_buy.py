# python "DynamicCrawling/05. Selenium  - Naver Shopping_SmartStore_buy.py"

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

# 광고 상품은 거의 스마트 스토어 제품이므로, 광고 상품을 검색
# 1. 1번째 광고 상품 찾아서 클릭
target = find_v(wait, "a[class*=adProduct_link__]")
target.click()

# 연결된 창으로 전환
browser.switch_to.window(browser.window_handles[1])

# Select box 요소를 찾기
# 1. wait은 하나만 가져오기 때문에 요소를 찾아 기다리는 역할로만 사용
find_p(wait, 'a[aria-haspopup="listbox"]')
# 2. find_elements 로 모든 Select box 요소를 가져오기
select_boxes = browser.find_elements(By.CSS_SELECTOR, 'a[aria-haspopup="listbox"]')
for select_box in select_boxes:
    print(select_box.text)

# 1번째 select box부터 선택
select_boxes[0].click()
time.sleep(0.3)

# 1번째 select box의 1번째 옵션을 선택
# find_p(wait, 'ul[role=listbox] a[role=option]')
browser.find_elements(By.CSS_SELECTOR, 'ul[role=listbox] a[role=option]')[0].click()

# 2번째 select box부터 선택
select_boxes[1].click()
time.sleep(0.1)

# 2번째 select box의 1번째 옵션을 선택
browser.find_elements(By.CSS_SELECTOR, 'ul[role=listbox] a[role=option]')[0].click()

# 구매 버튼 클릭
buy_btn = find_v(wait, "div[class*='N=a:pcs.buy'] a")
buy_btn.click()

# 배송지 선택 - 우리집
# find_v(wait, 'div.recent_deli span.item')
delivery_list = browser.find_elements(By.CSS_SELECTOR, 'div.recent_deli span.item')
for delivery in delivery_list:
    print(delivery.text)
    if '우리집' in delivery.text:
        delivery.find_element(By.CSS_SELECTOR, 'span.radio-mark').click()
        break

# 결제 버튼 클릭
find_p(wait, 'button.btn_payment').click()

time.sleep(5)

browser.quit()
