from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import helper
import kite_automation_config
import time


driver = None
def get_driver():
    global driver
    if driver is None:
        driver = webdriver.Chrome(kite_automation_config.PATH)
    return driver

def login_kite_in_browser():
    driver = get_driver()
    driver.maximize_window()

    driver.get(kite_automation_config.KITE_LOGIN_URL)

    print(driver.title)

    helper.input_field_by_xpath(driver,kite_automation_config.KITE_USER_ID_XPATH,kite_automation_config.KITE_LOGIN)
    helper.input_field_by_xpath(driver,kite_automation_config.KITE_PASSWORD_XPATH,kite_automation_config.KITE_PASSWORD)
    helper.click_label_by_xpath(driver,kite_automation_config.KITE_LOGIN_BUTTON_XPATH)

    # # Fetching xpath of pin
    # element_pin = driver.find_element(By.XPATH, kite_automation_config.KITE_PIN_XPATH)
    # if element_pin.is_displayed():
    #     element_pin.send_keys(kite_automation_config.KITE_PIN)
    #
    # element_continue_btn = driver.find_element(By.XPATH, kite_automation_config.KITE_CONTINUE_BTN_XPATH)
    # if element_continue_btn.is_displayed():
    #     element_continue_btn.click()

def click_label_by_xpath(driver,xpath):
    wait = WebDriverWait(driver, 300)
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    element = driver.find_element(By.XPATH, xpath)
    if element.is_displayed():
        element.click()


def input_field_by_xpath(driver, xpath, field_value):
    wait = WebDriverWait(driver, 300)
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    element = driver.find_element(By.XPATH, xpath)
    if element.is_displayed():
        time.sleep(kite_automation_config.DELAY_IN_SEC)
        element.clear()
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)
        element.send_keys(field_value)

def round_nearest(x,a):
    return round(round(x/a)*a,2)