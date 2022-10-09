from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By

# driver=webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
driver = webdriver.Chrome()
# options = webdriver.ChromeOptions()
# options.add_argument('--disable-blink-features=AutomationControlled')  # 避免webdriver检测
# driver.set_window_size(1290,1080)
driver.implicitly_wait(10)
# driver.get('https://kyfw.12306.cn/otn/resources/login.html')
driver.maximize_window()
# driver.find_element_by_id("J-login").click()
driver.get("http://127.0.0.1:1080/cgi-bin/nav.pl?in=home")

time.sleep(1)
login_windows = driver.current_window_handle
# driver.get('http://127.0.0.1:1080/cgi-bin/nav.pl?in=home/')
# driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td[2]/input')
# driver.switch_to.frame(driver.find_element(By.XPATH,"html/frameset"))
# driver.switch_to.frame()
# aa = driver.find_element(By.XPATH,'/html/frameset/frame[1]')
# bb = aa.get_attribute('name')
# print(bb)

driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[4]/td[2]/input').send_keys("jojo")
# driver.find_element(By.NAME, "username").send_keys("jojo")
driver.find_element(By.NAME, "password").send_keys("bean")
driver.find_element(By.NAME, "login").click()
time.sleep(3)

all_handles = driver.window_handles
for handle in all_handles:
    if handle != login_windows:
        driver.switch_to.window(handle)
        print(driver.title)
        driver.switch_to.frame("navbar")
        driver.find_element(By.XPATH, '/html/body/center/center/a[1]/img').click()
        time.sleep(2)
        driver.switch_to.parent_frame()
        driver.switch_to.frame("info")
        driver.find_element(By.XPATH, '/html/body/blockquote/form/table/tbody/tr[7]/td/input').click()
