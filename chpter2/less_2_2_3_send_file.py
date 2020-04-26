import time, os

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/file_input.html")
#time.sleep(5)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
firstName = driver.find_element_by_css_selector("input[name='firstname']")

# Напишем текст ответа в найденное поле
firstName.send_keys("A")
#.sleep(5)

# Ищем поле для ввода текста
lastName = driver.find_element_by_css_selector("input[name='lastname']")

# Напишем текст ответа в найденное поле
lastName.send_keys("A")
#time.sleep(5)

# Ищем поле для ввода текста
email = driver.find_element_by_css_selector("input[name='email']")

# Напишем текст ответа в найденное поле
email.send_keys("A@q.ru")
#time.sleep(5)

# Ищем кнопку для отправки документа
button = driver.find_element_by_id("file")

# Напишем текст ответа в найденное поле

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))

# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'less_2_2.txt')

# отправляем ответ
button.send_keys(file_path)
#time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".btn-primary")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
#time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
#driver.quit()
