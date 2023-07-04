from selenium import webdriver
from selenium.webdriver.common.by import By
from _pytest import mark
from _pytest.mark.structures import Mark
from time import sleep

import time
import pytest

Login = [
    ("portoazmijays@gmail.com","12345678998"),       # Login with invalid password
    ("1234543","Bisamasuk789#")
]

@pytest.fixture
def setup():
    driver = webdriver.Chrome(executable_path='C:Users/azmij/chromedriver.exe')
    driver.get("https://snap.careers/")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//button[@class='close']").click()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    
@pytest.fixture # User has login with valid account
def setup2():
    driver = webdriver.Chrome(executable_path='C:Users/azmij/chromedriver.exe')
    driver.get("https://snap.careers/")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//button[@class='close']").click()
    driver.find_element(By.XPATH,"//button[@class='btn btn-theme border-radius-0']/i[@class='icon-login']").click()
    driver.implicitly_wait(25)
    driver.find_element(By.ID,"email").send_keys("portoazmijays@gmail.com")
    driver.find_element(By.XPATH,"//div[@id='candidate']//input[@name='password']").send_keys("Bisamasuk789#")
    driver.find_element(By.XPATH,"//div[@id='candidate']//button[@class='btn btn-theme']").click()
    time.sleep(30)
    yield driver
    driver.quit()

#==============================================================================
# SCENARIO / TEST CASE  :  Login Kandidat - NORMAL [Expected Sukses]
#==============================================================================  
@pytest.mark.loginNormal
def test_loginKandidat(setup):
    setup.find_element(By.XPATH,"//button[@class='btn btn-theme border-radius-0']/i[@class='icon-login']").click()
    setup.implicitly_wait(25)
    setup.find_element(By.ID,"email").send_keys("portoazmijays@gmail.com")
    setup.find_element(By.XPATH,"//div[@id='candidate']//input[@name='password']").send_keys("Bisamasuk789#")
    setup.find_element(By.XPATH,"//div[@id='candidate']//button[@class='btn btn-theme']").click()
    time.sleep(30)
    
    view = setup.find_element(By.XPATH,"//p[.='Jumlah Views']").text
    assert view == "Jumlah Views"
    
#==============================================================================
# SCENARIO / TEST CASE  :  Login Kandidat - Negative [Expected Failed login]
#==============================================================================
@pytest.mark.logNegative
@pytest.mark.parametrize('a,b',Login)
def test_loginKandidat1(setup,a,b):
    setup.find_element(By.XPATH,"//button[@class='btn btn-theme border-radius-0']/i[@class='icon-login']").click()
    setup.implicitly_wait(25)
    setup.find_element(By.ID,"email").send_keys(a)
    setup.find_element(By.XPATH,"//div[@id='candidate']//input[@name='password']").send_keys(b)
    setup.find_element(By.XPATH,"//div[@id='candidate']//button[@class='btn btn-theme']").click()
    time.sleep(30)
    
    #view = setup.find_element(By.XPATH,"//p[.='Jumlah Views']").text
    #assert view == "Jumlah Views"
    
#==============================================================================
# SCENARIO / TEST CASE  :  Lupa Password - Normal [Success change password]
#==============================================================================
@pytest.mark.lupaPsw
def test_lupaPassword(setup):
    setup.find_element(By.XPATH,"//button[@class='btn btn-theme border-radius-0']/i[@class='icon-login']").click()
    setup.implicitly_wait(8)
    setup.find_element(By.XPATH,"//a[@href='https://snap.careers/password/reset']").click()
    setup.implicitly_wait(15)
    setup.find_element(By.ID,"email").send_keys("portoazmijays@gmail.com")
    setup.find_element(By.XPATH,"//button[@class='btn btn-theme']").click()
    
    notif1 = setup.find_element(By.XPATH,"//div[@class='alert alert-success']").text
    assert notif1 == "Kami telah mengirim email untuk pengaturan ulang kata sandi!"
                        
    time.sleep(18)
    
#==============================================================================
# SCENARIO / TEST CASE  :  Lupa Password - Negative [Failed change password] using invalid email
#==============================================================================
@pytest.mark.negativePsw
def test_lupaPassword(setup):
    setup.find_element(By.XPATH,"//button[@class='btn btn-theme border-radius-0']/i[@class='icon-login']").click()
    setup.implicitly_wait(8)
    setup.find_element(By.XPATH,"//a[@href='https://snap.careers/password/reset']").click()
    setup.implicitly_wait(8)
    setup.find_element(By.ID,"email").send_keys("llakclnu")
    setup.find_element(By.XPATH,"//button[@class='btn btn-theme']").click()

#==============================================================================
# SCENARIO / TEST CASE  :  Find Jobs - Normal
#==============================================================================
@pytest.mark.Cariloker
def test_findloker(setup):
    setup.find_element(By.XPATH,"//a[.='Cari Lowongan']").click()
    setup.find_element(By.XPATH,"//select[@class='form-control select-multiple-state']/option[.='Pilih Provinsi']").click()
    setup.implicitly_wait(25)
    setup.find_element(By.XPATH,"//select[@class='form-control select-multiple-state']/option[.='Jawa Barat']").click()
    setup.implicitly_wait(25)
    setup.find_element(By.XPATH,"//div[@class='searchnt']/button[contains(.,'Cari')]").click()
    setup.implicitly_wait(25)
    setup.find_element(By.XPATH,"//a[contains(.,'MARKETING EVENT')]").click()
    setup.implicitly_wait(25)
    
#==============================================================================
# SCENARIO / TEST CASE  :  Contact Us - Normal
#==============================================================================
@pytest.mark.contactUs
def test_ContactUs(setup):
    setup.find_element(By.XPATH,"//ul[@class='navbar-nav ml-auto d-lg-none ']//a[contains(.,'Hubungi Kami')]").click()
    setup.implicitly_wait(30)
    
#==============================================================================
# SCENARIO / TEST CASE  :   - Normal
#==============================================================================   
@pytest.mark.perusahaan
def test_normalSnap(setup):
    setup.find_element(By.XPATH,"//ul[@class='navbar-nav ml-auto']//a[.='Perusahaan']").click()
    setup.implicitly_wait(20)
    
    company = setup.find_element(By.XPATH,"//h2[.='Perusahaan']").text
    assert company == "Perusahaan"
    
    setup.find_element(By.XPATH,"//a[contains(.,'COMMON GROUND')]").click()
    setup.implicitly_wait(20)
