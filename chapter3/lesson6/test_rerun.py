'''Рассмотрим еще одну проблему, такие тесты, которые по независящим от нас внешним обстоятельствам или из-за трудновоспроизводимых багов,
могут иногда падать, хотя всё остальное время они проходят успешно. Vы будем перезапускать упавший тест, чтобы еще раз убедиться,
что он действительно нашел баг, а не упал случайно. Для этого мы будем использовать плагин pytest-rerunfailures
Чтобы указать количество перезапусков для каждого из упавших тестов, нужно добавить в командную строку параметр:
"--reruns n", где n - это количество перезапусков.
pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py'''

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")
