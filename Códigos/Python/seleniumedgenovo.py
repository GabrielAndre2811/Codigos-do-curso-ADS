from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.geolocation": 1
})

nav = webdriver.Edge(options=options, service=Service(EdgeChromiumDriverManager().install()))
nav.maximize_window()

nav.get("https://app2.pontomais.com.br/")

nav.find_element(By.XPATH, '//*[@id="container-login"]/div[1]/div/div[4]/div[1]/login-form/pm-form/form/div/div/div[1]/pm-input/div/div/pm-text/div/input').send_keys("231313131")
nav.find_element(By.XPATH, '//*[@id="container-login"]/div[1]/div/div[4]/div[1]/login-form/pm-form/form/div/div/div[2]/pm-input/div/div/pm-password/div/input').send_keys("xxxxx")
nav.find_element(By.XPATH, '//*[@id="container-login"]/div[1]/div/div[4]/div[1]/login-form/pm-button[1]/button').click()

nav.find_element(By.XPATH, '/html/body/app-root/app-side-nav-outer-toolbar/app-header/header/dx-toolbar/div/div[3]/div[2]/dxi-item/pm-button/button/span').click()

nav.find_element(By.XPATH,'//span[contains(text(), " Bater ponto ")]/..').click()
nav.find_element(By.CLASS_NAME, 'pm-btn-icon btn-register mt-1').click()
nav.find_element(By.CLASS_NAME, 'pm-button').click()
nav.find_element(By.CLASS_NAME, 'pm-btn-icon').click()


nav.find_element(By.CLASS_NAME, 'btn-register').click()
nav.find_element(By.CSS_SELECTOR, 'pm-button.pm-btn-icon.btn-register button').click()
nav.find_element(By.XPATH, '/html/body/app-root/app-side-nav-outer-toolbar/dx-drawer/div/div[2]/dx-scroll-view/div[1]/div/div[1]/div[2]/div[1]/app-container/time-card-register/div/div[2]/div[2]/pm-time-card-register/pm-card/div/div[2]/div[1]/div[2]/div/pm-button/button').click()

clickable = nav.find_element(By.XPATH, '/html/body/app-root/app-side-nav-outer-toolbar/app-header/header/dx-toolbar/div/div[3]/div[4]/dxi-item/div[2]/announcekit/div/pm-button/button')
action = ActionChains(nav)
action.double_click(clickable).perform()
