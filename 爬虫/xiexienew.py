__author__ = "那位先生Beer"
from selenium import webdriver
def main():
    path = u"C:\Program Files (x86)\Google\Chrome\Application\chromedriver"
    browser = webdriver.Chrome(executable_path = path)
    try:
        Id = 15285
        for i in range(Id, 1, -1):
            url = 'http://www.zjda.gov.cn/jact/front/mailpubdetail.do?transactId=' + str( i ) + '&sysid=6'
            browser.get(url)
            if browser.current_url != url:
                continue
            else:
                firstTable = browser.find_elements_by_css_selector('div.jact_main div.jact_box div.jact_box_font')[0].find_elements_by_css_selector('table')[0]
                Td = firstTable.find_elements_by_css_selector('tbody tr')[3].find_elements_by_css_selector('td')[3]
                initTime = Td.text

                SecondTable = browser.find_elements_by_css_selector('div.jact_main div.jact_box div.jact_box_font')[1].find_elements_by_css_selector('table')[0]

                contentTr = SecondTable.find_elements_by_css_selector( 'tbody tr' )[2]
                content = contentTr.find_elements_by_css_selector( 'td' )[1].text

                timeTr = SecondTable.find_elements_by_css_selector( 'tbody tr' )[3]
                endTime = timeTr.find_elements_by_css_selector( 'td' )[3].text
                StrOption(initTime + "  " + endTime + "  " + content)
    finally:
        browser.close()

def StrOption(text):
    f = open('res.txt', 'a', encoding="utf-8")
    f.write(text)
    f.write('\n')
if __name__ == '__main__':
    main()
