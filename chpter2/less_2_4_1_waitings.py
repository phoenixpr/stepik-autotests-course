import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/explicit_wait2.html")

# ищем кнопку
button = driver.find_element_by_tag_name("button")

#ждём пока появится текст 100
waiting_for_price = WebDriverWait(driver, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

button.click()

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
button_1 = driver.find_element_by_id("solve").click()

assert True
