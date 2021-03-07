from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
import time

# setup to initialize from cache
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=Users\\hammad\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
options.add_argument('--profile-directory=Default')

# initializing Chrome Driver
chromeBrowser = webdriver.Chrome(executable_path='F:\\webdriver\\chromedriver', options=options)

# launching whatsapp site
chromeBrowser.get('https://web.whatsapp.com/')

# console guide
print(" [-] scan the QR code with 15 sec \n [-] If u miss the time, restart the program")
time.sleep(15)


def find_user(username):
    print('[-] find user fnc start')
    searchbox = chromeBrowser.find_element_by_xpath('//div[@contenteditable=\'true\']')
    searchbox.click()
    searchbox.send_keys(username)
    time.sleep(1.2)
    selectuser = chromeBrowser.find_elements_by_xpath('//*[text()=\'{}\'][1]'.format(username))
    print(selectuser)
    selectuser = selectuser[1]
    time.sleep(1)
    selectuser.click()
    fetch_msg(user_name)
    print('[-] find user fnc end')


def msg_box():
    print(' [-] inside msgbox func\n')


def fetch_msg(username):
    print('[-] fetch msg fnc start')
    lastmsg = chromeBrowser.find_elements_by_xpath(
        "//div[contains(@data-pre-plain-text,'{}:')]//div[@class='eRacY']//span".format(username))
    for i in range(len(lastmsg)):
        print(lastmsg[i].text)
    print('[-] fetch msg fnc end')


# Loop to fetch and forward messages
while 1 < 2:
    try:
        user_name = 'Ma boy'
        user = chromeBrowser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
        fetch_msg(user_name)
    except (NoSuchElementException, StaleElementReferenceException):
        find_user(user_name)

    print('======= AFTER EXCEPT ========')
    time.sleep(5)
