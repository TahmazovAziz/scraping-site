from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
print('на каком браузере вы хотите запустить код?')


link = "https://www.name-generator.org.uk/nickname/"

choose_brouser = int(input('1 - Firefox, 2 - Chrome'))
    
if choose_brouser == 1:
    firefox_options = FirefoxOptions()
    firefox_options.add_argument('--headless')
    firefox_driver = webdriver.Firefox(options=firefox_options)
    firefox_driver.get(link)
    fill_name_button = firefox_driver.find_element(By.ID, "fill_all").click()
    xpath = '//*[@id="quick_submit"]'
    start_button = firefox_driver.find_element(By.XPATH, xpath).click()
    name = firefox_driver.find_element(By.CLASS_NAME, "names").text
    print(name)
elif choose_brouser == 2:
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver.get(link)
    
    fill_name_button = chrome_driver.find_element(By.ID, "fill_all").click()
    xpath = '//*[@id="quick_submit"]'
    start_button = chrome_driver.find_element(By.XPATH, xpath).click()
    name = chrome_driver.find_element(By.CLASS_NAME, "names").text
    print(name)
else:
    print('данный браузер не подерживаеться')
