import behave_webdriver
import os
import re
import time
from behave_webdriver.driver import ChromeOptions
from os.path import expanduser

def save_screenshot(context, step):
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%S")
    filename = re.sub('\W', '-', '{} failed {}'.format(timestamp,
                                                       str(step.name)))
    filepath = os.path.join('screenshots', filename + '.png')
    if not os.path.exists('screenshots'):
        os.mkdir('screenshots')

    print('Saving screenshot to %s' % filepath)
    context.behave_driver.save_screenshot(filepath)


def before_all(context):
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    context.behave_driver = behave_webdriver.Chrome(
        chrome_options=chrome_options,
        executable_path='./features/chromedriver/chromedriver'
    )


def after_all(context):
    context.behave_driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        save_screenshot(context, step)