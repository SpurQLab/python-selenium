from selenium import webdriver
from Pages.BasePage import BasePage
from Pages.calculatorpage import CalculatorPage


def before_all(context):
    context.driver = webdriver.Chrome("Resources/chromedriver.exe")
    context.driver.get("https://www.calculator.net/bmi-calculator.html")
    context.driver.maximize_window()
    basepage = BasePage(context.driver)
    context.calculatorPage = CalculatorPage(basepage)


def after_all(context):
    context.driver.close()
