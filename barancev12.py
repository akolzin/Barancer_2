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
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    time.sleep(1)
    driver.find_element_by_name("password").send_keys("admin")
    time.sleep(2)
    driver.find_element_by_xpath("//button[text()='Login']").click()
    time.sleep(2)
    driver.find_element_by_link_text("Catalog").click()
    time.sleep(2)
    driver.find_element_by_css_selector("#content > div > div.panel-action > ul > li:nth-child(2) > a").click()
    time.sleep(1)
    driver.find_element_by_css_selector(
        "#tab-general > div > div:nth-child(1) > div:nth-child(1) > div > label:nth-child(1)").click()
    driver.find_element_by_css_selector("#category-id-0 > label > input[type=checkbox]").click()
    driver.find_element_by_css_selector("#categories > div:nth-child(2) > label > input[type=checkbox]").click()
    driver.find_element_by_css_selector("#tab-general > div > div:nth-child(1) > div:nth-child(4) > input").send_keys("10/04/2020")
    driver.find_element_by_css_selector("#tab-general > div > div:nth-child(1) > div:nth-child(5) > input").send_keys("10/05/2020")
    driver.find_element_by_css_selector("#tab-general > div > div:nth-child(2) > div:nth-child(1) > div > input").send_keys("11112")
    driver.find_element_by_css_selector("#tab-general > div > div:nth-child(2) > div:nth-child(2) > input").send_keys("qw112")
    driver.find_element_by_css_selector("#tab-general > div > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > input").send_keys("QW112")
    driver.find_element_by_css_selector("#tab-general > div > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > input").send_keys("11112111")
    driver.find_element_by_css_selector("#tab-general > div > div:nth-child(2) > div:nth-child(4) > div > select").click()
    driver.find_element_by_xpath("//*[@id='tab-general']/div/div[2]/div[4]/div/select/option[2]").click()
    time.sleep(2)

    driver.find_element_by_css_selector(
        "#images > div.new-images > div > div.input-group > input").send_keys("D:\\xampp\\htdocs\\litecart\\images\\products\\qw.jpg")
    time.sleep(3)
    # os.startfile(r'D:\\xampp\\htdocs\\litecart\\images\\products\\qw.jpg')
    #driver.execute_script("window.open('http://localhost/litecart/','_blank');")
    #driver.switch_to.window(driver.window_handles[1])
    # driver.get("http://localhost/litecart/")
    # driver.get("D:/xampp/htdocs/litecart/images/products/qw.jpg")
    #time.sleep(2)
    #e1 = driver.find_element_by_css_selector("#box-category-tree > ul > li > a")
    #e2 = driver.find_element_by_css_selector("#site-menu > div.navbar-header > form > div > input")
    #ActionChains(driver).move_to_element(e1).click_and_hold().move_to_element(e2).release().perform()
    #ActionChains(driver).drag_and_drop(e1, e2).perform()
    #time.sleep(4)
    #driver.close()
    #driver.switch_to.window(driver.window_handles[0])
    driver.find_element_by_link_text("Dock").click()
    time.sleep(2)
    y = driver.find_element_by_css_selector("#en").find_elements_by_css_selector("input")
    for x in y:
        x.send_keys("11112")
    time.sleep(2)
    yq = driver.find_element_by_css_selector("#en").find_elements_by_css_selector("textarea")
    for x in yq:
        x.send_keys("11112")
    driver.find_element_by_css_selector(
        "#en > div:nth-child(2) > div > div > div.trumbowyg-editor.trumbowyg-autogrow-on-enter").send_keys("11112")
    time.sleep(2)
    driver.find_element_by_link_text("Prices").click()
    time.sleep(2)
    n = 1
    yy = driver.find_element_by_css_selector("#prices").find_elements_by_css_selector("input")
    for x in yy:
        if n < 3:
            x.send_keys("11113")
            n = n + 1
        else:
            n = n + 1
    print(n)
    time.sleep(2)
    driver.find_element_by_css_selector("#content > div > div.panel-body > form > div.panel-action.btn-group > button:nth-child(1)").click()
    time.sleep(1)
    driver.find_element_by_link_text("Rubber Ducks").click()
    time.sleep(3)