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
    driver.get("https://XYZTravelCar.com/")
    driver.maximize_window()
    driver.implicitly_wait(2)
    yield driver
    driver.quit()

#==================================================================
# POSITIF TEST CASE : Order new rental car
#==================================================================

@pytest.mark.rental_Car
def test_rental_Car(setup):
    setup.find_element(By.ID,"Cars Product").click()
    setup.find_element(By.ID,"Without Driver").click()
    setup.implicitly_wait(2)
    setup.find_element(By.XPATH,"//option[contains(text(),'Pick-up Location')]").click()
    setup.find_element(By.XPATH,"//option[contains(text(),'Jakarta')]").click()
    setup.find_element(By.XPATH,"//option[contains(text(),'Pick-up Date')]").send_keys("26/04/2024")
    setup.find_element(By.XPATH,"//option[contains(text(),'Pick-up Time')]").send_keys("09.00")
    setup.find_element(By.XPATH,"//option[contains(text(),'Drop-off Date')]").send_keys("29/04/2024")
    setup.find_element(By.XPATH,"//option[contains(text(),'Drop-off Time')]").send_keys("11.00")
    setup.find_element(By.ID,"btn-Search Car").click()
    setup.implicitly_wait(5)
    setup.find_element(By.ID,"Car_1").click()
    setup.find_element(By.ID,"Car Provider_1").click()
    setup.find_element(By.ID,"Product Detail").click()
    setup.find_element(By.ID,"btn-Continue").click()
    setup.implicitly_wait(5)
    setup.find_element(By.XPATH,"//option[contains(text(),'Pick-up Location')]").click()
    setup.find_element(By.XPATH,"//option[contains(text(),'Rental Office')]").click()
    setup.find_element(By.XPATH,"//option[contains(text(),'Drop-off Location')]").click()
    setup.find_element(By.XPATH,"//option[contains(text(),'Other Location')]").click()
    setup.find_element(By.ID,"Pick-up/Drop-off").send_keys("Kindly please check for cars condition")
    setup.find_element(By.ID,"btn-Book Now").click()
    setup.implicitly_wait(5)
    setup.find_element(By.ID,"Contact Details").send_keys("085000111333")
    setup.find_element(By.ID,"Driver Details").send_keys("Driver name : Zafran abqory")
    setup.find_element(By.ID,"btn-Continue").click()
    setup.find_element(By.ID,"spesial request").send_keys("The car must be the latest version")
    setup.find_element(By.ID,"all rental requirements").click()
    setup.find_element(By.ID,"btn-Continue").click()
    setup.implicitly_wait(5)
    setup.find_element(By.ID,"Select Payment").click()
    setup.find_element(By.ID,"Transfer").click()
    setup.find_element(By.ID,"BCA").click()
    setup.find_element(By.ID,"btn-proceed payment").click()
    setup.implicitly_wait(5)

    alert = setup.find_element(By.ID,"Success!").text
    assert alert == "Your transfer has been confirmed"
