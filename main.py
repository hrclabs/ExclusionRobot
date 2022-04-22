import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def locate_element_by_xpath(xpath):
    try:
        element = WebDriverWait(selenium_driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        return element
    except:
        print("Oops ! Element cannot be detected.")


def locate_element_by_id(id):
    try:
        element = WebDriverWait(selenium_driver, 20).until(
            EC.presence_of_element_located((By.ID, id)))
        return element
    except:
        print("Oops ! Element cannot be detected.")


if __name__ == '__main__':

    print('Open Chrome browser...')
    path = "C:\\Users\\varunakanthak\\Automation\\chrome_driver\\chromedriver"
    selenium_driver = webdriver.Chrome(path)
    selenium_driver.maximize_window()

    # Go to login page
    selenium_driver.get("https://login.advancedmd.com/")

    # Switch to ifram
    selenium_driver.switch_to.frame(selenium_driver.find_element_by_tag_name("iframe"))
    time.sleep(2)

    print('Logging to AMD...')
    # Enter username
    user_name = locate_element_by_xpath(
        "/html/body/div/div[2]/form/fieldset/div[1]/input")
    user_name.clear()
    user_name.send_keys('BI_CBO1')

    # Enter password
    user_name = locate_element_by_xpath(
        "/html/body/div/div[2]/form/fieldset/div[2]/input")
    user_name.clear()
    user_name.send_keys('Haiti@2022!')

    # Enter office key
    user_name = locate_element_by_xpath(
        "/html/body/div/div[2]/form/fieldset/div[3]/input")
    user_name.clear()
    user_name.send_keys('136419')

    # Press Enter button
    user_name.send_keys(Keys.ENTER)

    time.sleep(10)

    print('Switching to second window...')
    # Switch to the second window
    selenium_driver.switch_to.window(selenium_driver.window_handles[1])

    # Click on Claim-Center
    claim_center = locate_element_by_id("mnuClaimsCenter")
    claim_center.click()

    time.sleep(10)

    print('Switching to third window...')
    # Switch to the third window
    selenium_driver.switch_to.window(selenium_driver.window_handles[2])

    print('Capturing required information...')
    # get information
    charge_reviews = locate_element_by_xpath("/html/body/fieldset/table/tbody/tr[2]/td[2]/nobr/span[2]")
    Claim_inspector = locate_element_by_xpath("/html/body/fieldset/table/tbody/tr[2]/td[3]/nobr/span[2]")
    unbilled = locate_element_by_xpath("/html/body/fieldset/table/tbody/tr[2]/td[5]/nobr/span[2]")
    exclusion_numbers = locate_element_by_xpath("/html/body/fieldset/table/tbody/tr[2]/td[6]/nobr/span[2]")
    run_alerts = locate_element_by_xpath("/html/body/fieldset/table/tbody/tr[2]/td[7]/nobr/span[2]")

    time.sleep(3)

    # Print information
    print("Charge Reviews : " + charge_reviews.text)
    print("Claim Inspector : " + Claim_inspector.text)
    print("Unbilled : " + unbilled.text)
    print("Exclusions : " + exclusion_numbers.text)
    print("Run Alerts : " + run_alerts.text)

    print('Closing all windows...')
    # Close all windows and the driver
    time.sleep(1)
    selenium_driver.close()
    selenium_driver.switch_to.window(selenium_driver.window_handles[1])
    time.sleep(1)
    selenium_driver.close()
    time.sleep(1)
    selenium_driver.quit()

    print('Done')
