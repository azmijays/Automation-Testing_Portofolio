from selenium import webdriver
from selenium.webdriver.common.by import By
from _pytest import mark
from _pytest.mark.structures import Mark
from time import sleep
import time
import pytest

# SCENARIO / TEST CASE 2 : NORMAL - CHECK BOX
#===============================================================================
@pytest.mark.checkBox
def test_checkbox():
    driver = webdriver.Chrome(executable_path='C:/Users/azmij/chromedriver.exe')
    driver.get("https://demoqa.com/checkbox")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//span[@class='rct-checkbox']").click()
    time.sleep(20)
    
    result = driver.find_element(By.XPATH,"//span[.='home']").text
    assert result == "home"
