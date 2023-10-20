import time
import argparse
from anticaptchaofficial.recaptchav2proxyon import *
# from anticaptchaofficial.recaptchav2proxyless import *

import requests

from setting import *
from functions import *
from recaptcha import bypass_recaptcha_v2

CARECREDIT_URL = 'https://www.carecredit.com/apply/'
ALPHAEONCREDIT_URL = 'https://go.alphaeoncredit.com/credit-portal/apply'

ANTI_CAPTCHA_API_KEY = "03698f9d4f06153d8426f9d83fdd1d67"
ANTI_CAPTCHA_API_URL = "http://api.anti-captcha.com/createTask"
ANTI_CAPTCHA_RESULT_URL = "http://api.anti-captcha.com/getTaskResult"

def get_captcha_solution(api_key, site_key, url, user_agent):
    # Define the CAPTCHA type and details
    task_data = {
        "userAgent" : user_agent,
        "type": "NoCaptchaTask",
        "websiteURL": url,
        "websiteKey": site_key,
        "proxyType": PROXY["type"],
        "proxyAddress": PROXY["host"],
        "proxyPort": PROXY["port"],
        "proxyLogin": PROXY["login"],
        "proxyPassword": PROXY["password"]
    }

    # Send the task
    response = requests.post(ANTI_CAPTCHA_API_URL, json={
        "clientKey": api_key,
        "task": task_data
    })
    print (response.json())

    task_id = response.json().get("taskId")
    print ("task id", task_id)
    # Wait for the solution
    for _ in range(30):  # Wait up to 30 seconds
        time.sleep(5)  # Wait 5 seconds between each poll
        result = requests.post(ANTI_CAPTCHA_RESULT_URL, json={
            "clientKey": api_key,
            "taskId": task_id
        }).json()
        if result.get("status") == "ready":
            return result.get("solution").get("gRecaptchaResponse")

    raise Exception("Failed to get CAPTCHA solution in time")

def captcha_solving(api_key, site_key, url, user_agent):
    solver = recaptchaV2Proxyon()
    solver.set_verbose(1)
    solver.set_key(api_key)
    solver.set_website_url(url)
    solver.set_website_key(site_key)
    #set optional custom parameter which Google made for their search page Recaptcha v2
    #solver.set_data_s('"data-s" token from Google Search results "protection"')

    solver.set_proxy_type(PROXY["type"])
    solver.set_proxy_address(PROXY["host"])
    solver.set_proxy_port(PROXY["port"])
    solver.set_proxy_login(PROXY["login"])
    solver.set_proxy_password(PROXY["password"])

    solver.set_user_agent(user_agent)
    solver.set_cookies("test=true")


    # Specify softId to earn 10% commission with your app.
    # Get your softId here: https://anti-captcha.com/clients/tools/devcenter
    solver.set_soft_id(0)

    g_response = solver.solve_and_return_solution()
    if g_response != 0:
        print ("g-response: "+g_response)
    else:
        print ("task finished with error " + solver.error_code)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Make an credit profile")

    with open('elements.json') as fp:
        elements = json.loads(fp.read())
    
    profile_id = ''

    # Delete Profile
    try:
        profile_id = fnGetUUID(f'{OCTO_ID}')
        deleteProfile(profile_id)
        print(f'Success to delete {OCTO_ID} profile!')
    except:
        print(f'There does not exist with profile name {OCTO_ID}')
    
    # Create Profile
    try:
        profile_id = fnGetUUID(f'{OCTO_ID}')
    except:
        print(f'Create Octo Profile with {OCTO_ID}.')
        profile_id = createProfile(f'{OCTO_ID}')

    port = get_debug_port(profile_id)
    driver = get_webdriver(port)

    # driver = webdriver.Chrome(service=Service(executable_path="C:/chromedriver-win64/chromedriver.exe"))
    # driver.get('https://patrickhlauke.github.io/recaptcha/')

    ''' automate the care credit '''
    # driver.get(CARECREDIT_URL)
    # oldURL = ''
    # while True:
    #     newURL = driver.current_url
    #     if newURL.split('/')[-2] == 'apply':
    #         while True:
    #             if carecredit_apply_first(driver):
    #                 break
    #     elif newURL.split('/')[-1] == 'applyPage.action' or newURL.split('/')[-1] == 'instantLinkAuthSucces.action':
    #         while True:
    #             if carecredit_apply(driver):
    #                 break
    #     elif newURL.split('/')[-1] == 'pfInstantLink.action':
    #         while True:
    #             if carecredit_link(driver):
    #                 break
        
    #     elif newURL.split('/')[-1][:13] == 'eapply.action':
    #         print (newURL)
    #         while True:
    #             if carecredit_verification(driver):
    #                 print ('verification')
    #                 break
    #     oldURL = newURL
    # time.sleep(10)

    ''' automate the alphaeon credit '''
    alphaeoncredit_captcha_status = False
    driver.get(ALPHAEONCREDIT_URL)
    oldURL = ''
    while True:
        newURL = driver.current_url
        print (newURL)
        if newURL.split('/')[-1] == 'apply':
            alphaeoncredit_pre_qualify(driver)
        elif newURL.split('/')[-1][:5] == 'phone':
            if not alphaeoncredit_captcha_status:
                print ('captcha detected! ', newURL)
                alphaeoncredit_captcha_status = bypass_recaptcha_v2(driver)
            else:
                alphaeoncredit_verification(driver)
        elif newURL.split('/')[-2][:5] == 'phone':
            pass
        elif newURL.split('/')[-1][:5] == 'offer':
            while True:
                if alphaeoncredit_apply(driver):
                    break
        
        oldURL = newURL
    time.sleep(10)
    ''' automate the alphaeon credit '''
