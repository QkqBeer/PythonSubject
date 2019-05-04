
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
path = u"C:\Program Files (x86)\Google\Chrome\Application\chromedriver"
browser = webdriver.Chrome(executable_path = path)
try:
    browser.get('https://www.baidu.com')
    input1 = browser.find_element_by_id('kw')
    input1.send_keys('Python')
    input1.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser,10)
    wait.until(EC.presence_of_all_elements_located((By.ID,'content_left')))
    # print(browser.current_url)
    # print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()