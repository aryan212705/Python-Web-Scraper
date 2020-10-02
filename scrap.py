import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
from math import ceil
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import random

link = "https://docs.python.org/3/library/math.html"
page = urllib.request.urlopen(link)
soup = BeautifulSoup(page,"lxml")


CAPABILITY_KEY = "pageLoadStrategy"
CAPABILITY_VALUE = "eager"
MODE = "-headless"
FIREFOX_EXECUTABLE_PATH = "geckodriver"
CHROME_EXECUTABLE_PATH = "chromedriver"
PHANTOM_EXECUTABLE_PATH = "phantomjs"
ANIME_NAME = ""
TIMEOUT = 30



main_section = soup.find("div", class_ = "section")
module_name = main_section.find("h1").get_text()
module_desc = main_section.find("p").get_text()


def start_driver():
    print("Starting webdriver")
    try:
        caps = DesiredCapabilities().FIREFOX
        caps[CAPABILITY_KEY] = CAPABILITY_VALUE
        profile = webdriver.FirefoxProfile()
        options = webdriver.FirefoxOptions()
        options.add_argument(MODE)
        driver = webdriver.Firefox(profile, executable_path=FIREFOX_EXECUTABLE_PATH, firefox_options=options, capabilities=caps)
        print("Driver started")
    except:
        try:
            caps = DesiredCapabilities().CHROME
            caps[CAPABILITY_KEY] = CAPABILITY_VALUE
            options = webdriver.ChromeOptions()
            options.add_argument(MODE)
            driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH, capabilities=caps)
            print("Driver started")
        except:
            try:
                caps = DesiredCapabilities().PHANTOMJS
                caps[CAPABILITY_KEY] = CAPABILITY_VALUE
                driver = webdriver.PhantomJS(executable_path=PHANTOM_EXECUTABLE_PATH, capabilities=caps)
                print("Driver started")
            except:
                print("Webdrivers are missing. Require at any one of these drivers:", "\n1. Geckodriver(for Firefox)\n2. Chromedriver(for Chrome)\n3. PhantomJS")
                exit()
    return driver



print(module_name, "\n")
print(module_desc, "\n\n")
section_name = []
func_name = []
func_desc = []
for section in main_section.find_all("div", class_  = "section"):
    section_name.append(section.find("h2").get_text())
    section_name.append(section.find("h3").get_text())
    section_name.append(section.find("h4").get_text())
    name, desc = [], []
    for function in section.find_all("dl", class_ = "function"):
        name.append(function.find("dt").get_text())
        desc.append(function.find("dd").get_text())
        asc.append(function.find("dh").get_text())
    func_name.append(name)
    func_desc.append(desc)

for i in range(len(section_name)):
    print(section_name[i],"\n")
    for j in range(len(func_name[i])):
        print(func_name[i][j],"\n")
        print(func_desc[i][j])
        print(func_asc[i][j])
