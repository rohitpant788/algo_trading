import time
import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import helper
import kite_automation_config

driver = helper.get_driver()
range_high = 0
range_low = 0

start_tracking_time = datetime.datetime.now().replace(hour=kite_automation_config.KITE_ORB_START_TIME_HOUR,
                                                      minute=kite_automation_config.KITE_ORB_START_TIME_MIN, second=0,
                                                      microsecond=0)
stop_tracking_time = datetime.datetime.now().replace(hour=kite_automation_config.KITE_ORB_END_TIME_HOUR,
                                                     minute=kite_automation_config.KITE_ORB_END_TIME_MIN, second=0,
                                                     microsecond=0)


def add_stock_to_watchlist():
    # Click on firsttab of watchlist when it exists
    helper.click_label_by_xpath(driver,kite_automation_config.KITE_WATCHLIST_FIRST_TAB)

def fetch_high_low(candle_size_in_mins):
    print(f'Candle size in minutes {candle_size_in_mins}')

    time.sleep(kite_automation_config.DELAY_IN_SEC)
    time.sleep(kite_automation_config.DELAY_IN_SEC)
    time.sleep(kite_automation_config.DELAY_IN_SEC)
    time.sleep(kite_automation_config.DELAY_IN_SEC)

    element_current_price = driver.find_element(By.XPATH, kite_automation_config.KITE_STOCK_PRICE)
    if element_current_price.is_displayed():
        print(f'Current Price is {element_current_price.text}')
        now = datetime.datetime.now()
        global stop_tracking_time
        while now < stop_tracking_time:
            now = datetime.datetime.now()
            print(f'now : {now}')
            print(f'now : {stop_tracking_time}')
            start_tracking_high_low_range()


def start_tracking_high_low_range():
    now = datetime.datetime.now()
    # print("Current time: " + now)
    # start_tracking_time = now.replace(hour=kite_automation_config.KITE_ORB_START_TIME_HOUR, minute=kite_automation_config.KITE_ORB_START_TIME_MIN, second=0, microsecond=0)
    global start_tracking_time
    # print("Start Tracking Time: " + start_tracking_time)
    # stop_tracking_time = now.replace(hour=kite_automation_config.KITE_ORB_END_TIME_HOUR, minute=kite_automation_config.KITE_ORB_END_TIME_MIN, second=0, microsecond=0)
    global stop_tracking_time
    # print("Stop Tracking Time: " + stop_tracking_time)
    if (now < start_tracking_time):
        print('Tracking not required at the moment')
    elif (start_tracking_time <= now) & (now <= stop_tracking_time):
        print('Need to track the high and low of the range')
        element_current_price = driver.find_element(By.XPATH, kite_automation_config.KITE_STOCK_PRICE)

        if get_range_low() == 0:
            set_range_low(float(element_current_price.text))
        if get_range_high() == 0:
            set_range_high(float(element_current_price.text))

        # Setting range low
        if float(element_current_price.text) < range_low:
            set_range_low(float(element_current_price.text))

        if float(element_current_price.text) > range_high:
            set_range_high(float(element_current_price.text))
    else:
        pass
    print(f'Current time :{now}')
    print(f'Range Low :{get_range_low()}')
    print(f'Range High :{get_range_high()}')


def set_range_low(low):
    global range_low
    range_low = low


def set_range_high(high):
    global range_high
    range_high = high


def get_range_low():
    global range_low
    return range_low


def get_range_high():
    global range_high
    return range_high


def trade_the_breakout():
    while True:
        if get_range_low() == 0:
            print(f'Range low is {get_range_low()}')
            break
        element_current_price = float(driver.find_element(By.XPATH, kite_automation_config.KITE_STOCK_PRICE).text)
        if get_range_low() > element_current_price:
            print(f' Place the MIS sell order')
            place_order('sell', element_current_price)
            break

        if element_current_price > get_range_high():
            print(f' Place the MIS buy order')
            place_order('buy', element_current_price)
            break
    return None


def place_order(order_type, price):
    print(f' {order_type} placed')
    element_to_hover = driver.find_element(By.XPATH, kite_automation_config.KITE_STOCK_ICICI_LABEL)
    # Hover over the element
    hover = ActionChains(driver).move_to_element(element_to_hover)
    hover.perform()

    if order_type == 'buy':
        # Selecting Order pane
        helper.click_label_by_xpath(driver, kite_automation_config.KITE_STOCK_BUY_LABEL)
    else:
        helper.click_label_by_xpath(driver, kite_automation_config.KITE_STOCK_SELL_LABEL)

    # Selecting Order pane
    helper.click_label_by_xpath(driver, kite_automation_config.KITE_ORDER_PANE_REGULAR)

    # Selecting Intraday Option
    helper.click_label_by_xpath(driver, kite_automation_config.KITE_ORDER_PANE_INTRADAY)

    # Input quantity for trade
    helper.input_field_by_xpath(driver, kite_automation_config.KITE_ORDER_PANE_QUANTITY,
                                kite_automation_config.KITE_ORB_QTY)

    # Input price for trade.
    helper.input_field_by_xpath(driver, kite_automation_config.KITE_ORDER_PANE_PRICE, price)

    # Place Order
    helper.click_label_by_xpath(driver, kite_automation_config.KITE_ORDER_PANE_ORDER_BTN)
