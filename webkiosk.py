from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options=Options()
#chrome_options.add_argument("--headless")

user = ["*********"]    #username
pwd = ["**********"]    #password

#driver=webdriver.Chrome()
driver=webdriver.Chrome("C:/Users/Abhinav Gupta/Downloads/chromedriver.exe",options=chrome_options)

driver.get("https://webkioskintra.thapar.edu:8443/")

elem = driver.find_element_by_name("MemberCode")
elem.send_keys(user[0])
elem = driver.find_element_by_name("Password")
elem.send_keys(pwd[0])
elem.send_keys(Keys.RETURN)

time.sleep(10)
#window_after = driver.window_handles[0]
#then execute the switch to window method to move to newly opened window



#driver.switch_to_window(window_after)
while(1):
    print(driver.get("https://webkioskintra.thapar.edu:8443/StudentFiles/SRS/StudNewSrsEntry.jsp"))

    time.sleep(10)
    driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td/input").click()

    time.sleep(10)
    if(driver.find_element_by_xpath("/html/body/table[3]/tbody/tr[7]/td/input").get_attribute("value")=="Send Feedback"):
        driver.find_element_by_xpath("/html/body/table[3]/tbody/tr[7]/td/input").click()
    else:
        driver.find_element_by_xpath("/html/body/table[3]/tbody/tr[20]/td/input").click()


while(1):
    print('reached here')
    continue
