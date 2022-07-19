import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from soupsieve import select_one
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ChromeOptions


baseUrl = 'http://www.golfzon.com/course/list/R#topsearch'
url = baseUrl

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

area = soup.select_one('#datalist.course_list_area')
#courses = area.select('.list_info_tit')
courses = area.select('li')

for course in courses:
    #name = course.find('title')
    a = course.select_one('dd')
    print(a.text)

    name = course.select_one('a')
    print(name.text)
    print("https://www.golfzon.com"+name.get('href'))

    info = course.select_one('.course_info_con2')
    info2 = info.select_one('dd')

    hole,dist = str(info2.text).split('/')
    hole = hole.strip()
    dist = dist.strip()
    print(hole)
    print(dist)
    
    diff_course = info.select_one('span').get('class')
    diff_green = info.select_one('span').get('class')
    print(str(diff_course).strip("[']"))
    print(str(diff_green).strip("[']"))
    print('-----------------------')


options = ChromeOptions()

chrome_driver = webdriver.Chrome(options=options)
chrome_driver.get(url)

elem_hover = chrome_driver.find_element_by_css_selector('.ui-state-default').get('2')
elem_click = chrome_driver.find_element_by_css_selector('.ui_state-hover')

actions = ActionChains()
actions.move_to_element(elem_hover)
actions.click(elem_click)
actions.perform()