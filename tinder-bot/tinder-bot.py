from selenium import webdriver
from time import sleep

from fb_creds import username, password

def bot():
    bot = webdriver.Chrome()
    bot.get('https://tinder.com')
    sleep (5)

    fb_button = bot.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
    fb_button.click()
    
    tinder_window = bot.window_handles[0]
    
    # login with Facebook
    fb_login_window = bot.switch_to.window(bot.window_handles[-1])
    fb_mail = bot.find_element_by_xpath('//*[@id="email"]')
    fb_mail.send_keys(username)
    
    fb_password = bot.find_element_by_xpath('//*[@id="pass"]')
    fb_password.send_keys(password)
    
    fb_login_button = bot.find_element_by_xpath('//*[@id="loginbutton"]')
    fb_login_button.click()
    sleep (5)

    # closing tinder popups
    bot.switch_to.window(tinder_window)

    tinder_loc = bot.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    tinder_loc.click()
    tinder_notify = bot.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
    tinder_notify.click()
    sleep (5)

    while True:
        sleep (1)
        try:
            like = bot.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
            like.click()
            print ('liked!')
        except:
            try:
                bot.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]').click()
            except:
                print ('fatt gya')
login()
