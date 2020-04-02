import time, os

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(2)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/selects1.html")
#time.sleep(5)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем первое число
firstNum_element = driver.find_element_by_id("num1")
firstNum = firstNum_element.text # текст возвращается как строка
print(firstNum)

# Ищем поле для ввода текста
secondNum_element = driver.find_element_by_id("num2")
secondNum = secondNum_element.text # текст возвращается как стока
print(secondNum)

answer = int(firstNum) + int(secondNum)

# выбираем выпадающий список и кликаем по нему
driver.find_element_by_tag_name("select").click()

# выбираем нужны ответ и кликаем
driver.find_element_by_css_selector("[value='{}']".format(answer)).click()

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".btn-default")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
#time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
#driver.quit()
