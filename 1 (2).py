import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
st = browser.find_element(By.NAME, "first_name")
st.send_keys("st")
button = browser.find_element(By.ID, "submit_button")
button.click()
time.sleep(8)
# закрываем браузер после всех манипуляций
#browser.quit()

# 22.28183198718841