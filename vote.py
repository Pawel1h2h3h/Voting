from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from find_data import (
    click_akceptuje,
    click_zaloguj,
    fill_password,
    fill_login)
from selenium.webdriver.common.by import By
from NordVPN_Randomizer.NordVPN_Randomizer import switch_vpn


def vote():
    driver = webdriver.Chrome()
    driver.get("https://konkurswarmiaimazury.pl/lista-zgloszen-w-kategorii-mieszkancy/")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    value = click_button(driver)
    time.sleep(5)
    switch_vpn()
    return value



def login_mail(login, password, driver):
    driver.execute_script("window.open('https://oauth.gazeta.pl/poczta/auth#s=NavIco', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])
    click_akceptuje(driver)
    fill_login(driver, login)
    fill_password(driver, password)
    click_zaloguj(driver)


def get_old_emails():
    with open('baza_starych_mail/stare_maile.txt', 'r') as fp:
        pass


def click_button(driver, xpath="/html/body/section/div/div[1]/div[30]/div[2]/div[1]/div[2]/button"):
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        hover_and_click(driver, button)
        return True
    except Exception as e:
        return False



def hover_and_click(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()


if __name__ == '__main__':
    while True:
        vote()
