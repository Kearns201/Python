from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
    link = driver.find_element(By.XPATH, '//span[contains(text(),"设置")]')
    action = ActionChains(driver)
    action.click_and_hold(link).perform()
    driver.find_element(By.LINK_TEXT, "搜索设置").click()
    driver.find_element(By.CLASS_NAME, 'prefpanelgo').click()
    # 获取模式警告框
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    # 点击警告框的确定按钮
    sleep(2)
    alert.accept()
    driver.quit()