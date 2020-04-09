from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    x = browser.find_element_by_id("num1")
    num1 = x.text
    y = browser.find_element_by_id("num2")
    num2 = y.text
    sum = str(int(num1) + int(num2))
    browser.find_element_by_class_name("custom-select").click()
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)
    print(sum)

    browser.find_element_by_class_name('btn.btn-default').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла