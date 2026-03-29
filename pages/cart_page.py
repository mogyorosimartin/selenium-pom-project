from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage





class CartPage(BasePage):
    
    PRODUCT = (By.XPATH, "(//div[@class='product-image-wrapper'])[{}]")
    ADD_TO_CART = (By.XPATH, "(//a[contains(text(),'Add to cart')])[{}]")
    CONTINUE_BTN = (By.CSS_SELECTOR, ".btn.btn-success.close-modal.btn-block")
    CART_ROWS = (By.XPATH, "//tr[starts-with(@id, 'product-')]")
    PRICE_TEXT = (By.CLASS_NAME, "cart_price")
    QUANTITY_TEXT = (By.CLASS_NAME, "cart_quantity")
    TOTAL_PRICE = (By.CLASS_NAME, "cart_total_price")
    VIEW_CART_BTN = (By.LINK_TEXT, "View Cart")
    
    def add_to_cart(self,index):
        actions = ActionChains(self.driver)

        product = self.find(self.format_locator(self.PRODUCT, index))
        actions.move_to_element(product).perform()

        add_btn = product.find_element(By.XPATH, ".//a[contains(text(),'Add to cart')]")
        add_btn.click()
    
    def click_continue(self):
        self.click(self.CONTINUE_BTN)
        
    def click_cart(self):
        self.click(self.VIEW_CART_BTN)
    
    def get_cart_items(self):
        return self.driver.find_elements(*self.CART_ROWS)
    
    def get_cart_data(self):
        cart_rows = self.driver.find_elements(*self.CART_ROWS)
        data = []
        for row in cart_rows:
            price_text = row.find_element(*self.PRICE_TEXT).text
            quantity_text = row.find_element(*self.QUANTITY_TEXT).text
            total_text = row.find_element(*self.TOTAL_PRICE).text

            price = int(price_text.replace("Rs. ", "").strip())
            quantity = int(quantity_text.strip())
            total = int(total_text.replace("Rs. ", "").strip())

            data.append((price, quantity, total))
    
        return data
            