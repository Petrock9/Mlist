from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import wget
import pyautogui
import os
import shutil

############################
###########GET##############
############################的
try:
    location = "D:/MData/"
    shutil.rmtree(location)
except:
    time.sleep(1)

try:
    main_dir = "D:/MData"
    os.mkdir(main_dir)
except:
    time.sleep(0.5)

item_number = str(32982727203)
options = Options()
options.add_argument("user-data-dir=C:\\Users\\JC\\AppData\\Local\\Google\\Chrome\\User Data\\Profiwle 2")
driver = webdriver.Chrome(executable_path="D:\\chromedriver\\chromedriver.exe", chrome_options=options)
driver.get("https://www.mercari.com/us/item/m" + item_number)

edit_b = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/div[2]/div[3]/div[3]/div/div')
edit_b.click()

time.sleep(5)

####get pictures

try:
    __next = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.ID, "__next"))
    )

    pictures = __next.find_elements_by_tag_name("img")

    for picture in pictures:
        url = picture.get_attribute("src")
        if url[8] == 'm':
            print(url)
            wget.download(url, 'D:/MData/')

except:
    driver.quit()

# title
title = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[2]/div[2]/input')
title_txt = title.get_attribute("value")
print(title_txt)

# Description
description = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[2]/textarea')
description_txt = description.get_attribute("value")
print(description_txt)

# Category1
category1 = driver.find_element_by_xpath('//*[@id="categoryId"]/div[1]')
print(category1.text)
c1save = category1.text
time.sleep(0.5)

# Category2
category2 = driver.find_element_by_xpath('//*[@id="subCategoryId"]/div[1]')
print(category2.text)
c2save = category2.text
time.sleep(0.5)

# Category3
category3 = driver.find_element_by_xpath('//*[@id="subSubCategoryId"]/div[1]')
print(category3.text)
c3save = category3.text
time.sleep(0.5)
if c3save == "Select subcategory":
    c3save = "Other"

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

# Brand
brand = driver.find_element_by_xpath('//*[@id="downshift-0-input"]')
brand_txt = brand.get_attribute("placeholder")
print("brand is : " + brand_txt)

# Condition
condition = 0
con1 = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[6]/div[2]/div/label[1]/div/p[1]')
con1_v = con1.get_attribute("color")
if con1_v == "white":
    condition = con1

con2 = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[6]/div[2]/div/label[2]/div/p[1]')
con2_v = con2.get_attribute("color")
if con2_v == "white":
    condition = con2

con3 = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[6]/div[2]/div/label[3]/div/p[1]')
con3_v = con3.get_attribute("color")
if con3_v == "white":
    condition = con3

con4 = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[6]/div[2]/div/label[4]/div/p[1]')
con4_v = con4.get_attribute("color")
if con4_v == "white":
    condition = con4

con5 = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[6]/div[2]/div/label[5]/div/p[1]')
con5_v = con5.get_attribute("color")
if con5_v == "white":
    condition = con5

condition_text = condition.text
print("condition is " + condition.text)

# Color
color = driver.find_element_by_xpath('//*[@id="itemColorId"]/div[1]')
print(color.text)
cosave = color.text

# Size
try:
    size = driver.find_element_by_xpath('//*[@id="itemSizeId"]')
    print("Size is " + size.text)
    size_save = size.text
    time.sleep(0.5)
except:
    print('no size')
    time.sleep(0.1)

# Ship from
shipfrom = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[10]/div/div[1]/div/input')
shipfrom_txt = shipfrom.get_attribute("value")
print(shipfrom_txt)

# Dertermin if free shipping
if_free_ship = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[10]/div/div[2]/div/div/input')
if_free_ship_v = if_free_ship.get_attribute("value")

if if_free_ship_v == "Ship on your own":
    ship_condition = 1
    print("ship on your own @condition 1")
else:
    ship = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[10]/div/div[2]/div/div/input')
    ship.click()
    time.sleep(1)
    try:
        div6 = driver.find_element_by_xpath('//*[@id="root-modal"]/div/div/div/div[2]/div[6]')
        ship_condition = 3
        print("Free shipping Prepaid @condition 3")
    except:
        ship_condition = 2
        print("Free shipping Prepaid @condition 2")

    lb = driver.find_element_by_name('weight_in_pounds')
    lb_txt = lb.get_attribute("value")
    print(lb_txt + " LB")

    oz = driver.find_element_by_name('weight_in_ounces')
    oz_txt = oz.get_attribute("value")
    print(oz_txt + " OZ")
    # else:
    #     ship = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[10]/div/div[2]/div/div/input')
    #     ship.click()
    #     time.sleep(1)
    #     ship_c = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[1]/div[1]/div/span/svg')
    #     ship_c_v = ship_c.get_attribute("fill")
    #     print(ship_c_v)
    #
    #     if ship_c_v == "#C4C4C4":
    #         ship_condition = 2
    #         print("Not free shipping @condition 2")
    #         lb = driver.find_element_by_name('weight_in_pounds')
    #         lb_txt = lb.get_attribute("value")
    #         print(lb_txt + " LB")
    #
    #         oz = driver.find_element_by_name('weight_in_ounces')
    #         oz_txt = oz.get_attribute("value")
    #         print(oz_txt + " OZ")
    #     elif ship_c_v == "#5E6DF2":
    #         ship_condition = 3
    #         print("Free shipping Prepaid @condition 3")
    #         lb = driver.find_element_by_name('weight_in_pounds')
    #         lb_txt = lb.get_attribute("value")
    #         print(lb_txt + " LB")
    #
    #         oz = driver.find_element_by_name('weight_in_ounces')
    #         oz_txt = oz.get_attribute("value")
    #         print(oz_txt + " OZ")
    #     # Close shipping
    calc_s = driver.find_element_by_xpath('//*[@id="root-modal"]/div/div/div/div[1]/button/img')
    calc_s.click()

# price
price = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[11]/div[2]/input')
price_txt = price.get_attribute("value")
print("Product price is " + price_txt)

############################
###########PUT##############
############################
time.sleep(1)
driver.get("https://www.mercari.com/sell/")
time.sleep(2)

upload = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[1]/div[4]/div/div')
upload.click()

time.sleep(1)
pyautogui.click(300, 300)
time.sleep(0.5)
pyautogui.hotkey('ctrlleft', 'a')
pyautogui.press('enter')

# Put title
put_title = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[2]/div[2]/input')
put_title.send_keys(title_txt)

# Put Description
put_description = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[2]/textarea')
put_description.send_keys(description_txt)

# Put Brand
print(brand_txt)
put_brand = driver.find_element_by_xpath('//*[@id="downshift-0-input"]')

# Put Condition
if condition_text == "New":
    put_item_condition = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[6]/div[2]/div/label[1]/div/p[1]')
    put_item_condition.click()
elif condition_text == "Like new":
    put_item_condition = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[6]/div[2]/div/label[2]/div/p[1]')
    put_item_condition.click()
elif condition_text == "Good":
    put_item_condition = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[6]/div[2]/div/label[3]/div/p[1]')
    put_item_condition.click()
elif condition_text == "Fair":
    put_item_condition = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[6]/div[2]/div/label[4]/div/p[1]')
    put_item_condition.click()
elif condition_text == "Poor":
    put_item_condition = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[6]/div[2]/div/label[5]/div/p[1]')
    put_item_condition.click()

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

# Put Category2
try:
    put_category2 = driver.find_element_by_xpath('//*[@id="subCategoryId"]/div[1]')
    put_category2.click()
    time.sleep(0.5)
    cat2s = driver.find_elements_by_tag_name("li")
    for cat2 in cat2s:
        option2 = cat2

        if option2.text == c2save:
            op2 = option2.get_attribute('id')
            oop2 = driver.find_element_by_id(op2)
            oop2.click()
except:
    time.sleep(1)

# Put Category3
try:
    put_category3 = driver.find_element_by_xpath('//*[@id="subSubCategoryId"]/div[1]')
    put_category3.click()
    time.sleep(0.5)
    cat3s = driver.find_elements_by_tag_name("li")
    for cat3 in cat3s:
        option3 = cat3
        print(option3.text)
        if option3.text == c3save:
            op3 = option3.get_attribute('id')
            oop3 = driver.find_element_by_id(op3)
            oop3.click()
except:
    time.sleep(1)

# Put color
try:
    put_color = driver.find_element_by_xpath('//*[@id="itemColorId"]/div[1]')
    put_color.click()
    time.sleep(0.5)
    colors = driver.find_elements_by_tag_name("li")
    for color in colors:
        co = color
        print(co.text)
        if co.text == cosave:
            coo = color.get_attribute('id')
            ccoo = driver.find_element_by_id(coo)
            ccoo.click()
except:
    time.sleep(0.1)

# Put Size
try:
    put_size = driver.find_element_by_xpath('//*[@id="itemSizeId"]')
    put_size.click()
    time.sleep(0.5)
    p_sizes = driver.find_elements_by_tag_name("li")
    for p_size in p_sizes:
        size_option = p_size
        print(size_option.text)
        if size_option.text == size_save:
            ppsize = size_option.get_attribute('id')
            clsize = driver.find_element_by_id(ppsize)
            clsize.click()
except:
    time.sleep(1)

# putships from
put_sf = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[10]/div/div[1]/div/input')
put_sf.send_keys(shipfrom_txt)

# put shippping
put_shipping = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[10]/div/div[2]/div/div/input')
put_shipping.click()
time.sleep(1)

try:
    before_edit = driver.find_element_by_xpath('//*[@data-testid="EditShippingButton"]')
    before_edit.click()
except:
    print("no before you edit warning")
    time.sleep(0.1)

# click_edit = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[10]/div/div[2]/div/div/input')
# click_edit.click()

if ship_condition == 1:
    f_ship = driver.find_element_by_xpath('//*[@id="offerShippingYes"]')
    f_ship.click()
    time.sleep(0.2)

    ship_own = driver.find_element_by_xpath('//*[@data-testid="ShipYourOwnButton"]')
    ship_own.click()
    time.sleep(0.2)

    put_calc = driver.find_element_by_xpath('//*[@data-testid="CalculateShippingButton"]')
    put_calc.click()
    time.sleep(0.4)

if ship_condition == 2:
    nf_ship = driver.find_element_by_xpath('//*[@id="offerShippingNo"]')
    nf_ship.click()
    time.sleep(0.4)

    put_lb = driver.find_element_by_name('weight_in_pounds')
    put_lb.send_keys(lb_txt)
    put_oz = driver.find_element_by_name('weight_in_ounces')
    put_oz.send_keys(oz_txt)
    time.sleep(0.4)

    put_calc = driver.find_element_by_xpath('//*[@data-testid="CalculateShippingButton"]')
    put_calc.click()
    time.sleep(0.4)
    sel_carr = driver.find_element_by_xpath('//*[@id="root-modal"]/div/div/div/div[2]/div[2]/div[1]/div')
    sel_carr.click()
    time.sleep(0.4)
    save2 = driver.find_element_by_xpath('//*[@id="root-modal"]/div/div/div/div[2]/div[3]/button')
    save2.click()
    time.sleep(0.4)

if ship_condition == 3:
    f_ship = driver.find_element_by_xpath('//*[@id="offerShippingYes"]')
    f_ship.click()
    time.sleep(0.2)

    ship_pp = driver.find_element_by_xpath('//*[@data-testid="PrepaidButton"]')
    ship_pp.click()
    time.sleep(0.2)

    put_lb = driver.find_element_by_name('weight_in_pounds')
    put_lb.send_keys(lb_txt)
    put_oz = driver.find_element_by_name('weight_in_ounces')
    put_oz.send_keys(oz_txt)
    time.sleep(0.4)

    put_calc = driver.find_element_by_xpath('//*[@data-testid="CalculateShippingButton"]')
    put_calc.click()
    time.sleep(0.4)
    sel_carr = driver.find_element_by_xpath('//*[@id="root-modal"]/div/div/div/div[2]/div[2]/div[1]/div')
    sel_carr.click()
    time.sleep(0.4)
    save2 = driver.find_element_by_xpath('//*[@id="root-modal"]/div/div/div/div[2]/div[3]/button')
    save2.click()
    time.sleep(0.4)

# put pricing
# put_price = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[11]/div[2]/input')
# put_price.send_keys(price_txt)


time.sleep(3)
###LIST!!!!!

time.sleep(3)
if_price = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[16]/form/button')
if_botton = if_price.get_attribute('disabled')

if if_botton:
    print("Item " + item_number + " re-list FAILED")
    driver.quit
else:
    list_p = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[16]/form/button')
    list_p.click()
    time.sleep(3)
    ###Delete Original
    driver.get("https://www.mercari.com/us/item/m" + item_number)

    edit_b = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/div[2]/div[3]/div[3]/div/div')
    edit_b.click()

    time.sleep(4)

    dele = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[17]/div[1]/button[2]')
    dele.click()
    time.sleep(2)
# end
driver.quit()
