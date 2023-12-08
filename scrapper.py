from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from sendMessage import sendMessage

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
    sendMessage()

    for index, element in enumerate(elements, 1):
        print("{} 번째 공지사항 제목: {}, link: https://hubkitchen.startup-plus.kr/cms_for_bcb/process/notice/{}".format(index, element.text, element.attrs['href']))