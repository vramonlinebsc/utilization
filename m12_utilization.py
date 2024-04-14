#!/usr/bin/env python
# coding: utf-8

# pip install 2captcha-python
# pip install -U selenium
# pip install webdriver-manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

import time
import logging

#chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')

options= webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize Chrome driver with options
driver=webdriver.Chrome(options=options)
#driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.maximize_window()
driver.get("https://eprotector.nuvamaassetservices.com/")
wait = WebDriverWait(driver, 10)

img_captcha = wait.until(ec.visibility_of_element_located((By.ID, "lblCapImg")))
txt_captcha = wait.until(ec.visibility_of_element_located((By.ID, "txtCaptcha")))
txt_captcha.clear()
txt_captcha.send_keys(img_captcha.text)

txt_username = wait.until(ec.visibility_of_element_located((By.ID, "txtUserID")))
txt_username.clear()
txt_username.send_keys('20118')

txt_password = wait.until(ec.visibility_of_element_located((By.ID, "txtPassword")))
txt_password.clear()
txt_password.send_keys('ClassB@234')

btn_submit = wait.until(ec.visibility_of_element_located((By.ID, "btnSubmit")))
btn_submit.click()

try:
    WebDriverWait(driver, 10).until(ec.alert_is_present())
    driver.switch_to.alert.accept()
    print("Alert Present")
except:
    print("No Alert")

try:
    WebDriverWait(driver, 10).until(ec.alert_is_present())
    driver.switch_to.alert.accept()
    print("Alert Present")
except:
    print("No Alert")

while (len(driver.window_handles) < 2):
    wait = WebDriverWait(driver, 2)

driver.switch_to.window(driver.window_handles[1])

driver.find_element(by=By.XPATH, value="// a[contains(text(),\'OMM')]").click()
driver.find_element(by=By.XPATH, value="// a[contains(text(),\'Client OMM')]").click()
btn_nse = driver.find_element(by=By.XPATH, value="// a[contains(text(),\'NSE Derivatives')]")

btn_nse.send_keys("\n")

wait.until(ec.frame_to_be_available_and_switch_to_it((By.ID, "COMM-NSE+Derivatives_Frame")))
try:
    txt_req = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[3]/div/div/table/tbody/tr[2]/td[7]")
    txt_req2 = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[3]/div/div/table/tbody/tr[2]/td[10]")

    txt_util = txt_req.text
    txt_mtm = txt_req2.text

    print(txt_util)
    print(txt_mtm)
except Exception as e:
    print(f"Error: {e}")
    """
       #outlook = win32com.client.Dispatch('outlook.application')
        #mail = outlook.CreateItem(0)
        #mail.To = 'prawinmani@gmail.com'
        #mail.To = 'kedar@matsyacapital.com;sunil@matsyacapital.com;manojk@matsyacapital.com;shivam@matsyacapital.com'
        #mail.Subject = 'M12 - Utilisation Rate'
        #mail.Body = "Current Utilisation Rate is at " + str(txt_util) + "%\nFutures MTM is " + str(txt_mtm)
        #mail.Send()
    #except:
    #    print("Error: No Record")
    """
driver.switch_to.default_content()

btn_logout = driver.find_element(By.XPATH, "/html/body/form[1]/table/tbody/tr[1]/td[2]/a[2]")

driver.execute_script("doLogout();", btn_logout)
driver.close()

driver.switch_to.window(driver.window_handles[0])
driver.close()
