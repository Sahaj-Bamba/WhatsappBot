from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import gtts
import random
import json

data = ""
with open('configuration.json') as f:
    data = json.load(f)

# configurations

keywords = data['keywords']
msgs = data['replies']
fixedReply = data['fixedReply']
count = 1
unreadClass = "OUeyt"
sendButtonClass = "_35EW6"
msgBoxClass = "_2WovP"
textClass = "_3FXB1 selectable-text invisible-space copyable-text"
dirPath = os.path.dirname(os.path.realpath(__file__))
driver = webdriver.Chrome(dirPath+"\chromedriver.exe")
driver.get("https://web.whatsapp.com/")


def run():
    if (openUnread()):
        if (isHappyBirthday()):
            sendMessage()
    if (isHappyBirthday()):
        sendMessage()


def main():
    run()


def openUnread():
    try:
        time.sleep(0.1)
        xpath = '//span[@class="{}"]'.format(unreadClass)
        user = driver.find_element_by_xpath(xpath)

        user = user.find_element_by_xpath('..')
        user = user.find_element_by_xpath('..')
        user = user.find_element_by_xpath('..')
        user = user.find_element_by_xpath('..')

        user.click()
        time.sleep(0.1)

        return True
    except:
        return False


def isHappyBirthday():
    try:
        xpath = '//span[@class="{}"]'.format(textClass)
        eles = driver.find_elements_by_xpath(xpath)
        str = eles[-1].text
        for s in keywords:
            if (s in str.lower()):
                return True
        return False
    except:
        return False


def sendMessage():
    msg_box = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, msgBoxClass)))
    msg_box.send_keys(msgs[random.randrange(len(msgs))] + fixedReply)
    button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, sendButtonClass)))
    driver.implicitly_wait(0.25)
    button.click()
    time.sleep(0.25)


while (True):
    main()
