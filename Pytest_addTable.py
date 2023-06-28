from selenium import webdriver
from selenium.webdriver.common.by import By
from _pytest import mark
from _pytest.mark.structures import Mark
from time import sleep
import time
import pytest

# SCENARIO / TEST CASE 4 : NORMAL - WEB TABLE
#===============================================================================
@pytest.fixture
def setup2():
    driver = webdriver.Chrome(executable_path='C:/Users/azmij/chromedriver.exe')
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()
    driver.implicitly_wait(20)  
    driver.find_element(By.XPATH,"//button[@id='addNewRecordButton']").click()
    yield driver
    driver.quit() 

@pytest.mark.webTableadd
def test_add_webTable(setup2):
    #setup2.find_element(By.XPATH,"//button[@id='addNewRecordButton']").click()
    setup2.find_element(By.XPATH,"//input[@id='firstName']").send_keys("Zafran Abqory")
    setup2.find_element(By.XPATH,"//input[@id='lastName']").send_keys("Abqory")
    setup2.find_element(By.XPATH,"//input[@id='userEmail']").send_keys("Zafranabqory@yahoo.co.id")
    setup2.find_element(By.XPATH,"//input[@id='age']").send_keys("25")
    setup2.find_element(By.XPATH,"//input[@id='salary']").send_keys("15000000")
    setup2.find_element(By.XPATH,"//input[@id='department']").send_keys("IT Governence")
    setup2.find_element(By.XPATH,"//button[@id='submit']").click()

    result2 = setup2.find_element(By.XPATH,"//div[.='Zafran Abqory']").text  # This script is to validate the form is successfully added to a  table
    assert result2 == "Zafran Abqory"
