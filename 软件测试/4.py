from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.126.com")
    driver.maximize_window()
    search_windows = driver.current_window_handle
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="normalLoginTab"]/div[1]/div[2]/a[1]').click()
    all_handles = driver.window_handles
    for handle in all_handles:
        if handle != search_windows:
            # 切换到注册窗口
            driver.switch_to.window(handle)
            print(driver.title)
            sleep(2)
            driver.find_element(By.XPATH,'//*[@id="username"]').send_keys('aaaa')
            driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('5646556')
            sleep(5)
            driver.close()
