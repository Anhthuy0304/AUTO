import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("/Users/anhthuy/Documents/GitHub/chromedriver")
url='https://todo-list-login.firebaseapp.com/#!/'
driver.get(url)
delay=1
tmp=[]
while len(tmp)==0:
    page_source = BeautifulSoup(driver.page_source, "html.parser")
    tmp = page_source.find_all("a", {"class": "btn btn-social btn-github"})
    time.sleep(delay)
window_before = driver.window_handles[0]
login_click = driver.find_element_by_xpath('/html/body/ng-view/div/a[4]')
login_click.click()
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
tmp=[]
while len(tmp)==0:
    page_source = BeautifulSoup(driver.page_source, "html.parser")
    tmp = page_source.find_all("label", {"for": "login_field"})
    time.sleep(delay)
email = driver.find_element_by_id("login_field").send_keys('Anhthuy0304')
password = driver.find_element_by_id("password").send_keys('Anhthuy12@')
signin_click = driver.find_element_by_xpath('//*[@id="login"]/div[3]/form/div/input[12]').click()
try:
    time.sleep(2)
    author_click = driver.find_element_by_xpath('//*[@id="js-oauth-authorize-btn"]').click()
except:
    print('To be continued')
driver.switch_to.window(window_before)
tmp=[]
while len(tmp)==0:
    page_source = BeautifulSoup(driver.page_source, "html.parser")
    tmp = page_source.find_all("div", {"class": "brownhill"})
    time.sleep(delay)
for i in range(10):
    text = driver.find_element_by_xpath('/html/body/ng-view/div/div[2]/div[1]/input').send_keys(i)
    addlist_click = driver.find_element_by_xpath('/html/body/ng-view/div/div[2]/div[2]/button').click()
time.sleep(3)
logout_click = driver.find_element_by_xpath('/html/body/ng-view/div/nav/div/ul/li/div/button').click()
####################################################################################################################
tmp=[]
while len(tmp)==0:
    page_source = BeautifulSoup(driver.page_source, "html.parser")
    tmp = page_source.find_all("a", {"class": "btn btn-social btn-github"})
    time.sleep(delay)
window_before = driver.window_handles[0]
login_click = driver.find_element_by_xpath('/html/body/ng-view/div/a[4]')
login_click.click()
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
try:
    tmp = []
    while len(tmp) == 0:
        page_source = BeautifulSoup(driver.page_source, "html.parser")
        tmp = page_source.find_all("label", {"for": "login_field"})
        time.sleep(delay)
    email = driver.find_element_by_id("login_field").send_keys('username')
    password = driver.find_element_by_id("password").send_keys('password')
    signin_click = driver.find_element_by_xpath('//*[@id="login"]/div[3]/form/div/input[12]').click()
except:
    print('To be continued')
try:
    time.sleep(2)
    author_click = driver.find_element_by_xpath('//*[@id="js-oauth-authorize-btn"]').click()
except:
    print('To be continued')
driver.switch_to.window(window_before)
tmp=[]
while len(tmp)==0:
    page_source = BeautifulSoup(driver.page_source, "html.parser")
    tmp = page_source.find_all("div", {"class": "brownhill"})
    time.sleep(delay)
for i in range(10,5,-1):
    remove_click = driver.find_element_by_xpath('/html/body/ng-view/div/div[3]/div/ul/li['+str(i)+']/div/div[2]/button').click()
time.sleep(3)
logout_click = driver.find_element_by_xpath('/html/body/ng-view/div/nav/div/ul/li/div/button').click()
