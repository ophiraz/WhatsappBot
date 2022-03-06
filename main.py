from selenium import webdriver
import time
from datetime import datetime
import random

#names of people you want to send the message to
chat_name = ["אלון", "אני עם אצמי","יעל יחידת מחלימים"]
#list of messages, one message will be randomly sent from this
messages = ["בוקר טוב! אני בבית היום", "היי יעל, אני בבית היום", "אני בבית היום", "היי יעל, בוקר טוב! אני בבית היום...", "בוקר טוב יעל, אני בבית"]
#list of times you want the message to be sent
timeToSend = ['09:00 AM']

class WhatsAppBot():
    def __init__(self):
       #initialize the driver and open chrome
       self.driver = webdriver.Chrome()

    def login(self):
        # open the web.whatsapp website
        self.driver.get("https://web.whatsapp.com/")
        print("Please scan QRO nce")
        # wait until the user scans the QR code
        while True:
            try:
                # look for the chat search bar (check Inspect Element                   section to understand this line)
                searchBox = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]")

                print("Scanning Successful")
                # if search box is available then the user has Successfully scanned the QR so break
                break
            except Exception as e:

                pass  # seach box was not found, still waiting for user
            # check if the search box is available, every 1 second
            time.sleep(1)

    def searchChat(self, name):
        # locate the search box
        searchBox = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]")

        # type in the required person’s name
        searchBox.send_keys(name)

        # wait for 1 second to make sure everything renders properly
        time.sleep(1)

    def sendMessage(self, name):
        # look for the required chat name
        chat = self.driver.find_element_by_xpath(" // span[ @ title ='{}']".format(name))
        # click on the particular chat
        chat.click()
        # select the typing area/ chat box
        chatBox = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
        # type in the required message
        chatBox.send_keys(random.choice(messages))
        # wait for 1 second to make sure that the send button renders
        time.sleep(1)
        # search the send button
        sendButton = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button")
        # click the send button

        sendButton.click()

def main():
    bot = WhatsAppBot()
    bot.login()
    lock = 0

    while True:
        # if the current time is in alarm time then send
        if (datetime.now().strftime("%H:%M %p") in timeToSend and lock == 0):
            lock = 1
            for i in chat_name:
                bot.searchChat(i)
                bot.sendMessage(i)
                time.sleep(2)
        # if current time is not in alarm time then release the lock
        elif (datetime.now().strftime("%H:%M %p") not in timeToSend):
            lock = 0
        # check every 25 seconds if current time matches alarm time
        time.sleep(25)

if(__name__ == "__main__"):
    main()