from selenium import webdriver
from selenium.webdriver.common.by import By
from _pytest import mark
from _pytest.mark.structures import Mark
from time import sleep
import time
import pytest

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-logging'])
option.headless = True
option.add_argument('-- windows-size=1920,1080')
#==============================================================================
# INPUT VALUE LOGIN FOR NEGATIVE CASE
#==============================================================================    
dataReg= [
    ("PT.Bisa Masuk ID","Japran Abqory","Abqory@gmail.com","085777888999","Bisamasuk789#","Bisamasuk789#"),
    ("PT.Bisa Masuk ID","Japran Abqory","Abqory@gmail.com","085777888999","0","0"),
    ("PT.Bisa Masuk ID","Japran Abqory","Abqory@gmail.com","085777888999","Bisamasuk789#","000000"),
    #("","Japran Abqory","Abqory@gmail.com","085777888999","Bisamasuk789#","Bisamasuk789#")
]

#==============================================================================
# FIXTURE : [Setup,Option,Maximaze win,implicity_wait,Screenshot]
#==============================================================================    
@pytest.fixture
def setup1():
    #driver = webdriver.Chrome(options=option)
    driver = webdriver.Chrome(executable_path='C:Users/azmij/chromedriver.exe')
    driver.get("https://titip-web-front-staging.azurewebsites.net/")
    driver.maximize_window()
    driver.implicitly_wait(25)
    yield driver
    driver.get_screenshot_as_file("S_setup1.png")
    driver.quit()
    
    #Notif11 = driver.find_element(By.XPATH,"//button[@class='text-gray-800 border-gray-800 border-b-4 lg:text-xl text-lg font-semibold mx-6 outline-none py-2']").text
    #assert Notif11 == "Cari Kargo"
    
#==============================================================================
# SCENARIO / TEST CASE  :  REGISTER - NORMAL = Regist dengan data yang valid [sukses]
#==============================================================================    

@pytest.mark.normalregister     
def test_register(setup1):
    setup1.find_element(By.XPATH,"//button[@class='bg-transparent ml-5 px-[18px] py-[5px] border-2 border-white text-white rounded-lg transition duration-500 text-xs font-semibold mx-1']").click()
    time.sleep(10)
    setup1.find_element(By.XPATH,"//p[.='Charterer']").click()
    setup1.find_element(By.XPATH,"//div[@class='mt-3 px-5']/div[1]/div[1]//input[@class='bg-inputGray rounded-lg text-xs placeholder:text-[11.5px] px-2 py-3 h-fit w-full outline-none ']").send_keys("PT Staging Coba coba")
    setup1.find_element(By.XPATH,"//div[@class='mt-3 px-5']//div[2]//input[@class='bg-inputGray rounded-lg text-xs placeholder:text-[11.5px] px-2 py-3 h-fit w-full outline-none ']").send_keys("azmijays")
    setup1.find_element(By.XPATH,"//div[@class='mt-3 px-5']//div[3]//input[@class='bg-inputGray rounded-lg text-xs placeholder:text-[11.5px] px-2 py-3 h-fit w-full outline-none ']").send_keys("PT_Stagingsaja@yahoo.com")
    setup1.find_element(By.XPATH,"//div[@class='mt-3 px-5']//div[4]//input[@class='bg-inputGray rounded-lg text-xs placeholder:text-[11.5px] px-2 py-3 h-fit w-full outline-none ']").send_keys("087000000789")
    setup1.find_element(By.XPATH,"//select[@class='bg-inputGray w-full text-xs px-3 py-3 rounded-lg outline-none ']").click()
    setup1.find_element(By.XPATH,"//option[.='PT']").click()
    setup1.find_element(By.XPATH,"//button[@class='w-full bg-slmRed rounded-md text-xs font-semibold text-white py-2.5']").click()
    time.sleep(15)
    setup1.find_element(By.XPATH,"//div[@class='mt-3 px-5']/div[1]/div[1]//input[@name='password']").send_keys("Bisamasuk789#")
    setup1.find_element(By.XPATH,"//div[@class='mt-3 px-5']//div[2]//input[@name='password']").send_keys("Bisamasuk789#")
    time.sleep(10)
    setup1.find_element(By.XPATH,"//button[@class='w-full bg-slmRed rounded-md text-xs font-semibold text-white py-2.5']").click()
    time.sleep(8)
    #setup1.find_element(By.XPATH,"//button[@class='text-xs w-full bg-slmRed border-2 border-slmRed rounded-lg text-white py-2 font-semibold transition duration-500 hover:bg-red-800 hover:border-red-800 ']").click()
    #assert 
    notif1 = setup1.find_element(By.XPATH,"//p[@class='text-md text-gray-800 font-bold']").text #---> to verify that user succesfully registered their account
    assert notif1 == "Berhasil mendaftar"
    time.sleep(5)
    
#==============================================================================
# SCENARIO / TEST CASE  :  REGISTER - NEGATIVE 
#==============================================================================  
    
@pytest.mark.Negativereg
@pytest.mark.parametrize('a,b,c,d,e,f',dataReg)
def test_negative_regist(setup1,a,b,c,d,e,f):
    setup1.find_element(By.XPATH,"//button[@class='bg-transparent ml-5 px-[18px] py-[5px] border-2 border-white text-white rounded-lg transition duration-500 text-xs font-semibold mx-1']").click()
    time.sleep(10)
    setup1.find_element(By.XPATH,"//p[.='Charterer']").click()
    setup1.find_element(By.XPATH,"//div[@class='mt-3 px-5']/div[1]/div[1]//input[@class='bg-inputGray rounded-lg text-xs placeholder:text-[11.5px] px-2 py-3 h-fit w-full outline-none ']").send_keys(a)
    setup1.find_element(By.XPATH,"//div[@class='mt-3 px-5']//div[2]//input[@class='bg-inputGray rounded-lg text-xs placeholder:text-[11.5px] px-2 py-3 h-fit w-full outline-none ']").send_keys(b)
    setup1.find_element(By.XPATH,"//div[@class='mt-3 px-5']//div[3]//input[@class='bg-inputGray rounded-lg text-xs placeholder:text-[11.5px] px-2 py-3 h-fit w-full outline-none ']").send_keys(c)
    setup1.find_element(By.XPATH,"//div[@class='mt-3 px-5']//div[4]//input[@class='bg-inputGray rounded-lg text-xs placeholder:text-[11.5px] px-2 py-3 h-fit w-full outline-none ']").send_keys(d)
    setup1.find_element(By.XPATH,"//select[@class='bg-inputGray w-full text-xs px-3 py-3 rounded-lg outline-none ']").click()
    setup1.find_element(By.XPATH,"//option[.='PT']").click()
    setup1.find_element(By.XPATH,"//button[@class='w-full bg-slmRed rounded-md text-xs font-semibold text-white py-2.5']").click()
    time.sleep(15)
    setup1.find_element(By.XPATH,"//div[@class='mt-3 px-5']/div[1]/div[1]//input[@name='password']").send_keys(e)
    setup1.find_element(By.XPATH,"//div[@class='mt-3 px-5']//div[2]//input[@name='password']").send_keys(f)
    time.sleep(10)
    setup1.find_element(By.XPATH,"//button[@class='w-full bg-slmRed rounded-md text-xs font-semibold text-white py-2.5']").click()
    time.sleep(8)
    
    #notif2 = setup1.find_element(By.XPATH,"//p[@class='text-xs text-red-500']").text
    #assert notif2 == "Kolom wajib diisi"
   
   
#==============================================================================
# SCENARIO / TEST CASE  :  LOGIN - NORMAL [Failed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ]
#==============================================================================  
@pytest.mark.Login                  #------> still failed because i could not found xpath for login button
def test_Login(setup1):
    setup1.find_element(By.CLASS_NAME,"px-[18px] py-[5px] border-2 bg-slmRed border-slmRed text-white rounded-lg transition duration-500 text-xs font-semibold mx-1").click()
    time.sleep(20)
    #setup1.find_element(By.CLASS_NAME,".mx-1.bg-slmRed").click()
    setup1.find_element(By.XPATH,"//form[@class='space-y-5']/div[1]/input[@class='null w-full text-xs bg-transparent rounded-lg border-[1.5px] border-gray-200 px-4 py-2.5 outline-none']").Send_keys("deppjons@gmail.com")
    setup1.find_element(By.XPATH,"//form[@class='space-y-5']/div[2]//input[@class='null w-full text-xs bg-transparent rounded-lg border-[1.5px] border-gray-200 px-4 py-2.5 outline-none']").Send_keys("bigdreams")
    setup1.find_element(By.XPATH,"//form[@class='space-y-5']/div[2]//input[@class='null w-full text-xs bg-transparent rounded-lg border-[1.5px] border-gray-200 px-4 py-2.5 outline-none']").click()
    time.sleep(8)
    
#==============================================================================
# SCENARIO / TEST CASE  :  Search Kargo - NORMAL 
#==============================================================================   
@pytest.mark.SearchKargo
def test_Search(setup1):
    setup1.find_element(By.XPATH,"//input[@class='undefined w-full text-xs bg-transparent rounded-3xl border-[1.5px] border-gray-200 px-3 py-3 outline-none inputBarcodeField']").send_keys("aceh")
    setup1.find_element(By.XPATH,"//button[@class='sc-ftvSup bnstfL h-fit bg-slmRed text-white border-[1.5px] border-slmRed text-xs font-semibold px-12 py-3 mt-2 rounded-3xl outline-none transition duration-500 hover:bg-transparent hover:text-slmRed']").click()
    time.sleep(15)
    
    #place1 = setup1.find_element(By.XPATH,"//span[.='Aceh port']").text
    #assert place1 == "Aceh port"
    
#==============================================================================
# SCENARIO / TEST CASE  :  CONTACT US - NORMAL [Sukses]
#==============================================================================  
   
@pytest.mark.ContactUs
def test_kontakKami(setup1):
    setup1.find_element(By.XPATH,"//button[.='Kontak']").click()
    setup1.find_element(By.XPATH,"//div[@class='space-y-4']/div[1]/input[@class='null w-full text-xs bg-transparent rounded-lg border-[1.5px] border-gray-200 px-4 py-2.5 outline-none']").send_keys("PT Kunci Mas")
    setup1.find_element(By.XPATH,"//div[@class='space-y-4']/div[2]/input[@class='null w-full text-xs bg-transparent rounded-lg border-[1.5px] border-gray-200 px-4 py-2.5 outline-none']").send_keys("ptKunciMas@gmail.com")
    setup1.find_element(By.XPATH,"//select[@class='null bg-transparent text-xs rounded-lg border-[1.5px] border-gray-200 px-2 py-3 outline-none w-full']").click()
    setup1.find_element(By.XPATH,"//option[.='Charterer']").click()
    setup1.find_element(By.XPATH,"//textarea[@class='null bg-transparent border-[1.5px] rounded-lg resize-none h-20 text-xs px-2 py-2 w-full outline-none']").send_keys("Have we take another daily meet?")
    setup1.find_element(By.XPATH,"//button[@class='bg-blue-900 w-full text-white rounded-lg text-xs font-semibold py-3']").click()
    time.sleep(20)
    
    
    Finish = setup1.find_element(By.XPATH,"//p[@class='text-md text-gray-800 font-bold']").text
    assert Finish == "Pesan Anda telah kami terima"
    time.sleep(5)
    
#==============================================================================
# SCENARIO / TEST CASE  :  ABOUT US - NORMAL [Sukses]
#==============================================================================  
#@pytest.mark.aboutUs
#def test_aboutus(setup1):
#    setup1.find_element(By.XPATH,"//div[@class='lg:flex lg:items-center lg:align-end hidden relative']/div[3]//button[@class='text-sm text-gray-800 outline-none mx-4 flex']").click()
    
    #about1 = setup1.find_element(By.XPATH,"//p[@class='lg:text-base text-gray-400 font-semibold uppercase pb-5 tracking-widest']").text
    #assert about1 == "Tentang kami"
