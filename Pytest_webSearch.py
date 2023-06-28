from selenium import webdriver
from selenium.webdriver.common.by import By
from _pytest import mark
from _pytest.mark.structures import Mark
from time import sleep
import time
import pytest

@pytest.mark.webSearch
def test_normal_srch():
    driver = webdriver.Chrome(executable_path='C:/Users/azmij/chromedriver.exe')
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()
    driver.implicitly_wait(20)  
    driver.find_element(By.XPATH,"//div[@class='rt-tbody']/div[1]//span[2]").click()    # for delete element on table
    time.sleep(15)
    driver.find_element(By.XPATH,"//input[@id='searchBox']").send_keys("Alden")        # function for searching data
    time.sleep(30)
    driver.quit()
