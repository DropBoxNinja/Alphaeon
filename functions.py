import time
import autoit
import ctypes
import json

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from setting import *

def carecredit_apply_first(driver)->bool:
    time.sleep(1)
    elements = load_json('elements.json')
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['profession'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.send_keys(Keys.DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()
    except:
        print("Can't input Profession!")
        return False
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['getStarted'])
        ele.click()
    except:
        print("Can't click get started button!")
        return False
    return True

def carecredit_verification(driver)->bool:
    time.sleep(1)
    elements = load_json('elements.json')
    user = load_json('user.json')
    
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['verifySSN'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys('a')
        actions.send_keys(user["ssnNumber"][-4:])
        actions.perform()
    except:
        print("Can't input last for digits of SSN!")
        return False
    
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['verifyMobileNumber'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys('a')
        actions.send_keys(user["mobileNumber"])
        actions.perform()
    except:
        print("Can't input mobile phone number!")
        return False
    
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['verifyButton'])
        ele.click()
    except:
        print("Can't click continue button!")
        return False
    
    return True

def carecredit_link(driver)->bool:
    time.sleep(1)
    elements = load_json('elements.json')

    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['textLink'])
        ele.click()
    except:
        print ('Can\'t click text link!')
        return False
    return True

def carecredit_apply(driver)->bool:
    time.sleep(1)
    elements = load_json('elements.json')
    user = load_json('user.json')
    
    time.sleep(1)
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['creditLimit'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["creditLimit"])
        actions.perform()
    except:
        print("Can't input creditLimit!")
        return False
    
    time.sleep(1)
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['firstName'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["firstName"])
        actions.perform()
    except Exception as e:
        print(f"Can't input firstName! {e}")
        return False
    
    time.sleep(1)
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['lastName'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["lastName"])
        actions.perform()
    except:
        print("Can't input lastName!")
        return False
    
    time.sleep(1)
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['streetAddress'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["streetAddress"])
        actions.perform()
    except:
        print("Can't input streetAddress!")
        return False
    
    time.sleep(1)
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['zipCode'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["zipCode"])
        actions.perform()
    except:
        print("Can't input zipCode!")
        return False
    
    time.sleep(1)
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['cityAndState'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["city"] + ', ' + user["state"])
        actions.perform()
    except:
        print("Can't input city and state!")
        return False
    
    time.sleep(1)
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['cityAndState'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["city"] + ', ' + user["state"])
        actions.perform()
    except:
        print("Can't input city and state!")
        return False
    
    time.sleep(1)
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['housing'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.send_keys(Keys.DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()
    except:
        print("Can't input housing!")
        return False
    
    time.sleep(1)
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['primaryPhone'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys('a')
        actions.send_keys(user["mobileNumber"])
        actions.perform()
    except:
        print("Can't input primary phone !")
        return False
    
    time.sleep(1)
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['primaryPhoneType'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.send_keys(Keys.DOWN)
        actions.send_keys(Keys.DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()
    except:
        print("Can't input primary phone type!")
        return False
    
    time.sleep(1)
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['emailAddress'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["email"])
        actions.perform()
    except:
        print("Can't input email address !")
        return False

    time.sleep(1)
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['confirmEmailAddress'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["email"])
        actions.perform()
    except:
        print("Can't input confirm email address !")
        return False
    
    time.sleep(1)
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['ssnNumber'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys('a')
        actions.send_keys(user["ssnNumber"])
        actions.perform()
    except:
        print("Can't input confirm ssn number !")
        return False
    
    time.sleep(1)
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['DOB'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys('a')
        actions.send_keys(user["DOB"])
        actions.perform()
    except:
        print("Can't input confirm DOB !")
        return False
    
    time.sleep(1)
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['monthlyIncome'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["monthlyIncome"])
        actions.perform()
    except:
        print("Can't input confirm monthly income !")
        return False
    
    time.sleep(1)
    try:
        ele = fnGetElementXpath(driver, False, elements["careCredit"]['apply'])
        ele.click()
    except:
        print("Can't click apply button !")
        return False
    
    return True


def alphaeoncredit_pre_qualify(driver)->bool:
    time.sleep(1)
    elements = load_json('elements.json')
    user = load_json('user.json')

    try:
        ele = fnGetElementXpath(driver, False, elements["alphaeonCredit"]['preQualifyButton'])
        ele.click()
    except:
        print("Can't click pre-qualify button !")
        return False
    return True

def alphaeoncredit_verification(driver)->bool:
    time.sleep(1)
    elements = load_json('elements.json')
    user = load_json('user.json')

    try:
        ele = fnGetElementXpath(driver, False, elements["alphaeonCredit"]['acceptCookieButton'])
        if ele == False:
            return True
        ele.click()
    except:
        print("Can't click accept all cookies !")
        return False
    
    try:
        ele = fnGetElementXpath(driver, False, elements["alphaeonCredit"]['verifyMobileNumber'])
        if ele == False:
            return True
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["mobileNumber"])
        actions.perform()
    except:
        print("Can't input mobile number !")
        return False
    
    try:
        ele = fnGetElementXpath(driver, False, elements["alphaeonCredit"]['verifySSN'])
        if ele == False:
            return True
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["ssnNumber"])
        actions.perform()
    except:
        print("Can't input ssn number !")
        return False
    
    try:
        ele = fnGetElementXpath(driver, False, elements["alphaeonCredit"]['verifyZipCode'])
        if ele == False:
            return True
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["zipCode"])
        actions.perform()
    except:
        print("Can't input zip code !")
        return False

    try:
        ele = fnGetElementXpath(driver, False, elements["alphaeonCredit"]['verifyButton'])
        if ele == False:
            return True
        ele.click()
    except:
        print("Can't click verify button !")
        return False

def alphaeoncredit_apply(driver)->bool:
    time.sleep(1)
    elements = load_json('elements.json')
    user = load_json('user.json')

    try:
        ele = fnGetElementXpath(driver, False, elements["alphaeonCredit"]['firstName'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["firstName"])
        actions.perform()
    except:
        print("Can't input firstName !")
        return False
    
    try:
        ele = fnGetElementXpath(driver, False, elements["alphaeonCredit"]['lastName'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["lastName"])
        actions.perform()
    except:
        print("Can't input lastName !")
        return False
    
    try:
        ele = fnGetElementXpath(driver, False, elements["alphaeonCredit"]['streetAddress'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["streetAddress"])
        actions.perform()
    except:
        print("Can't input streetAddress !")
        return False
    
    try:
        ele = fnGetElementXpath(driver, False, elements["alphaeonCredit"]['city'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["city"])
        actions.perform()
    except:
        print("Can't input city !")
        return False
    
    try:
        ele = fnGetElementXpath(driver, False, elements["alphaeonCredit"]['state'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["state"])
        actions.perform()
    except:
        print("Can't input state !")
        return False
    
    try:
        ele = fnGetElementXpath(driver, False, elements["alphaeonCredit"]['annualIncome'])
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(user["annualIncome"])
        actions.perform()
    except:
        print("Can't input annual income !")
        return False
    
    try:
        ele = driver.find_element_by_id('reviewTermsConsent')
        ele.click()
    except:
        print("Can't check consent !")
        return False

    try:
        ele = fnGetElementXpath(driver, False, elements["alphaeonCredit"]['submitButton'])
        ele.click()
    except:
        print("Can't click submit button !")
        return False
    
    return True