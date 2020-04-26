import time, math

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/get_attribute.html")
#time.sleep(5)

# находим картинку, забираем значение из АТРИБУТА valuex
x_element = driver.find_element_by_css_selector("img#treasure")
x = x_element.get_attribute("valuex")

# вычисляем х
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему
# Ищем поле для ввода формулы
answer_inp = driver.find_element_by_id("answer")

# отправляем ответ
answer_inp.send_keys(y)

# ищем чекбокс и кликаем
checkbox_inp = driver.find_element_by_id("robotCheckbox")
checkbox_inp.click()

# ищем радиокнопку и кликаем на нужное
radio_inp = driver.find_element_by_id("robotsRule")
radio_inp.click()

# отправляем ответ
submit_btn = driver.find_element_by_css_selector(".btn-default")
submit_btn.click()
