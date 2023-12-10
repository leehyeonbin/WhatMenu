from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from is_today import is_today
from post import Post
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
    
    dateList = soup.select('.list-right')
    elements = soup.select('tbody > tr > td > a')

    count = sum(1 for element in dateList if is_today(element.text.strip()))
    posts = []
    
    # for index, element in enumerate(elements[:count], 1):
    for index, element in enumerate(elements, 1):
        print("https://hubkitchen.startup-plus.kr/cms_for_bcb/process/notice/{}".format(element.attrs["href"]))
        driver.get("https://hubkitchen.startup-plus.kr/cms_for_bcb/process/notice/{}".format(element.attrs["href"]))
        driver.implicitly_wait(1)
        title = driver.find_element('xpath', '/html/body/div/div[1]/div/div/div/div[2]/div/div/div/div/div[1]/h2').text
        content = driver.find_element('xpath', '/html/body/div/div[1]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/p/img').get_attribute('src')
        print("{} 번째 공지사항 제목: {}, link: https://hubkitchen.startup-plus.kr/cms_for_bcb/process/notice/{}".format(index, element.text, element.attrs['href']))
        if "[키친인큐베이터] 메뉴공지" in element.text:
            posts.append(Post(title = title, content = content))
            break

    send_message(posts = posts)