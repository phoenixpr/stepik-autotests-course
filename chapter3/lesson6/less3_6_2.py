import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


# запуск pytest -s -v less3_6_2.py
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()



# передаём разные парамаетры - русский и англ язык в ссылку
@pytest.mark.parametrize('num_of_page', ["236895", "236896", '236897', '236898', '236899', '236903', '236904', '236905'])
def test_guest_should_see_login_link(browser, num_of_page):

    answer = str(math.log(int(time.time())))
    print('Считаем ответ...')
    link = f"https://stepik.org/lesson/{num_of_page}/step/1"
    print('Открываем страницу...')
    browser.get(link)
    input1 = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
    print('Ждём видимости элемента...')
    #= browser.find_element_by_tag_name('textarea')
    input1.send_keys(answer)
    print('отправляем ответ')
    button = browser.find_element_by_css_selector('.submit-submission')
    button.click()
    print('Нажимаем кнопку "отправить"...')
    corr_of_answer = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.smart-hints__feedback > pre.smart-hints__hint'))).text
    print(corr_of_answer)
    assert 'Correct!' in corr_of_answer
    print('Ожидаем "Correct!" в сообщении ответа')

