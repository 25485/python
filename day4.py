import urllib
from selenium import webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='./chromedriver')

# 로그인 정보
loginUrl = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
loginId = ''
loginPw = ''

# 로그인 실행
driver.get(loginUrl)

# 로그인 대기
driver.implicitly_wait(5)

# id,pw 입력
driver.find_element_by_name('username').send_keys(loginId)
driver.find_element_by_name('password').send_keys(loginPw)

# 로그인 버튼 클릭
driver.find_element_by_css_selector('button.L3NKy').click()

# 알림 설정 클릭
driver.find_element_by_css_selector('button.HoLwm').click()

# 검색 태그 정보
tag = 'bts'
searchUrl = 'https://www.instagram.com/explore/tags/' + tag

# 태그 검색 실행
driver.get(searchUrl)

# 태그 검색 대기
driver.implicitly_wait(5)
elem = driver.find_element_by_tag_name("body")
scrollCnt = 1
myList = []
while scrollCnt < 15:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    while len(myList) < 101:
        for image in driver.find_elements_by_css_selector('img.FFVAD'):
            imgUrl = image.get_attribute('srcset')
            url = imgUrl.split(' 150w,')
            if(len(myList) < 101):
                myList.append(url[0])
        break
    scrollCnt += 1
# driver.quit()