import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

class TestTodoList:

    @classmethod
    def setup_class(cls):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',  
            'appPackage': 'com.example.todolist',  
            'appActivity': '.MainActivity',  # 
            'automationName': 'UiAutomator2'
        }
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_add_task(self):
        # Menekan tanda + untuk menambahkan task baru
        add_button = self.driver.find_element_by_id('add_button_id')  
        add_button.click()

        task_field = self.driver.find_element_by_id('task_field_id')  
        task_field.send_keys('Belajar Appium')

        save_button = self.driver.find_element_by_id('save_button_id') 
        save_button.click()

        sleep(2)
    
        tasks = self.driver.find_elements_by_id('task_id')  
        assert 'Appium' in [task.text for task in tasks]

    def test_check_task_in_list(self):
        tasks = self.driver.find_elements_by_id('task_id') 
        assert 'Appium' in [task.text for task in tasks]

    def test_delete_task(self):
        task_element = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Appium']") 

        actions = TouchAction(self.driver)
        actions.long_press(task_element).move_to(x=10, y=task_element.location['y']).release().perform()

        sleep(2)

        tasks = self.driver.find_elements_by_id('task_id')
        assert 'Belajar Appium' not in [task.text for task in tasks]
