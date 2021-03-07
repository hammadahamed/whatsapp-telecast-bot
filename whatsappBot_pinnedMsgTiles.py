from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import os

# configuring browser options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-infobars')
chrome_options.add_experimental_option("prefs", {'profile.default_content_setting_values.notifications': 0})
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--user-data-dir=Users\\hammad\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
chrome_options.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(executable_path='F:\\webdriver\\chromedriver', options=chrome_options)

# user names
group1 = 'test1'
group2 = 'test2'
sender_name = 'MoM'
messages = []
new_messages = []


# initializing and executing chrome
def launch_page():

    driver.get('https://web.whatsapp.com')


def forward_message(prev):
    user_select = driver.find_element_by_xpath("//span[@title='{}']".format(group1))
    user_select.click()
    # time.sleep(0.2)

    # checking for new msg
    # new msg tile -class name  -> iBZ7z
    try:
        new_msg = driver.find_element_by_xpath("//span[@class='iBZ7z']").text
        if new_msg.endswith('UNREAD MESSAGES') or new_msg.endswith('UNREAD MESSAGE'):

            split_text = new_msg.split()
            no_of_msgs = int(split_text[0])
            print('\n [+] Found {} new messages  !!!!!!!!!!!!!!!!!!'.format(no_of_msgs))

            # collecting the msgs from sender
            msg_list = driver.find_elements_by_xpath("//div[contains(@data-pre-plain-text,'{}:')]//div[@class='eRacY']//span[@dir='ltr']//span".format(sender_name))
            # extracting the text from UI elements
            print(msg_list)
            for i in range(len(msg_list)):
                # print(msg_list[i].text)
                messages.append(msg_list[i].text)
            print(messages)

            # filtering the $new-messages from the $message list
            new_messages = messages[(len(messages) - no_of_msgs):]
            print('\n1:')
            print(prev)
            print(new_messages)
            x = new_messages
            # checking for duplicate new messages
            if len(prev) > 0:
                for e in prev:
                    for ee in new_messages:
                        if e == ee:
                            new_messages[new_messages.index(ee)] = ';;;;;'

            print('\n2:')
            # print(x)
            prev = x
            print(new_messages)
            print(x)
            print(prev)

            # sending the messages to the other group via function
            send_to_group2(new_messages)
            # prev = new_messages
            return prev

    except NoSuchElementException:
        # send_to_group2("hello")
        print(' NO NEW MESSAGES ! ')
        return 0


def send_to_group2(newmsgs):
    user_select = driver.find_element_by_xpath("//span[@title='{}']".format(group2))
    user_select.click()

    # message box
    msg_box = driver.find_element_by_xpath("//*[@id=\"main\"]/footer/div[1]/div[2]/div")
    send_button = driver.find_element_by_xpath("//*[@id=\"main\"]/footer/div[1]/div[3]")

    # send button class name --> _2r1fJ ---  but that didnt work
    for k in range(len(newmsgs)):
        if newmsgs[k] != ';;;;;':
            msg_box.click()
            print("after replacement -- list -->  " + newmsgs[k])

            for parts in newmsgs[k].split('\n'):
                msg_box.send_keys(parts)
                ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(
                    Keys.ENTER).perform()

            send_button.click()
            print("\n [-] Sent message{} to Group 2 \n -------> {} <-------".format(k, newmsgs[k]))


def select_group2():
    user_select = driver.find_element_by_xpath("//span[@title='{}']".format(group2))
    user_select.click()


def main_algorithm():

    launch_page()
    time.sleep(15)
    check = 1
    prev = []

    while 1 == 1:
        print("\n [$] CHECK {}".format(check))
        x = forward_message(prev)
        if x != 0: prev = x
        select_group2()
        time.sleep(5)
        check += 1



try:
    main_algorithm()

except StaleElementReferenceException as error:
    print(" \n[-] ERROR OCCURRED")
    print(error.__class__)
    time.sleep(0.5)

    print(" [-] Reloading page and Retrying now...")
    time.sleep(0.5)
    launch_page()
    main_algorithm()

except NoSuchElementException as error:
    print(" [-] ERROR OCCURRED \n [-] error type : {} \n [-] Trying again... Please wait..".format(error))
    time.sleep(3)
    main_algorithm()





