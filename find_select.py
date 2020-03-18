from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector("#num1").text
    y = browser.find_element_by_css_selector("#num2").text
    sum = int(x) + int(y)

    select = Select(browser.find_element_by_css_selector(".custom-select"))

    select.select_by_value(f"{str(sum)}")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
