from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep
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
