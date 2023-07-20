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


# ũ�� ����̹� �ڵ� ������Ʈ�� ���� ���
from webdriver_manager.chrome import ChromeDriverManager

# ũ�� ������ �ɼ� ����
chrome_options = Options()

# ���ʿ��� ���� �޽��� ����
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# ũ�� ����̹� �ֽ� ���� ����
service = Service(executable_path=ChromeDriverManager().install())


browser = webdriver.Chrome(service=service, options=chrome_options)

# ������ �ε� ���
wait = WebDriverWait(browser, 10)
short_wait = WebDriverWait(browser, 3)

# ���ϴ� �������� ����
browser.get("https://shopping.naver.com")


# Element ã�� �Լ�
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
