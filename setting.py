import selenium.webdriver as webdriver

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests
import json

from config import *

def load_json(json_file):
    with open(json_file) as fp:
        jsons = json.loads(fp.read())
    return jsons

def fnGetUUID(profileName):
    response_octo = requests.request("GET", f'{OCTO_AUTOMATION_URL}?search={profileName}', headers=OCTO_HEADER)
    data_uuid = response_octo.json()
    uuid = data_uuid.get('data')[0]['uuid']
    return uuid

def createProfile(profileName)->str:
    data = {
        "title": profileName,
        "fingerprint": {
                "os": "win",
                "screen": "1920x1080"
        },
        "proxy": PROXY
    }
    response = requests.post(url = OCTO_AUTOMATION_URL, json = data, headers=OCTO_HEADER).json()
    uuid = response.get('data')['uuid']
    return uuid

def deleteProfile(profileUUID)->str:
    data = {
        "uuids": [f"{profileUUID}"],
        "skip_trash_bin": True
    }
    response = requests.delete(url = OCTO_AUTOMATION_URL, json = data, headers=OCTO_HEADER).json()
    uuid = response.get('data')['deleted_uuids'][0]
    return uuid

def get_webdriver(port):
    chrome_options = Options()
    chrome_options.add_experimental_option('debuggerAddress', f'127.0.0.1:{port}')
    chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_argument('--headless')  # Run Chrome in headless mode, i.e., without GUI
    chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
    chrome_options.add_argument('--no-sandbox')
    # Change chrome driver path accordingly
    driver = webdriver.Chrome(
        service=Service(executable_path="C:/chromedriver-win64/chromedriver.exe"),
        options=chrome_options,
    )
    return driver

def get_debug_port(profile_id):
    data = requests.post(
        f'{LOCAL_API}/start', json={'uuid': profile_id, 'headless': False, 'debug_port': True}
    ).json()
    print(data)
    return data['debug_port']

def fnGetElementXpath(driver, flag, xpath):
    try:
        ele = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        if flag == False:
            return ele
        else:
            ele.click()
    except:
        print(f"fnGetElementXpath() is error because {xpath} can't find")
        return False

def fnGetElementsClass(driver, ClassName):
    try:
        eles = WebDriverWait(driver, 60).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, ClassName)))
        return eles
    except:
        print(f"fnGetElementXpath() is error because {ClassName} can't find")
        return False

