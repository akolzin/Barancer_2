import pytest
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.google.com/")
    wait = WebDriverWait(driver, 10)  # seconds
    driver.find_element_by_class_name("hOoLGe").click()
    time.sleep(3)
    driver.find_element_by_name("q").send_keys("webdriver")
    time.sleep(2)
    #driver.find_element_by_name("q").clear()
    #driver.find_element_by_name("q").send_keys()
    for _ in range(9):driver.find_element_by_id("K8").click()
    time.sleep(2)
    for _ in range(3):driver.find_element_by_id("K49").click()
    driver.find_element_by_id("K50").click()
    driver.find_element_by_id("K51").click()
    time.sleep(2)
    driver.find_element_by_class_name("gNO89b").click()
    #submit_button = driver.find_element_by_class_name("gNO89b")
    time.sleep(3)
    #submit_button.click()
    time.sleep(3)
    wait.until(EC.title_is("11123 - Поиск в Google"))
    #WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))