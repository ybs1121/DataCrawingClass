from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
import time
from selenium import webdriver
#
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")


name = input("품종 : ")
english_name = input("품종(영어): ")
os.mkdir("링크" + english_name)

#driver = webdriver.Chrome('chromedriver',options=options)
driver = webdriver.Chrome(options=options)
driver.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=")
# assert "Python" in driver.title2
elem = driver.find_element_by_name("query") #검색창 찾기
# elem.clear()

elem.send_keys(name)
elem.send_keys(Keys.RETURN) #엔터키 입력

#sroll

SCROLL_PAUSE_TIME = 1.0

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        #break
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

# driver.find_elements_by_css_selector(".rg_i.Q4LuWd").click()
# time.sleep(3) # 이미지 로딩 시간 기다려주기
# imgae_URL = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
# urllib.request.urlretrieve(imgae_URL,"test.jpg")

images = driver.find_elements_by_css_selector("._image._listImage")
#images = driver.find_elements_by_xpath("/html/body/div[3]/div[2]/div/div[1]/section/div/div[1]/div[1]/div[3]/div/div[1]/a/img")
count = 1000
print(len(images))

time0 = time.time()
for image in images:
    try:
        image.click()
        time.sleep(1) # 이미지 로딩 시간 기다려주기
        try:
            #imgae_URL= driver.find_element_by_class_name("._image._listImage").get_attribute("src")
            imgae_URL = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/section/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div[1]/div[1]/img").get_attribute("src")
            urllib.request.urlretrieve(imgae_URL,"경로/" +english_name+ "/"+english_name+"."+str(count)+".jpg")
            count = count + 1
            print(str(count)+".jpg")
        except:
            pass

    except:
        pass



# assert "No results found." not in driver.page_source
driver.close()
