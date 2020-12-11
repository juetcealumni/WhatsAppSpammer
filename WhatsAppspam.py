from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver=webdriver.Chrome('F:\chromedriver.exe')
driver.implicitly_wait(15)
driver.get('https://web.whatsapp.com')
victim=input('Enter user name to spam: ')
inputbox = driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/label[1]/div[1]/div[2]")
inputbox.send_keys(victim)
inputbox.send_keys(Keys.ENTER)
inputString = input("Enter message to send: ")
while(True):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()