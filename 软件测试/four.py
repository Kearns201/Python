from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

if __name__ == '__main__':
    drive = webdriver.Chrome()
    drive.implicitly_wait(10)
    drive.get('http://127.0.0.1:1080/WebTours/')
    drive.maximize_window()
    # drives.switch_to.parent_frame()
    drive.switch_to.frame('body')
    drive.switch_to.frame('navbar')
    # drives.find_element(By.,'/html/frameset/frame[2]')
    sleep(2)
    drive.find_element(By.XPATH, '/html/body/form/table/tbody/tr[4]/td[2]/input').send_keys('jojo')
    drive.find_element(By.XPATH, '/html/body/form/table/tbody/tr[6]/td[2]/input').send_keys('bean')
    drive.find_element(By.NAME, 'login').click()
    sleep(3)
    drive.quit()