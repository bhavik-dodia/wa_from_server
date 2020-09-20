import os
import sys
import time
import requests
# import winclip32
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains

def send_data(users, url, msg=''):

    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("user-data-dir=C:\\Users\\BHAVIK DODIA\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")

    # opens the chrome browser
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)

    # opens WhatsApp Web in browser
    driver.get('http://web.whatsapp.com')

    response = requests.get(url)

    # output = BytesIO()
    # Image.open(BytesIO(response.content)).convert('RGB').save(output, 'BMP')
    # winclip32.set_clipboard_data(winclip32.BITMAPINFO_STD_STRUCTURE, output.getvalue()[14:])

    time.sleep(30)

    # sends multiple messages to a single user
    try:
        for user in users:
            profile = driver.find_element_by_xpath(f'//span[@title = "{user}"]')
            profile.click()

            time.sleep(0.5)

            ActionChains(driver).key_down(keys.Keys.CONTROL).send_keys('v').key_up(keys.Keys.CONTROL).perform()

            time.sleep(2)

            msg_box = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]')
            msg_box.send_keys(msg)
            time.sleep(0.5)
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div').click()

    except Exception as e:
        res = str(e)
    else:
        res = 'Message(s) sent successfully...'

    # input('close chrome? ')

    # closes the browser
    time.sleep(5)
    driver.close()
    return res
