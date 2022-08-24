from behave import *

use_step_matcher("re")


@when("User Enters Age (?P<value>.*)")
def step_impl(context, value):
    context.calculatorPage.clear_and_input_element("//input[@class='inhalf']", value)

@step("User clicks on Gender Male")
def step_impl(context):
    context.calculatorPage.click_element("//label[normalize-space()='Male'][1]")

@step("User Enters Height (?P<value>.*)")
def step_impl(context, value):
    context.calculatorPage.clear_and_input_element("(//input[@id='cheightmeter'])[1]", value)

@step("User Enters Weight (?P<value>.*)")
def step_impl(context, value):
    context.calculatorPage.clear_and_input_element("(//input[@id='ckg'])[1]", value)

@step("User clicks on Calculate button")
def step_impl(context):
    context.calculatorPage.click_element("//input[@value='Calculate']")

@then("User verify the result (?P<total>.*)")
def step_impl(context, total):
    result = context.calculatorPage.verify_result()
    print(f'****{result}***')
    print(f'*****{total}***')
    assert result == total
#
# @given("user is on bmi calculator page")
# def step_impl(context):
#     context.driver = webdriver.Chrome("C://Users//ANKITA//Downloads//chromedriver.exe")
#     context.driver.get("https://www.calculator.net/bmi-calculator.html")
#     context.driver.maximize_window()
#
# @when("Enters Age 35")
# def step_impl(context):
#     context.driver.find_element("xpath", "//input[@class='inhalf']").send_keys(35)
#     sleep(2)
#
#
#
# @step("User Enters Height 160")
# def step_impl(context):
#     context.driver.find_element("xpath", "(//input[@id='cheightmeter'])[1]").send_keys(160)
#     sleep(2)
#
# @step("User Enters Weight 55")
# def step_impl(context):
#     context.driver.find_element("xpath", "(//input[@id='ckg'])[1]").send_keys(60)
#     sleep(2)
#
#
# @then("User verify the result 21\.5")
# def step_impl(context):
#     result = driver.find_element("xpath", "(//div[@class='bigtext'])[1]").text
#
# @when("Enters Age 50")
# def step_impl(context):
#         context.driver.find_element("xpath", "//input[@class='inhalf']").send_keys(35)
#         sleep(2)
#
#
# @step("User Enters Height 175")
# def step_impl(context):
#     context.driver.find_element("xpath", "(//input[@id='cheightmeter'])[1]").send_keys(160)
#     sleep(2)
#
#
#
# @step("User Enters Weight 65")
# def step_impl(context):
#     context.driver.find_element("xpath", "(//input[@id='ckg'])[1]").send_keys(60)
#     sleep(2)
# s
#
#
#
# @then("User verify the result 21\.2")
# def step_impl(context):
#     result = driver.find_element("xpath", "(//div[@class='bigtext'])[1]").text
#
#
# @when("Enters Age 45")
# def step_impl(context):
#     context.driver.find_element("xpath", "//input[@class='inhalf']").send_keys(35)
#     sleep(2)
#
#
# @step("User Enters Height 150")
# def step_impl(context):
#     context.driver.find_element("xpath", "(//input[@id='cheightmeter'])[1]").send_keys(160)
#     sleep(2)
#
#
# @step("User Enters Weight 52")
# def step_impl(context):
#     context.driver.find_element("xpath", "(//input[@id='ckg'])[1]").send_keys(60)
#     sleep(2)
#
#
# @then("User verify the result 23\.1")
# def step_impl(context):
#     result = driver.find_element("xpath", "(//div[@class='bigtext'])[1]").text