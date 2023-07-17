# python "DynamicCrawling/03. Selenium - Naver Shopping.py"

# 크롬 드라이버 기본 모듈
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 크롬 드라이버 자동 업데이트을 위한 모듈
from webdriver_manager.chrome import ChromeDriverManager

import time

# Selenium이 Chrome Driver를 만듦
# Driver가 하나의 프로그램이니까, 프로그램의 위치를 지정해줘야 함


# 크롬 브라우저 옵션 지정
chrome_options = Options()
# 브라우저의 창 사이즈 지정
chrome_options.add_argument("--window-size=900,1000")
# 샌드박스를 비활성화
chrome_options.add_argument("--no-sandbox")
# 크롬을 백그라운드에서 실행
# chrome_options.add_argument("headless")


# 불필요한 에러 메시지 삭제
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 크롬 드라이버 최신 버전 설정
service = Service(executable_path=ChromeDriverManager().install())

browser = webdriver.Chrome(service=service, options=chrome_options)

# 페이지 이동 및 로딩 대기
browser.get("https://shopping.naver.com")

# 페이지 로딩 대기
wait = WebDriverWait(browser, 10)


# Element 찾는 함수
def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

# 검색 입력 Element
search = find(wait, 'input[type="text"][title="검색어 입력"]')

# 검색어 입력
search.send_keys("토니모리 클렌징폼")

# 검색 버튼 클릭
button = find(wait, 'div[class*="_searchInput_layer_tooltip_"] ~ button[class*="_searchInput_button_search_"]')
print(button)
button.click()

time.sleep(3)

browser.close()
