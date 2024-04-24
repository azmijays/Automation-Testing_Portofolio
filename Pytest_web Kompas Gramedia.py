from selenium import webdriver
from selenium.webdriver.common.by import By
from _pytest import mark
from _pytest.mark.structures import Mark
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import service as ChromeService
from time import sleep

import time
import pytest


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.mysantika.com/")
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.quit()

#======================================================================
# POSITIF TEST CASE : Order hotel and payment using BCA virtual Account
#======================================================================

@pytest.mark.order_Hotel
def test_order_Hotel(setup):
    setup.find_element(By.CSS_SELECTOR,"[aria-label='Discover Hotel or Location']").click() #arrow down
    setup.implicitly_wait(5)
    setup.find_element(By.CSS_SELECTOR,"[aria-label='Discover Hotel or Location']").send_keys("Jakarta")
    setup.implicitly_wait(3)
    setup.find_element(By.XPATH,"//div[.='Amaris Hotel Dr Susilo Grogol Jakarta']").click()
    setup.implicitly_wait(5)
    setup.find_element(By.XPATH,"//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/div[9]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/button[1]/div[1]").click() #search btn 
    time.sleep(5)
    setup.find_element(By.XPATH,"//button[@class='py-3 v-btn v-btn--flat theme--light']/div[@class='v-btn__content']").click()
    time.sleep(3)
    setup.find_element(By.XPATH,"//div[@id='room-list']/div[1]//div[4]//div[@class='flex booking-section xs12 sm12 md12']//div[@class='v-btn__content']").click() #select 1 room
    time.sleep(3)
    setup.find_element(By.XPATH,"//button[@class='mt-4 py-3 v-btn v-btn--flat theme--light']/div[@class='v-btn__content']").click() #Create reservation
    time.sleep(3)
    #Input data 
    setup.find_element(By.XPATH,"//div[@class='v-input mt-0 v-input--selection-controls v-input--switch v-input--hide-details theme--light']//div[@class='v-input--selection-controls__ripple']").click() #Toggle 
    setup.find_element(By.XPATH,"//ul[@class='v-expansion-panel theme--light']/li[1]//i[@class='v-icon material-icons theme--light']").click() #Arrow down
    time.sleep(2)
    setup.find_element(By.XPATH,"//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/div[12]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("testing788@gmail.com") #Email 
    setup.find_element(By.XPATH,"//li[@class='v-expansion-panel__container v-expansion-panel__container--active']//div[@class='flex pa-0 pr-2-sm-and-up pr-1-xs-only xs6']//input[1]").send_keys("Zafran") #First Name
    setup.find_element(By.XPATH,"//li[@class='v-expansion-panel__container v-expansion-panel__container--active']//div[@class='flex pa-0 pl-2-sm-and-up pl-1-xs-only xs6']//input[1]").send_keys("Abqory") #Last name
    setup.find_element(By.XPATH,"//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/div[12]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/input[1]").send_keys("85123456789") #Phone number
    time.sleep(2)
    setup.find_element(By.XPATH,"//button[contains(.,'Review Reservation')]").click() #Review Reservation btn
    time.sleep(2)
    setup.find_element(By.XPATH,"//button[contains(.,'Continue Payment')]").click() #Continue btn
    time.sleep(2)
    setup.find_element(By.XPATH,"//label[.='BCA Virtual Account']").click() #BCA Payment
    setup.find_element(By.XPATH,"//div[@class='tnc-pay-label']").click() #check box
    time.sleep(2)
    setup.find_element(By.XPATH,"//button[@class='custom v-btn v-btn--block v-btn--flat theme--dark']/div[@class='v-btn__content']").click() #Button pay
    setup.find_element(By.XPATH,"//div[contains(text(),'View Payment Instruction')]").click() #View payment
    time.sleep(10)

    #Assertation for hotel price is match with the total that must be paid by the user
    alert = setup.find_element(By.XPATH,"//div[@class='payment-instruction pa-3 v-card v-sheet theme--light']//div[@class='payment-instruction-channel-content-chname-left']/div[contains(.,'Rp 373.800')]").text
    assert alert == "Rp 373.800"
