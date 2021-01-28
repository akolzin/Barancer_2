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


@pytest.fixture
def driver(request):
    #wd1 = webdriver.Ie("C:\\tools\\IEDriverServer.exe")
    #wd = webdriver.Firefox()
    #wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Firefox Nightly\\firefox.exe")
    #wd = webdriver.Edge()
    wd = webdriver.Chrome()
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
    t = driver.find_element_by_css_selector(
        "#box-campaign-products > div > article > a > div.info > div.name").text
    print(t)
    href = driver.find_element_by_css_selector("#box-campaign-products > div > article > a").get_attribute("href")
    print(href)
    driver.execute_script("window.open('http://yandex.ru/','_blank');")
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.get(href)
    time.sleep(1)
    t1 = driver.find_element_by_css_selector(
        "#box-product > div.row > div.col-sm-8.col-md-6 > h1").text
    print(t1)
    if t == t1:
        print("yes")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    o = driver.find_element_by_css_selector(
        "#box-campaign-products > div > article > a > div.info > div.price-wrapper > del").value_of_css_property("color")
    print(o)
    text_file1 = open('C:\\Users\\exe90\\Desktop\\site\\site\\6.txt', 'w')
    text_file1.write(o)
    a = driver.find_element_by_css_selector(
        "#box-campaign-products > div > article > a > div.info > div.price-wrapper > strong").value_of_css_property("color")
    print(a)
    text_file1 = open('C:\\Users\\exe90\\Desktop\\site\\site\\6.txt', 'a')
    text_file1.write(a)

    oa = driver.find_element_by_css_selector(
        "#box-campaign-products > div > article > a > div.info > div.price-wrapper").text
    print(oa)
    text_file1 = open('C:\\Users\\exe90\\Desktop\\site\\site\\6.txt', 'a')
    text_file1.write(oa)

    so = driver.find_element_by_css_selector(
        "#box-campaign-products > div > article > a > div.info > div.price-wrapper > del").size
    print(so)
    # so1 = str(so)
    # text_file1 = open('C:\\Users\\exe90\\Desktop\\site\\site\\6.txt', 'a')
    # text_file1.write(so1)
    sa = driver.find_element_by_css_selector(
        "#box-campaign-products > div > article > a > div.info > div.price-wrapper > strong").size
    print(sa)
    # sa1 = str(sa)
    # text_file1 = open('C:\\Users\\exe90\\Desktop\\site\\site\\6.txt', 'a')
    # text_file1.write(sa1)

    if so != sa:
        print("yes")

    do = driver.find_element_by_css_selector(
        "#box-campaign-products > div > article > a > div.info > div.price-wrapper > del"
        ).value_of_css_property("text-decoration-line")
    print(do)
    text_file1 = open('C:\\Users\\exe90\\Desktop\\site\\site\\6.txt', 'a')
    text_file1.write(do)
    da = driver.find_element_by_css_selector(
        "#box-campaign-products > div > article > a > div.info > div.price-wrapper > strong"
        ).value_of_css_property("font-weight")
    print(da)
    text_file1 = open('C:\\Users\\exe90\\Desktop\\site\\site\\6.txt', 'a')
    text_file1.write(da)

    #
    driver.execute_script("window.open('http://yandex.ru/','_blank');")
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.get(href)
    time.sleep(1)

    o = driver.find_element_by_css_selector(
        "#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.price-wrapper > del"
        ).value_of_css_property("color")
    print(o)
    text_file1 = open('C:\\Users\\exe90\\Desktop\\site\\site\\7.txt', 'w')
    text_file1.write(o)
    a = driver.find_element_by_css_selector(
        "#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.price-wrapper > strong"
        ).value_of_css_property("color")
    print(a)
    text_file1 = open('C:\\Users\\exe90\\Desktop\\site\\site\\7.txt', 'a')
    text_file1.write(a)

    oa = driver.find_element_by_css_selector(
        "#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.price-wrapper").text
    print(oa)
    text_file1 = open('C:\\Users\\exe90\\Desktop\\site\\site\\7.txt', 'a')
    text_file1.write(oa)

    so = driver.find_element_by_css_selector(
        "#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.price-wrapper > del").size
    print(so)
    # so1 = str(so)
    # text_file1 = open('C:\\Users\\exe90\\Desktop\\site\\site\\6.txt', 'a')
    # text_file1.write(so1)
    sa = driver.find_element_by_css_selector(
        "#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.price-wrapper > strong").size
    print(sa)
    # sa1 = str(sa)
    # text_file1 = open('C:\\Users\\exe90\\Desktop\\site\\site\\6.txt', 'a')
    # text_file1.write(sa1)

    if so != sa:
        print("yes")

    do = driver.find_element_by_css_selector(
        "#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.price-wrapper > del"
        ).value_of_css_property("text-decoration-line")
    print(do)
    text_file1 = open('C:\\Users\\exe90\\Desktop\\site\\site\\7.txt', 'a')
    text_file1.write(do)
    da = driver.find_element_by_css_selector(
        "#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.price-wrapper > strong"
        ).value_of_css_property("font-weight")
    print(da)
    text_file1 = open('C:\\Users\\exe90\\Desktop\\site\\site\\7.txt', 'a')
    text_file1.write(da)
    time.sleep(2)
    text_file1.close()
    text_file2 = open(r"C:\\Users\\exe90\\Desktop\\site\\site\\6.txt", "r")
    ed = text_file2.readline()
    print(ed)
    text_file3 = open(r"C:\\Users\\exe90\\Desktop\\site\\site\\7.txt", "r")
    ed1 = text_file3.readline()
    print(ed1)

    if ed == ed1:
        print("good")
