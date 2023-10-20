import time
import os

import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import speech_recognition as sr
import ffmpy
import requests
import pydub

captcha1 = 'https://patrickhlauke.github.io/recaptcha/'
captcha2 = 'https://www.google.com/recaptcha/api2/demo'

def bypass_recaptcha_v2(driver):

    time.sleep(3)
    for _ in range(4):
        if _ == 3:
            return False
        try:
            frames = driver.find_elements_by_tag_name('iframe')
            driver.switch_to.frame(frames[0])
            frames = driver.find_elements_by_tag_name('iframe')
            print ('first first iframe', len(frames), frames)
            driver.switch_to.frame(frames[0])
            time.sleep(3)
            break
        except:
            print ('can\'t find iframe')
            continue

    while True:
        try:
            driver.find_element_by_class_name('recaptcha-checkbox-border').click()
            print ('recaptcha-checkbox-border')
            time.sleep(10)
            break
        except:
            print ('cant\'t find recaptcha-checkbox-border')
            continue

    driver.switch_to.default_content()
    driver.switch_to.default_content()

    while True:
        try:
            frames = driver.find_elements_by_tag_name('iframe')
            driver.switch_to.frame(frames[0])
            frames = driver.find_element_by_xpath("/html/body/div[2]/div[4]").find_elements_by_tag_name('iframe')
            driver.switch_to.frame(frames[0])
            print('second second frames', len(frames), frames)
            time.sleep(3)
            break
        except:
            print ('can\'t find second frame')
            continue


    while True:
        try:
            driver.find_element_by_id("recaptcha-audio-button").click()
            print ("recaptcha-audio-button")
            time.sleep(10)
            break
        except:
            # print ('can\'t find recaptcha-audio-button')
            continue

    driver.switch_to.default_content()
    driver.switch_to.default_content()

    while True:
        try:
            frames = driver.find_elements_by_tag_name('iframe')
            driver.switch_to.frame(frames[0])
            frames = driver.find_elements_by_tag_name('iframe')
            driver.switch_to.frame(frames[-1])
            print('third third frames', len(frames), frames)
            time.sleep(3)
            break
        except:
            print ('can\'t find third frame')
            continue

    while True:
        try:
            driver.find_element_by_xpath("/html/body/div/div/div[3]/div/button").click()
            print ('play button clicked')
            time.sleep(3)
            break
        except:
            print ('can\'t find recaptcha-audio-button')
            continue
    for _ in range(4):
        if _ == 3:
            return False
        try:
            src = driver.find_element_by_id('audio-source').get_attribute('src')
            break
        except:
            continue
    print (f"[INFO] Audio src {src}")
    user_agent = driver.execute_script('navigator.userAgent')
    headers = {"User-Agent": user_agent}
    response = requests.get(src, headers=headers)
    if response.status_code == 200:
        with open("sample.mp3", "wb") as file:
            file.write(response.content)
    while True:
        try:
            sound = pydub.AudioSegment.from_mp3('sample.mp3')
            break
        except:
            continue
    sound.export('sample.wav', format='wav')

    sample_audio = sr.AudioFile('sample.wav')
    r = sr.Recognizer()
    with sample_audio as source:
        audio = r.record(source)
    while True:
        try:
            key = r.recognize_google(audio)
            break
        except:
            continue
    print (f"[INFO] recaptcha Passcod: {key}")

    driver.find_element_by_id('audio-response').send_keys(key.lower())
    driver.find_element_by_id('audio-response').send_keys(Keys.ENTER)

    os.remove('sample.mp3')
    os.remove('sample.wav')
    return True

if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(executable_path="C:/chromedriver-win64/chromedriver.exe"))
    driver.get(captcha1)
    if bypass_recaptcha_v2(driver):
        print ("success")
    else:
        print ("failed!")
    time.sleep(100)
