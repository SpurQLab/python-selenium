from time import sleep

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class CalculatorPage:
    def __init__(self, context):
        self.context = context
        BasePage.__init__(self, context.driver)

    def click_element(self, element: str):
        self.driver.find_element("xpath", element).click()
        sleep(2)

    def clear_and_input_element(self, element: str, value: int):
        element = self.driver.find_element("xpath", element)
        element.clear()
        element.send_keys(value)
        sleep(2)

    def verify_result(self):
        result = self.driver.find_element("xpath", "(//div[@class='bigtext'])[1]").text
        # print(result)
        index1 = result.index("=")
        index2 = result.index("(")
        actual_result = result[index1 + 1:index2]
        # print(actual_result)
        return actual_result.replace('kg/m2', '').replace(' ', '')
