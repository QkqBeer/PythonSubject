__author__ = "那位先生Beer"
from selenium import webdriver
def main():
    path = u"C:\Program Files (x86)\Google\Chrome\Application\chromedriver"
    browser = webdriver.Chrome(executable_path = path)
    try:
        hrefList = []
        browser.get('http://daj.shaanxi.gov.cn/MessageList.aspx')
        tableList = browser.find_elements_by_css_selector('.tablelist tbody tr td a')
        for i in range(len(tableList)):
            hrefList.append(tableList[i].get_attribute('href'))
        currentPageUrl = browser.current_url
        nextLevelPage(browser, hrefList)
        browser.get(currentPageUrl)
        Repeat(browser)
    finally:
        browser.close()
def Repeat(browser):
    try:
        button = browser.find_element_by_link_text('下一页')
        button.click()
        browser.implicitly_wait( 20 )
        browser.switch_to_window( browser.window_handles[0] )  # 定位新页面 测试成功
        tableList = browser.find_elements_by_css_selector( '.tablelist tbody tr td a' )
        hrefList = []
        for i in range( len( tableList ) ):
            hrefList.append( tableList[i].get_attribute( 'href' ) )
        currentPageUrl = browser.current_url
        nextLevelPage( browser, hrefList )
        browser.get( currentPageUrl )
        Repeat( browser )
    finally:
        browser.close()
def StrOption(textList):
    f = open('res.txt', 'a', encoding="utf-8")
    for i in range(len(textList)):
        f.write(textList[i])
        f.write('\n')
def nextLevelPage(brower, hrefList):
    textList = []
    for i in range(len(hrefList)):
        brower.get(hrefList[i])
        t = brower.find_elements_by_css_selector('.tableView')[1]
        text = t.find_elements_by_css_selector('tr')[3].find_elements_by_css_selector('td')[1].text
        textList.append(text)
    StrOption(textList)
if __name__ == '__main__':
    main()
