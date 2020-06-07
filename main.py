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
prevReplyTo = "killer"
keywords = data['keywords']
msgs = data['replies']
fixedReply = data['fixedReply']
count = 1
unreadClass = "_31gEB"
sendButtonClass = "_1U1xa"
msgBoxClass = "_3uMse"
textClass = "_3Whw5 selectable-text invisible-space copyable-text"
replyNameClass = "FMlAw FdF4z _3Whw5"
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
    try:
        replyTo = getReplyTo()
        # try:
        #     replyTo = getReplyTo()
        # print(replyTo)
        # print(prevReplyTo)
        # if (replyTo == prevReplyTo):
        #     replyTo = "killer"
        # except:
        #     print("er")
        #     pass
        replyText = ""
        if (replyTo != "killer"):
            replyText = "@"+replyTo+" "
            prevReplyTo = replyTo
        print(replyText)
        msg_box = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, msgBoxClass)))
        msg_box.send_keys(
            replyText + msgs[random.randrange(len(msgs))])
        button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CLASS_NAME, sendButtonClass)))
        driver.implicitly_wait(0.025)
        button.click()
        time.sleep(0.025)
        msg_box.send_keys(fixedReply)
        button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CLASS_NAME, sendButtonClass)))
        driver.implicitly_wait(0.025)
        button.click()
        time.sleep(0.025)
    except:
        # print("ex")
        return


def getReplyTo():
    try:
        xpath = '//span[@class="{}"]'.format(replyNameClass)
        user = driver.find_elements_by_xpath(xpath)
        user = user[-1]
        return user.text
    except:
        return "killer"


while (True):
    main()
