from selenium import webdriver
import unittest



class test_class_Abs(unittest.TestCase):

    link = "http://suninjuly.github.io/registration1.html"
    link1 = "http://suninjuly.github.io/registration2.html"
    input1 = 'input[placeholder="Input your first name"]'
    input2 = 'input[placeholder="Input your last name"]'
    input3 = 'input[placeholder="Input your email"]'
    button = "button.btn"
    welcome_text = "Congratulations! You have successfully registered!"


    def test_abs1(self):
        self.browser = webdriver.Chrome()
        self.link = test_class_Abs.link
        self.browser.get(self.link)
        # надо обращаться к переменным класса через его имя как self.browser.get(test_class_Abs.input)
        self.input1 = self.browser.find_element_by_css_selector(test_class_Abs.input1)
        self.input1.send_keys("Ivan")
        self.input2 = self.browser.find_element_by_css_selector(test_class_Abs.input2)
        self.input2.send_keys("Petrov")
        self.input3 = self.browser.find_element_by_css_selector(test_class_Abs.input3)
        self.input3.send_keys("silencio")
        self.button = self.browser.find_element_by_css_selector(test_class_Abs.button)
        self.button.click()
        self.assertEqual("Congratulations! You have successfully registered!", test_class_Abs.welcome_text)

    def test_abs2(self):
        self.browser = webdriver.Chrome()
        self.link = test_class_Abs.link1
        self.browser.get(self.link)
        self.input1 = self.browser.find_element_by_css_selector(test_class_Abs.input1)
        self.input1.send_keys("Ivan")
        self.input2 = self.browser.find_element_by_css_selector(test_class_Abs.input2)
        self.input2.send_keys("Petrov")
        self.input3 = self.browser.find_element_by_css_selector(test_class_Abs.input3)
        self.input3.send_keys("silencio")
        self.button = self.browser.find_element_by_css_selector(test_class_Abs.button)
        self.button.click()
        self.assertEqual("Congratulations! You have successfully registered!", test_class_Abs.welcome_text)


if __name__ == "__main__":
    unittest.main()

