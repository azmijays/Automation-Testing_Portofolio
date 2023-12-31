import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

'Membuka web'
WebUI.navigateToUrl('https://demo.midtrans.com/')

WebUI.maximizeWindow()

'Click btn buy'
WebUI.click(findTestObject('1. Checkout/button_buy'))

'Input Amount'
WebUI.setText(findTestObject('1. Checkout/input_amount'), '12000')

'Input name'
WebUI.setText(findTestObject('1. Checkout/input_name'), 'Sandi Sundoro')

'Input Email'
WebUI.setText(findTestObject('1. Checkout/input_email'), 'kelompok4@gmail.com')

'Input Number Phone'
WebUI.setText(findTestObject('1. Checkout/input_phone'), '085234555777')

'Input City'
WebUI.setText(findTestObject('1. Checkout/input_city'), 'Jakarta')

'Input Address'
WebUI.setText(findTestObject('1. Checkout/input_address'), 'Jl.Utama V No.50, Cengkareng, Jakarta Barat')

'Input Postal Code'
WebUI.setText(findTestObject('1. Checkout/input_postccode'), '11733')

'Click btn checkout'
WebUI.click(findTestObject('1. Checkout/button_checkout'))

WebUI.click(findTestObject('2. Payment/button_choose c card'))

'Input credit card number\r\n'
WebUI.setText(findTestObject('2. Payment/input_credit card'), '4811111111111114')

'input expired date'
WebUI.setText(findTestObject('2. Payment/input_expired date'), '0125')

'Input CVV'
WebUI.setText(findTestObject('2. Payment/input_cvv'), '123')

WebUI.click(findTestObject('2. Payment/radiobtn_nopromo'))

WebUI.click(findTestObject('2. Payment/button_paynow'))

WebUI.setText(findTestObject('2. Payment/input_password'), '112233')

WebUI.click(findTestObject('2. Payment/button_oke'))

WebUI.verifyElementText(findTestObject('2. Payment/Alert_payment success'), 'Thank you for your purchase.')

WebUI.acceptAlert()

