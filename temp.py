from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.add_argument("user-data-dir=C:\\Users\\JC\\AppData\\Local\\Google\\Chrome\\User Data\\Profiwle 2")
driver = webdriver.Chrome(executable_path="D:\\chromedriver\\chromedriver.exe", chrome_options=options)
#
#
#
#
#
################For test##################
#
#
# Category1
category1 = driver.find_element_by_xpath('//*[@id="categoryId"]/div[1]')
print(category1.text)
c1save = category1.text
time.sleep(0.5)


# Put Category1
try:
    put_category1 = driver.find_element_by_xpath('//*[@id="categoryId"]/div[1]')
    put_category1.click()
    time.sleep(0.5)
    cat1s = driver.find_elements_by_tag_name("li")
    for cat1 in cat1s:
        option1 = cat1

        if option1.text == c1save:
            op1 = option1.get_attribute('id')
            oop1 = driver.find_element_by_id(op1)
            oop1.click()
except:
    time.sleep(2)
######################################################
#
#
#
# Get Shaft Height
try:
    shaft_height = driver.find_element_by_xpath('//*[@id="customItemFieldId_Shaft Height"]')
    print(shaft_height.text)
    shaft_height_save = shaft_height.text
    time.sleep(0.2)
except:
    print("no shaft height")

# Get End Use
try:
    end_use = driver.find_element_by_xpath('//*[@id="customItemFieldId_End Use"]')
    print(end_use.text)
    end_use_save = end_use.text
    time.sleep(0.2)
except:
    print("no end use")

# Get Heel Height
try:
    heel_height = driver.find_element_by_xpath('//*[@id="customItemFieldId_Heel Height"]')
    print(heel_height.text)
    heel_height_save = heel_height.text
    time.sleep(0.2)
except:
    print("no heel height")

# Get Material
try:
    material = driver.find_element_by_xpath('//*[@id="customItemFieldId_Material"]')
    print(material.text)
    material_save = material.text
    time.sleep(0.2)
except:
    print("no material")


# Put Shaft Height
try:
    put_shaft_height = driver.find_element_by_xpath('//*[@id="customItemFieldId_Shaft Height"]')
    put_shaft_height.click()
    time.sleep(0.2)
    cat1s = driver.find_elements_by_tag_name("li")
    for cat1 in cat1s:
        option1 = cat1

        if option1.text == shaft_height_save:
            op1 = option1.get_attribute('id')
            oop1 = driver.find_element_by_id(op1)
            oop1.click()
except:
    time.sleep(0.2)

# Put End Use
try:
    put_end_use = driver.find_element_by_xpath('//*[@id="customItemFieldId_End Use"]')
    put_end_use.click()
    time.sleep(0.2)
    cat1s = driver.find_elements_by_tag_name("li")
    for cat1 in cat1s:
        option1 = cat1

        if option1.text == end_use_save:
            op1 = option1.get_attribute('id')
            oop1 = driver.find_element_by_id(op1)
            oop1.click()
except:
    time.sleep(0.2)

# Put Heel Height
try:
    put_heel_height = driver.find_element_by_xpath('//*[@id="customItemFieldId_Heel Height"]')
    put_heel_height.click()
    time.sleep(0.2)
    cat1s = driver.find_elements_by_tag_name("li")
    for cat1 in cat1s:
        option1 = cat1

        if option1.text == heel_height_save:
            op1 = option1.get_attribute('id')
            oop1 = driver.find_element_by_id(op1)
            oop1.click()
except:
    time.sleep(0.2)

# Put Material
try:
    put_material = driver.find_element_by_xpath('//*[@id="customItemFieldId_Material"]')
    put_material.click()
    time.sleep(0.2)
    cat1s = driver.find_elements_by_tag_name("li")
    for cat1 in cat1s:
        option1 = cat1

        if option1.text == material_save:
            op1 = option1.get_attribute('id')
            oop1 = driver.find_element_by_id(op1)
            oop1.click()
except:
    time.sleep(0.2)

##########################
#############################

# Get Dress Occasion
try:
    dress_occasion = driver.find_element_by_xpath('//*[@id="customItemFieldId_Dress Occasion"]')
    print(dress_occasion.text)
    dress_occasion_save = dress_occasion.text
    time.sleep(0.2)
except:
    print("no dress occasion")

# Get Dress Style
try:
    dress_style = driver.find_element_by_xpath('//*[@id="customItemFieldId_Dress Style"]/div[1]')
    print(dress_style.text)
    dress_style_save = dress_style.text
    time.sleep(0.2)
except:
    print("no dress style")

# Put Dress Occasion
try:
    put_dress_occasion = driver.find_element_by_xpath('//*[@id="customItemFieldId_Dress Occasion"]')
    put_dress_occasion.click()
    time.sleep(0.2)
    cat1s = driver.find_elements_by_tag_name("li")
    for cat1 in cat1s:
        option1 = cat1

        if option1.text == dress_occasion_save:
            op1 = option1.get_attribute('id')
            oop1 = driver.find_element_by_id(op1)
            oop1.click()
except:
    time.sleep(0.2)

# Put Dress Style
try:
    put_dress_style = driver.find_element_by_xpath('//*[@id="customItemFieldId_Dress Style"]/div[1]')
    put_dress_style.click()
    time.sleep(0.2)
    cat1s = driver.find_elements_by_tag_name("li")
    for cat1 in cat1s:
        option1 = cat1

        if option1.text == dress_style_save:
            op1 = option1.get_attribute('id')
            oop1 = driver.find_element_by_id(op1)
            oop1.click()
except:
    time.sleep(0.2)