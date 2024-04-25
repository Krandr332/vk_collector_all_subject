# -*- coding: cp1251 -*-
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

from config import username, password


def sel():
    # �������� ���������� ���� � �����
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, 'add_products.csv')

    url = '**********/add-product-to-user/'

    # ������ ��� ��������������

    # ��������� Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # ��������� headless ������

    # ������ ��������
    driver = webdriver.Chrome(options=chrome_options)  # ������� ���� � ��������, ���� �� � ��� � ������ �����
    driver.get(url)

    # �����������
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    # �������� �������� �������� � ������ ��� �������� �����
    file_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))

    # �������� �����
    file_input.send_keys(file_path)

    # �������� �����
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(@class, 'mt-2') and contains(@class, 'send_button')]")))
    submit_button.click()
    time.sleep(5)

    driver.quit()
