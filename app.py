

from selenium.common.exceptions import NoSuchElementException 
from selenium import webdriver
import time
from random import randint
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
#############################################################################
Names    = ['Mary', 'Jenny', 'Jack', 'Mason', 'Joy', 'Elize', 'Pinky', 'Abigail', 'Gloria', 'Conny' , 'Pretty']

Name     = Names[randint(0,10)]
user     = randint(100,999)

getdriver = ("https://quiz2020.com/quiz/3289" + str(user))
driver = webdriver.Chrome(chrome_options=options)                 
driver.get(getdriver)

time.sleep(5)


driver.find_element_by_xpath('//*[@id="name"]').send_keys(Name)

driver.find_element_by_xpath('//*[@id="start"]').click()


def clickoncorrect():
    Options = []
    for k in range(1,10):
        for i in range(1,3):
            Option  = '/html/body/div[2]/div/div[2]/div[5]/table/tbody/tr[' + str(k) + ']/td[' + str(i) +']'
            try:
                a_      = driver.find_element_by_xpath(Option)
                a       = a_.get_attribute("class")
                if a == 'answer center correct':
                    a_.click()
                    break
            except NoSuchElementException:
                break
    
            
for i in range(1,21):
    clickoncorrect()
    time.sleep(1)
    
            
  
      
        
    
    
   
