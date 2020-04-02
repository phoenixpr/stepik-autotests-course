import time, math

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/alert_accept.html")
#time.sleep(5)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем кнопку по тегу и кликаем на неё
button = driver.find_element_by_tag_name("button").click()

# переключаемся на окно алерта и кликаем
alert = driver.switch_to.alert
alert.accept()

# находим число на странице (забираем текст с числом)
x_element = driver.find_element_by_id("input_value")
x = x_element.text

# вычисляем х
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему
# Ищем поле для ввода формулы
answer_inp = driver.find_element_by_id("answer")

# отправляем ответ
answer_inp.send_keys(y)
button_1 = driver.find_element_by_tag_name("button").click()
