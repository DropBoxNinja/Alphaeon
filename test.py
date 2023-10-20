import time
import argparse

import requests

from setting import *
from functions import *
from recaptcha import bypass_recaptcha_v2

CARECREDIT_URL = 'https://www.carecredit.com/apply/'
ALPHAEONCREDIT_URL = 'https://go.alphaeoncredit.com/credit-portal/apply'

captcha1 = 'https://patrickhlauke.github.io/recaptcha/'

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description="Make an credit profile")

    # with open('elements.json') as fp:
    #     elements = json.loads(fp.read())
    
    # profile_id = ''

    # # Delete Profile
    # try:
    #     profile_id = fnGetUUID(f'{OCTO_ID}')
    #     deleteProfile(profile_id)
    #     print(f'Success to delete {OCTO_ID} profile!')
    # except:
    #     print(f'There does not exist with profile name {OCTO_ID}')
    
    # # Create Profile
    # try:
    #     profile_id = fnGetUUID(f'{OCTO_ID}')
    # except:
    #     print(f'Create Octo Profile with {OCTO_ID}.')
    #     profile_id = createProfile(f'{OCTO_ID}')

    # port = get_debug_port(profile_id)
    # driver = get_webdriver(port)

    driver = webdriver.Chrome(service=Service(executable_path="C:/chromedriver-win64/chromedriver.exe"))
    driver.get(captcha1)
    verification = "https://www.google.com"
    driver.execute_script(f'''window.open("{verification}", "_blank");''');
    print ('window handles count', len(driver.window_handles))
    driver.switch_to.window(driver.window_handles[1])
    print (driver.current_url)
    time.sleep(100)