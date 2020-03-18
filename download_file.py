from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys("Anna")

    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Brown")

    email = browser.find_element_by_name("email")
    email.send_keys("anna@co.uk")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.rtf')           # добавляем к этому пути имя файла
    browser.find_element_by_css_selector('#file').send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()