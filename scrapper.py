from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from send_message import send_message

def scrapper():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    # 불필요한 에러 메시지 없애기
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # 브라우저 생성
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(3)
    
    driver.get("https://hubkitchen.startup-plus.kr/cms_for_bcb/process/notice/list.do?nowPage=1&show_no=2120&check_no=2106&c_maker=1&board_no=2120&c_relation=36&c_relation2=23&s_target=&s_text=")
    
    html = driver.page_source
    soup = bs(html, "html.parser")

    elements = soup.select('tbody > tr > td > a')

    for index, element in enumerate(elements, 1):
        print("{} 번째 공지사항 제목: {}, link: https://hubkitchen.startup-plus.kr/cms_for_bcb/process/notice/{}".format(index, element.text, element.attrs['href']))
    
    dateList = soup.select('.list-right')
    # for element in filter(element.text.strip() == "2023-12-08", dateList):
    #     print("{}".format(element.text))
    for index, element in enumerate(dateList, 1):
        print("{}".format(element.text.strip()))
    driver.find_element('xpath', '/html/body/div/div[1]/div/div/div/div[2]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[2]/a').click()
    driver.implicitly_wait(2)

    title = driver.find_element('xpath', '/html/body/div/div[1]/div/div/div/div[2]/div/div/div/div/div[1]/h2').text
    content = driver.find_element('xpath', '/html/body/div/div[1]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/p/img').get_attribute('src')
    print(title)
    print(content)

    send_message(title, content)