import time
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options

def go_headless():
    options = Options()
    options.add_argument('--headless')
    return options

def connect_fb(uname, passwd):
    driver = webdriver.Firefox(firefox_options=go_headless())
    driver.get('https://www.facebook.com/')
    
    username = uname
    password = passwd
    
    email_el = driver.find_element_by_id('email')
    pass_el = driver.find_element_by_id('pass')
    submit_btn = driver.find_element_by_id("u_0_2")

    email_el.clear()
    pass_el.clear()

    email_el.send_keys(username)
    pass_el.send_keys(password)
    submit_btn.click()
    
    return driver

driver = connect_fb('', '')
driver.get('https://www.facebook.com/events/birthdays/')
time.sleep(10)
bday_today_by_tag = driver.find_elements_by_xpath("//div[@role='heading']")
whole_doc = driver.find_element_by_xpath('html')
#bday_today_by_tag1 = driver.find_elements_by_xpath("//div[@class='_4-u3']")

#print(bday_today_by_tag.text)    
#for index in range(len(bday_today_by_tag1)):
    #print(bday_today_by_tag[index].text)
    #print(bday_today_by_tag1[index].text)

print("The PAGE has all these text:")
print(whole_doc.text)
print("---------------------------------------------------")
print("Text I am trying to get:")
for el in bday_today_by_tag:
    print(el.text)

driver.close()



