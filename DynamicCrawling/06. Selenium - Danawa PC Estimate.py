# python "DynamicCrawling/06. Selenium - Danawa PC Estimate.py"

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

# 세부 선택 항목 찾는 함수
def find_detail_options(wait, item_name):
    detail_options = finds_present(wait, 'div.search_option_item')
    for detail_option in detail_options:
        if item_name in detail_option.text:
            return detail_option


# 원하는 페이지에 접속
browser.get("http://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16&logger_kw=dnw_lw_esti")

# 견적 대상 카테고리 번호
category = {
    "cpu": "873",
    "메인보드": "875",
    "메모리": "874",
    "그래픽카드": "876",
    "SSD": "32617",
    "케이스": "879",
    "파워": "880",
}

# 카테고리에 대한 CSS Selector
category_css = {
    c: "dd.category_" + category[c] + " a" for c in category
}

# cpu 카테고리 클릭
cpu = find_visible(wait, category_css["cpu"] )
cpu.click()

# 잠시 대기
time.sleep(1)



# cpu 제조사 input 불러오기
cpu_manufacturer_list = find_detail_options(wait, "제조사").find_elements(By.CSS_SELECTOR, 'input')
print(cpu_manufacturer_list)
for cpu_manufacturer in cpu_manufacturer_list:
    print(cpu_manufacturer.get_attribute('data'))

print('----------------')

# cpu 제조사 input 불러와서 클릭
cpu_manufacturer_list = finds_visible_x(wait, '//div[contains(@class, "search_option_item") and .//*[contains(text(), "제조사")]]//input')
for cpu_manufacturer in cpu_manufacturer_list:
    browser.execute_script("arguments[0].click();", cpu_manufacturer)
    print(cpu_manufacturer.get_attribute('data'))


time.sleep(5)

browser.quit()