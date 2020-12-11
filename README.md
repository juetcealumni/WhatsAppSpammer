# WhatsApp Spammer Selenium
It's a selenium chromedriver based script to spam in WhatsApp groups. Make sure that you have installed correct chrome driver from official website.
## How to set up selenium?
The selenium package is used to automate web browser interaction from Python. At first, download required webdriver from selenium official website (https://selenium-python.readthedocs.io/installation.html). If you are using Google chrome, chromedriver is already available in this repo. Now open terminal and type `pip install selenium` to install python selenium package. Now keep the webdriver and the script in a folder of your choice.  

##  Explanation first !!!
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
```
For automating the web browsers, we need to import `webdriver` from selenium and to automate the inputs (Pressing keys automatically) we need to import `Keys`.  
```python
driver=webdriver.Chrome('F:\chromedriver.exe')
driver.implicitly_wait(15)
driver.get('https://web.whatsapp.com')
```
As we are using chrome here, we should use chromedriver now. Locate the `chromedriver.exe` file, copy the absolute path of it and pass the path as a parameter.  
Now, browser will open WhatsApp web and you have to scan the QR code by opening `WhatsApp Web` in your phone. The `driver.implicitly_wait(15)` tells the webdriver to wait for a while as the page might take some time to load properly.  
#### ChroPath plugin and XPath
Xpath is an XML path used for navigation through the HTML structure of the page. It is a syntax or language for finding any element on a web page using XML path expression. In Selenium automation, if the elements are not found by the general locators like id, class, name, etc. then XPath is used to find an element on the web page.  
ChroPath is a plugin for chrome which is used to find XPath ([Download from Chrome webstore](https://chrome.google.com/webstore/detail/chropath/ljngjbnaijcbncmcnjfhigebomdlkcjo)).  
```python
victim=input('Enter user name to spam: ')
inputbox = driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/label[1]/div[1]/div[2]")
inputbox.send_keys(victim)
inputbox.send_keys(Keys.ENTER)
inputString = input("Enter message to send: ")
```
As your code is running now, the prompt will ask you to input the name of the user (group/individual/Unknown number with whom you talked before). Even a few starting letters maybe sufficient as WhatsApp search box is quite smart :)  
The search Box is found by it's XPath and `send_keys` is used to pass the characters given as input. `ENTER` key automation opens the conversation. Now type the message in the prompt which you want to send to the user.  
```python
while(True):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
```
`while(True)` is used to run an infinite loop. Within this loop, characters of message are passed into the message box and the send button is clicked repeatedly until you close the program. So, have fun and keep spamming :joy::smiling_imp::sunglasses:
