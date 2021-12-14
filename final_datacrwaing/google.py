from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

def crawling_img(name):
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element_by_name("q")
    elem.send_keys(name)
    elem.send_keys(Keys.RETURN)

    #
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")  # �������� ���̸� �ڹٽ�ũ��Ʈ�� ã��
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # ������ ������ ��ũ���� ����
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    imgs = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    dir = ".\img" + "\\" + name

    createDirectory(dir) #���� ����
    count = 1
    for img in imgs:
        try:
            img.click()
            time.sleep(2)
            imgUrl = driver.find_element_by_xpath(
                '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img').get_attribute(
                "src")
            path = "C:img\\" + name + "\\"
            urllib.request.urlretrieve(imgUrl, path + name + str(count) + ".jpg")
            count = count + 1
            if count >= 550:
                break
        except:
            pass
    driver.close()
flowers = ["�ײ�"]

for flower in flowers:
    crawling_img(��)