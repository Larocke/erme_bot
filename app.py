import time
from selenium import webdriver

browser = webdriver.Chrome('/Users/kat/Desktop/Python/ERME-bot/chromedriver')

# Actual
# browser.get('https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161')

# Test
browser.get('https://www.bestbuy.com/site/sony-playstation-5-dualsense-wireless-controller-midnight-black/6464307.p?skuId=6464307')

buy_button = False

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

        browser.get('https://www.bestbuy.com/cart')
        
        print('Went to cart')

        browser.quit()