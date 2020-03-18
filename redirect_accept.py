from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(2)
    browser.find_element_by_css_selector("button.trollface").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()

finally:
    time.sleep(15)
    browser.quit()
