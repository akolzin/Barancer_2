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
    v = [1,2,3]
    a = driver.find_elements_by_css_selector("#box-create-account > form > div")
    # for x in a:
    #     print(x)
    #     aa = x.find_elements_by_css_selector("div")
    #     for x1 in aa:
    #         print(x1.text)
    #         x1.find_element_by_css_selector("input").send_keys("11111")
    for x2 in v:
        driver.get("http://localhost/litecart/create_account")
        y = driver.find_element_by_css_selector("#box-create-account > form"
                                                ).find_elements_by_css_selector("input")#.send_keys("11111")
        print(y)
        print(len(y))
        del y[0]
        n = 1
        print(y)
        print(len(y))
        # ty = y[0].get_attribute("name")
        # print(ty)
        for x in y:
            if n != 14:
                if n != 9:
                    x.send_keys("11111")
                    #time.sleep(1)
                    n = n + 1
                else:
                    po = str(pol)
                    x.send_keys("1@",po)
                    n = n + 1
                    pol = pol + 1
            else:
                x.click()
        yy = driver.find_element_by_css_selector("#box-create-account > form"
                                                 ).find_elements_by_css_selector("select")#.send_keys("11111")
        print(yy)
        print(len(yy))
        time.sleep(1)
        yy[0].click()
        time.sleep(2)
        # yu = driver.find_element_by_css_selector("#box-create-account > form"
        #                                          ).find_elements_by_css_selector("option")#.send_keys("11111")
        # print(len(yu))
        # for x1 in yu:
        #     if x1.text == "United States":
        #         x1.click()
        driver.find_element_by_xpath("//*[@id='box-create-account']/form/div[5]/div[1]/div/select/option[230]").click()
        y[10].click()
        time.sleep(2)
        driver.find_element_by_css_selector("#box-create-account > form > div.btn-group > button").click()
        #y[0].send_keys("11111")
        time.sleep(2)
        driver.find_element_by_css_selector("#default-menu > ul.nav.navbar-nav.navbar-right > li.account.dropdown > a").click()
        time.sleep(2)
        driver.find_element_by_link_text("Logout").click()
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    time.sleep(1)
    driver.find_element_by_name("password").send_keys("admin")
    time.sleep(2)
    driver.find_element_by_xpath("//button[text()='Login']").click()
    time.sleep(2)
    driver.find_element_by_link_text("Customers").click()
    time.sleep(2)
    for x3 in v:
        driver.find_element_by_css_selector(
            "#content > div > div.panel-body > form > table > tbody > tr:nth-child(1) > td:nth-child(8)").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#content > div > div.panel-body > form > div > div.col-md-8 > div.panel-action.btn-group > button:nth-child(3)").click()
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
    #y.send_keys("11111")
    #ActionChains(driver).move_to_element(500).click_and_hold().move_to_element(800).release().perform()