from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import pickle
import time
from file_path import mp3_path
from file_path import wav_path
from crop_image import create_crop
import os
from dotenv import load_dotenv
from webdriver_manager.chrome import ChromeDriverManager

# Load the .env file
load_dotenv()

key_dict = {
    "A-Flat-Minor":" A-flat minor ",
    "A-Flat-Major":" A-flat major ",
    "A-Minor":" A minor ",
    "A-Major":" A major ",
    "A-Sharp-Minor": " A-sharp minor ",
    "A-Sharp-Major": " A-sharp major ",
    "B-Flat-Minor":" B-flat minor ",
    "B-Flat-Major":" B-flat major ",
    "B-Minor":" B minor ",
    "B-Major":" B major ",
    "C-Flat-Major":" C-flat major ",
    "C-Minor":" C minor ",
    "C-Major":" C major ",
    "C-Sharp-Minor": " C-sharp minor ",
    "C-Sharp-Major": " C-sharp major ",
    "D-Flat-Major":" D-flat major ",
    "D-Minor":" D minor ",
    "D-Major":" D major ",
    "D-Sharp-Minor": " D-sharp minor ",
    "E-Flat-Major":" E-flat major ",
    "E-Minor":" E minor ",
    "E-Major":" E major ",
    "F-Minor":" F minor ",
    "F-Major":" F major ",
    "F-Sharp-Minor": " F-sharp minor ",
    "F-Sharp-Major": " F-sharp major ",
    "G-Flat-Major":" G-flat major ",
    "G-Minor":" G minor ",
    "G-Major":" G major ",
    "G-Sharp-Minor": " G-sharp minor ",
}
create_crop()

def beatstars(number: int, bpm: int, name: str, key: str, tags: list, folder:str, dir_path:str, driver_path:str):
    # Prevent browser from closing
    ## Create option instance
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # Create instance of google chrome and pass options instance
    # driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    #driverService = Service(driver_path)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    # to maximize the browser window
    driver.maximize_window()

    # Open URL
    driver.get("https://www.beatstars.com/dashboard")

    # Login: Email
    ## https://selenium-python.readthedocs.io/waits.html#explicit-waits
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#oath-email")
        )
    )

    # Input string and press button "enter"/"return"
    elem.send_keys(os.getenv("DEVICE_USERNAME"))
    elem.send_keys(Keys.RETURN)

    # Click element
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#btn-submit-oath")
        )
    )
    elem.click()

    # Login: Password
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#userPassword")
        )
    )
    elem.send_keys(os.getenv("DEVICE_PASSWORD"))
    elem.send_keys(Keys.RETURN)

    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#btn-submit-oath")
        )
    )
    elem.click()

    # Accept cookies
    try:
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
            )
        )
        elem.click()
    except:
        time.sleep(5)
    try:
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
            )
        )
        elem.click()
    except:
        pass

    # Pop Up

    try:
        elem = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="mat-dialog-0"]/bs-responsive-dialog-feature-template/bs-container-grid/div/div[1]/button')
            )
        )
        elem.click()
    except:
        pass

    # Click Upload Button
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             "#app-body > mp-root > mp-main-menu-top-nav > header > div > bs-container-grid.menu-top-nav.vb-r-gap-none > div > div.right-nav-side.authenticated > mp-button-upload-assets > bs-square-button > button > span")
        )
    )
    elem.click()

    # Click "My Uploads"
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#mat-menu-panel-8 > div > button:nth-child(3) > span")
        )
    )
    elem.click()

    # Click "+ Create media"
    elem = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
            By.CSS_SELECTOR, "#app-body > mp-root > mp-upload-files-nav > nav > div.btn-create > bs-square-button > button")
        )
    )
    elem.click()

    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             "#app-body > mp-root > div > div > ng-component > mp-component-container > div > div > div > section:nth-child(1) > button")
        )
    )
    elem.click()

    # Track Data
    ## Title
    title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             "#app-body > mp-root > div > div > ng-component > mp-track-form > div > form > fieldset.general-information > mat-card > div.track-form > section.track-info-section > div.track-title > div > input")
        )
    )
    title.clear()
    title.send_keys(f"{name} | {tags[0]} Type Beat")

    ##
    tag = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             "#app-body > mp-root > div > div > ng-component > mp-track-form > div > form > fieldset.general-information > mat-card > div.track-form > section.track-info-section > div.track-tags > mp-tags-input > div.input-text > div > input")
        )
    )
    tag.send_keys(tags[0])
    tag.send_keys(Keys.RETURN)
    tag.send_keys(tags[1])
    tag.send_keys(Keys.RETURN)
    tag.send_keys(tags[2])
    tag.send_keys(Keys.RETURN)

    # BPM
    bpm_elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             "#app-body > mp-root > div > div > ng-component > mp-track-form > div > form > fieldset.track-details > mat-card > div.track-details-info > section:nth-child(2) > div.track-bpm > div > input")
        )
    )
    bpm_elem.clear()
    bpm_elem.send_keys(bpm)

    # Key
    key_elem = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(
            (By.NAME, "keyNote")
        )
    )

    key_elem.click()
    key_select = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//*[text()='{key_dict[key]}']")
        )
    )
    key_select.click()

    # Click Mp3 button
    elem = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#tagged-tracks > button")
        )
    )
    driver.execute_script("arguments[0].click();", elem)
    # elem.click()

    ## Click cloud sign
    elem = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#file-dialog > div > ul > li:nth-child(1) > div > i")
        )
    )
    elem.click()


    ## Upload file
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#file-dialog > div > div > div > mp-step-my-device > div > input[type=file]")
        )
    )

    elem.send_keys(mp3_path(number, folder, dir_path))

    # Click WAV button
    elem = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#un-tagged-tracks > button")
        )
    )
    driver.execute_script("arguments[0].click();", elem)
    # elem.click()

    ## Click cloud sign
    elem = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#file-dialog > div > ul > li:nth-child(1) > div > i")
        )
    )
    elem.click()

    ## Upload file
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#file-dialog > div > div > div > mp-step-my-device > div > input[type=file]")
        )
    )
    elem.send_keys(wav_path(number))

    # Upload cropped image
    elem = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[text()=' Upload New Image ']")
        )
    )
    driver.execute_script("arguments[0].click();", elem)

    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "// *[text() = 'Upload file']")
        )
    )
    driver.execute_script("arguments[0].click();", elem)

    ## Click cloud sign
    elem = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#file-dialog > div > ul > li:nth-child(2) > div > i")
        )
    )
    elem.click()

    ## Upload file
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#uppy-drag-drop > div > button > input")
        )
    )
    elem.send_keys(r"D:\Dropbox\Youtube Uploads\Cropped_Image.jpg")

    # Save Crop
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "// *[text() = 'Save Crop']")
        )
    )
    elem.click()


    return