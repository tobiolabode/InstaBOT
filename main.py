from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import random
import sys
# TODO:
# itergrate loop with close brower
# add come back at x time feature


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrower(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(5)
        login_button = driver.find_element_by_xpath(
            "//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(5)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def unfollow(self):
        driver = self.driver
        driver.get("https://www.instagram.com/tobi.olabode/")
        time.sleep(3)
        #/html/body/span/section/main/div/header/section/ul/li[3]/a
        following_button = driver.find_element_by_xpath(
            "/html/body/span/section/main/div/header/section/ul/li[3]/a")
        following_button.click()
        time.sleep(5)

        unfollower_count = 0
        for _ in range(20):
            print(">>> Starting loop:", _)
            try:
                while True:
                    # 20 unfollow limit
                    if unfollower_count == 20:
                        print("------------------\n Closed to avoid dupicate unfollow loops\n------------------")
                        self.closeBrower()
                        sys.exit()
                    #print("attempt number:", attempt)
                    driver.find_element_by_xpath(
                        "/html/body/span/section/main/div/header/section/ul/li[3]/a").click()
                    time.sleep(3)
                    # follow_button
                    driver.find_element_by_xpath(
                        "/html/body/div[3]/div/div/div[2]/ul/div/li[1]/div/div[2]/button").click()
                    time.sleep(3)
                    # unfollow_button
                    driver.find_element_by_xpath(
                        "/html/body/div[4]/div/div/div/div[3]/button[1]").click()
                    unfollower_count += 1
                    print(">>> Unfollowed")
                    time.sleep(3)
                    # follow_button2
                    driver.find_element_by_xpath(
                        "/html/body/div[3]/div/div/div[2]/ul/div/li[2]/div/div[2]/button").click()
                    time.sleep(3)
                    # unfollow_button
                    driver.find_element_by_xpath(
                        "/html/body/div[4]/div/div/div/div[3]/button[1]").click()

                    unfollower_count += 1
                    print(">>> Unfollowed")
                    time.sleep(3)
                    print(">>> Waiting 3 secs")
                    print(">>>Refreshing")
                    driver.refresh()
                    print(">>> Waiting 5 secs")
                    time.sleep(5)
                    print(">>> you have unfollowed {} number of people".format(unfollower_count))
            except Exception:
                print(">>> Refreshing, Exception Occured ")
                driver.refresh()
                time.sleep(5)
                print(">>> you have unfollowed {} number of people".format(unfollower_count))
            else:
                break
        else:
            print("Fail!")


username = ""
password = ""

ig = InstagramBot(username=username, password=password)
print(">>> Logging in")
ig.login()
print(">>> Waiting 10 secs")
time.sleep(10)
ig.unfollow()
print(">>> Waiting 10 secs")
time.sleep(10)
print(">>> Waiting 10 secs")
time.sleep(10)
ig.unfollow()
print(">>> Closing Browser")
ig.closeBrower()
