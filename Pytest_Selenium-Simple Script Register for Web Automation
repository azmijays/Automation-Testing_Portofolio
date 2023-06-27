from selenium import webdriver
from selenium.webdriver.common.by import By
from _pytest import mark
from _pytest.mark.structures import Mark
from time import sleep
import time
import pytest

@Pytest.mark.Register
def Test_register()
    driver = webdriver.Chrome(executable_path='C:Users/azmij/chromedriver.exe')
    driver.get("https://titip-web-front-staging.azurewebsites.net/")
    driver.maximize_window()
    driver.implicitly_wait(25)
    yield driver
    driver.quit()

    driver.find_element(By.XPATH,"//button[@class='bg-transparent ml-5 px-[18px] py-[5px] border-2 border-white text-white rounded-lg transition duration-500 text-xs font-semibold mx-1']").click()
    time.sleep(10)
    driver.find_element(By.XPATH,"//p[.='Charterer']").click()
    driver.find_element(By.XPATH,"//div[@class='mt-3 px-5']/div[1]/div[1]//input[@class='bg-inputGray rounded-lg text-xs placeholder:text-[11.5px] px-2 py-3 h-fit w-full outline-none ']").send_keys("PT Staging Coba coba")
    driver.find_element(By.XPATH,"//div[@class='mt-3 px-5']//div[2]//input[@class='bg-inputGray rounded-lg text-xs placeholder:text-[11.5px] px-2 py-3 h-fit w-full outline-none ']").send_keys("azmijays")
    driver.find_element(By.XPATH,"//div[@class='mt-3 px-5']//div[3]//input[@class='bg-inputGray rounded-lg text-xs placeholder:text-[11.5px] px-2 py-3 h-fit w-full outline-none ']").send_keys("PT_Stagingsaja@yahoo.com")
    driver.find_element(By.XPATH,"//div[@class='mt-3 px-5']//div[4]//input[@class='bg-inputGray rounded-lg text-xs placeholder:text-[11.5px] px-2 py-3 h-fit w-full outline-none ']").send_keys("087000000789")
    driver.find_element(By.XPATH,"//select[@class='bg-inputGray w-full text-xs px-3 py-3 rounded-lg outline-none ']").click()
    driver.find_element(By.XPATH,"//option[.='PT']").click()
    driver.find_element(By.XPATH,"//button[@class='w-full bg-slmRed rounded-md text-xs font-semibold text-white py-2.5']").click()
    time.sleep(15)
    driver.find_element(By.XPATH,"//div[@class='mt-3 px-5']/div[1]/div[1]//input[@name='password']").send_keys("Bisamasuk789#")
    driver.find_element(By.XPATH,"//div[@class='mt-3 px-5']//div[2]//input[@name='password']").send_keys("Bisamasuk789#")
    time.sleep(10)
    driver.find_element(By.XPATH,"//button[@class='w-full bg-slmRed rounded-md text-xs font-semibold text-white py-2.5']").click()
    time.sleep(8)
    
    # Script below is to validate if user succesfully registered their account
    notif1 = setup1.find_element(By.XPATH,"//p[@class='text-md text-gray-800 font-bold']").text #---> to verify that user succesfully registered their account
    assert notif1 == "Berhasil mendaftar" 
    time.sleep(5)
