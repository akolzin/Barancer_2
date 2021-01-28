import subprocess
import pytest
import time
import os
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib3.util import wait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def driver(request):
    #wd1 = webdriver.Ie("C:\\tools\\IEDriverServer.exe")
    #wd = webdriver.Firefox()
    #wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Firefox Nightly\\firefox.exe")
    wd = webdriver.Edge()
    #wd1 = webdriver.Chrome()
    #wd = webdriver.Ie(capabilities={"requireWindowFocus": True})

    # dri = webdriver.Ie()
    # dri.get("http://www.google.com/")
    # textarea = dri.find_element_by_name("q")
    # textarea.send_keys("webdriver")
    # submit_button = dri.find_element_by_class_name("gNO89b")
    # time.sleep(1)
    # submit_button.click()
    # dri.quit()
    #
    # dri1 = webdriver.Edge()
    # dri1.get("http://www.google.com/")
    # textarea1 = dri1.find_element_by_name("q")
    # textarea1.send_keys("webdriver")
    # submit_button1 = dri1.find_element_by_class_name("gNO89b")
    # time.sleep(1)
    # submit_button1.click()
    # dri1.quit()
    #
    # dri2 = webdriver.Chrome()
    # dri2.get("http://www.google.com/")
    # textarea2 = dri2.find_element_by_name("q")
    # textarea2.send_keys("webdriver")
    # submit_button2 = dri2.find_element_by_class_name("gNO89b")
    # time.sleep(1)
    # submit_button2.click()
    # dri2.quit()

    # subprocess.Popen(('start', 'C:\\Users\\akolzin\\Desktop\\site\\site\\1.txt'), shell=True)
    # dri3 = webdriver.Firefox()
    # dri3.get("http://www.google.com/")
    # textarea3 = dri3.find_element_by_name("q")
    # textarea3.send_keys("webdriver")
    # submit_button3 = dri3.find_element_by_class_name("gNO89b")
    # time.sleep(1)
    # submit_button3.click()
    # dri3.quit()

    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd



def test_example(driver):
    # driver.switch_to_window(driver.current_window_handle)
    # driver.execute_script("window.focus();")
    driver.get("http://localhost/litecart/")
    # driver.find_element_by_name("username").send_keys("admin")
    # time.sleep(1)
    # driver.find_element_by_name("password").send_keys("admin")
    # time.sleep(2)
    # driver.find_element_by_xpath("//button[text()='Login']").click()
    time.sleep(2)
    pol = 1
    n = 0
    v = [1,2,3]
    # y = driver.find_element_by_css_selector("#box-popular-products > div"
    #                                         ).find_elements_by_css_selector("article")

    for x in v:
        y = driver.find_element_by_css_selector("#box-popular-products > div"
                                                ).find_elements_by_css_selector("article")
        time.sleep(2)
        y[n].click()
        time.sleep(2)
        try:
            driver.find_element_by_css_selector("#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.form-group.required > label")
            f = 1
        except NoSuchElementException:
            f = 0

        if f == 1:
            driver.find_element_by_css_selector(
                "#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.form-group.required > div > select").click()
            driver.find_element_by_xpath(
                "//*[@id='box-product']/div[1]/div[2]/div[5]/form/div[1]/div/select/option[2]").click()
        driver.find_element_by_css_selector(
            "#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.form-group > div > div:nth-child(2) > button").click()

        time.sleep(1)
        driver.find_element_by_css_selector("#header > a > img").click()
        print(n)
        n = n + 1
    time.sleep(1)
    driver.find_element_by_css_selector("#cart > a > img").click()
    time.sleep(3)
    yy = driver.find_element_by_css_selector("#box-checkout-cart > div > table > tbody"
                                            ).find_elements_by_css_selector("button")
    y1 = len(yy)
    print(y1)
    nn = 1
    for x1 in v:
        yy = driver.find_element_by_css_selector("#box-checkout-cart > div > table > tbody"
                                                 ).find_elements_by_css_selector("button")
        y1 = len(yy)
        print(y1)
        yy[1].click()
        time.sleep(1)
    time.sleep(3)

    for l in driver.get_log("browser"):
        print(l)
    driver.set_window_size(800, 600)
    driver.maximize_window()
    time.sleep(3)