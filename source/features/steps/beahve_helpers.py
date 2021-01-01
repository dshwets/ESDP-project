from selenium.common.exceptions import NoSuchElementException


def check_element_not_exists(context, xpath: str):
    try:
        context.behave_driver.find_element_by_xpath(xpath)
        raise Exception('Element was founded')
    except NoSuchElementException:
        pass
