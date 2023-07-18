# python "DynamicCrawling/04. Selenium - Naver Shopping_SmartStore.py"

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

browser.get("https://shopping.naver.com")

browser.close()

