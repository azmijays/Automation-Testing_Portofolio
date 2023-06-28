from selenium import webdriver
from selenium.webdriver.common.by import By
from _pytest import mark
from _pytest.mark.structures import Mark
from time import sleep
import time
import pytest

#===============================================================================
# SCENARIO / TEST CASE 1 : NORMAL - RADIO BUTTON
#===============================================================================
@pytest.mark.radioButton
def test_radioButton():
    driver = webdriver.Chrome(executable_path='C:/Users/azmij/chromedriver.exe')
    driver.get("https://demoqa.com/radio-button")
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR,"[for='yesRadio']").click()
    time.sleep(20)
    
    result1 = driver.find_element(By.XPATH,"//span[@class='text-success']").text   # <--- This script is to validate you have succesfully clicked the radio button
    assert result1 == "Yes"
