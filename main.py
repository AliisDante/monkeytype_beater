from time import sleep

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = Firefox(executable_path="./geckodriver")

def type_current_word(word_element, typing_element):
    letter_elements = word_element.find_elements(By.CSS_SELECTOR, "letter")

    letters = []

    for i in letter_elements:
        letters.append(i.text)

    letters = "".join(letters)

    if not typing_element:
        return False

    for i in letters:
        typing_element.send_keys(i)
        # sleep(0.03)

    return True

browser.get("https://monkeytype.com")

# Accept cookies
element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".acceptAll")))
element.click()

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#words .active")))

while True:
    word_element = browser.find_element(By.CSS_SELECTOR, "#words .active")
    typing_element = browser.find_element(By.CSS_SELECTOR, "#wordsInput")
    if word_element and typing_element:
        if not type_current_word(word_element, typing_element):
            break
        typing_element.send_keys(" ")
