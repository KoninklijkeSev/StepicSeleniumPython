from selenium import webdriver
import time
import os
try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    name = browser.find_element_by_name("firstname")
    name.send_keys("Mikhail")
    last = browser.find_element_by_name("lastname")
    last.send_keys("Sever")
    email = browser.find_element_by_name("email")
    email.send_keys("fake@fake.fake")
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    browser.find_element_by_class_name("btn.btn-primary").click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла