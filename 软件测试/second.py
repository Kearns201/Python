from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
search_windows = driver.current_window_handle
sleep(2)
driver.find_element(By.LINK_TEXT, '登录').click()
sleep(2)
driver.find_element(By.LINK_TEXT, '立即注册').click()
# 获取当前所有打开的窗口的句柄
all_handles = driver.window_handles

for handle in all_handles:
    if handle != search_windows:
        # 切换到注册窗口
        driver.switch_to.window(handle)
        print(driver.title)
        sleep(2)
        driver.find_element(By.NAME, 'userName').send_keys('aa')
        driver.find_element(By.NAME, 'phone').send_keys('13245678')
        sleep(5)
        driver.close()

if __name__ == '__main__':
    sleep(3)
    driver.switch_to.window(search_windows)
    # 关闭div遮幕窗口
    driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_4__closeBtn"]').click()
    print(driver.title)
