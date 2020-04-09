from selenium import webdriver
import time
import math
try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    browser.find_element_by_class_name("btn.btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_text = browser.find_element_by_id("input_value")
    x = x_text.text
    y = int(x)
    print(y)
    x = y

    def calc(x):
        return str(math.log(abs(12 * math.sin(x))))
    y = calc(x)
    print(y)

    browser.execute_script("window.scrollBy(0, 100);")
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    browser.find_element_by_class_name("btn.btn-primary").click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла