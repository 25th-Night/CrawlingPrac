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

def choose_one(text, options):
    print("--------------------")
    print("text")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    choose = int(input("-> "))
    return choose - 1


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
# cpu_options_list = finds_visible_x(wait,
#                                    '//div[contains(@class, "search_option_item") and .//*[contains(text(), "제조사")]]//input')
cpu_options_list = finds_visible_x(wait,
                                   '//div[contains(@class, "search_option_item") and .//*[contains(text(), "제조사")]]//input')

# 사용자로부터 선택할 cpu 제조사를 입력받기
i = choose_one("CPU 제조사를 골라주세요.",
               [option.get_attribute('data') for option in cpu_options_list])
cpu_manugacturer = cpu_options_list[i].get_attribute('data')

# 사용자가 선택한 cpu 제조사의 checkbox를 클릭
browser.execute_script("arguments[0].click();", cpu_options_list[i])

# 해당 제조사의 cpu 타입 불러오기
cpu_type_list = finds_visible_x(wait, f'//div[contains(text(), "{cpu_manugacturer}")]/..//input[@type="checkbox"]')

# '옵션 더보기' 버튼 클릭
cpu_type_more_btn = find_visible_x(wait, f'//div[contains(text(), "{cpu_manugacturer}")]/..//button[@class="btn_item_more"]')
cpu_type_more_btn.click()

# 사용자로부터 선택할 cpu 타입을 입력받기
i = choose_one("해당 제조사의 CPU 타입를 골라주세요.",
               [option.get_attribute('data') for option in cpu_type_list])

# 사용자가 선택한 cpu 타입의 checkbox를 클릭
browser.execute_script("arguments[0].click();", cpu_type_list[i])

time.sleep(5)

browser.quit()