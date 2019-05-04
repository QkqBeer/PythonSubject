__author__ = "那位先生Beer"
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
path = u"C:\Program Files (x86)\Google\Chrome\Application\chromedriver"
browser = webdriver.Chrome(executable_path = path)
try:
    browser.get('https://www.taobao.com')
    browser.save_screenshot('taobao.jpg')
except Exception:
    browser.close()