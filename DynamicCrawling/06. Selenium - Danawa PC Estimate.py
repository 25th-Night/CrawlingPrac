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
    print(text)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    choose = int(input("-> "))
    return choose - 1


def go_to_category(wait, category_name):
    find_visible(wait, category_css[category_name]).click()
    time.sleep(1)


def choice_content_input_list(wait, content):
    content_element = find_visible_x(wait, f'//div[contains(@class, "search_option_item") and ./*[contains(text(), "{content}")]]')
    try:
        content_element.find_element(By.CSS_SELECTOR, 'button.btn_item_more').click()
    except:
        pass

    options = content_element.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')

    i = choose_one(f"{content}를 골라주세요.", [option.get_attribute('data') for option in options])

    browser.execute_script("arguments[0].click();", options[i])

    return options[i].get_attribute('data')


def parse_selling_products():
    time.sleep(0.5)
    products = []
    products_info = []
    for product in finds_visible(wait, 'table.tbl_list tr[class^=productList_]'):
        name = product.find_element(By.CSS_SELECTOR, 'p.subject a').text
        try:
            price = product.find_element(By.CSS_SELECTOR, 'span.prod_price').text
        except:
            continue
        products.append(product)
        products_info.append(f"제품명: {name}, 가격: {price}")
    return products, products_info


def choice_product():
    try:
        products, products_info = parse_selling_products()
        i = choose_one("제품의 번호를 입력해주세요.\n 번호/제품명/가격 을 의미합니다.", products_info)
        products[i].find_element(By.CSS_SELECTOR, 'td.rig_line a').click()
    except:
        print("검색된 제품이 존재하지 않습니다.")


# 원하는 페이지에 접속
browser.get("http://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16&logger_kw=dnw_lw_esti")

# cpu 카테고리로 이동
go_to_category(wait, "cpu")

# cpu 제조사를 유저로부터 입력받아 선택
selected_manufacturer = choice_content_input_list(wait, "제조사")


# 제조사에 따른 cpu 타입을 유저로부터 입력받아 선택
choice_content_input_list(wait, selected_manufacturer)

# 유저로부터 선택받은 cpu를 담기
choice_product()

# 메인보드
go_to_category(wait, "메인보드")

# 메인보드 제조사, 제품 분류 클릭

choice_content_input_list(wait, "제조사")

# 메인보드 제품 분류 리스트 클릭
cpu_type = find_visible_x(wait,
               f'//div[contains(@class, "search_option_item") and ./*[contains(text(), "제품 분류")]]//input[contains(@data, "{selected_manufacturer}")]'
               )
browser.execute_script("arguments[0].click();", cpu_type)


# 유저로부터 선택받은 메인보드를 담기
choice_product()

time.sleep(5)

browser.quit()