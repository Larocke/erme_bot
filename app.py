import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('/Users/kat/Desktop/Python/ERME-bot/chromedriver')

# Actual
# browser.get('https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161')

# Test
browser.get('https://www.bestbuy.com/site/sony-playstation-5-dualsense-wireless-controller-midnight-black/6464307.p?skuId=6464307')

buy_button = False

def go_to(class_name):
    try:
        element = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, class_name))
        )
        go_to_cart_btn = browser.find_element_by_class_name(class_name)
        go_to_cart_btn.click()
        print('Went to', class_name)
    except:
        browser.quit()
        print('Quit because was not able get to', class_name)


while not buy_button:
    try:
        # finding a unique class to the disabled sold out button
        add_to_cart_btn = browser.find_element_by_class_name('c-button-disabled')
        
        print('Refresh')
        
        time.sleep(1)
        browser.refresh()
        
    except:
        buy_button = True
        
        add_to_cart_btn = browser.find_element_by_class_name('c-button-primary')
        add_to_cart_btn.click()
        print('Added to cart')

        go_to('go-to-cart-button')
        go_to('checkout-buttons__checkout')
        go_to('cia-guest-content')

        

        
        

