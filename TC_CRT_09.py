from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(), options=options)
wait = WebDriverWait(driver, 20)

try:
    # ====================== TAB 1: THÊM SẢN PHẨM ======================
    driver.get("https://hoanghamobile.com/dien-thoai/xiaomi-redmi-note-15-6gb-128gb")
    print("✅ Mở trang sản phẩm")

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    add_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.add-buy.add-cart.inventory")
        )
    )

    driver.execute_script("arguments[0].click();", add_button)
    print("✅ Đã thêm sản phẩm vào giỏ hàng")

    time.sleep(3)

    # ====================== TAB 2 ======================
    driver.switch_to.new_window("tab")
    print("✅ Đã mở Tab 2")

    driver.get("https://hoanghamobile.com/gio-hang")

    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".cart-items")
        )
    )

    time.sleep(2)

    # ====================== KIỂM TRA ĐỒNG BỘ ======================
    cart_items = driver.find_elements(
        By.CSS_SELECTOR,
        ".cart-items > .item"
    )

    actual_count = len(cart_items)

    print(f"Số lượng sản phẩm trong giỏ: {actual_count}")

    if actual_count == 1:
        print("✅ PASS: Giỏ hàng được đồng bộ giữa 2 tab")
    else:
        print(f"❌ FAIL: Mong đợi 1 sản phẩm, thực tế {actual_count}")

except Exception as e:
    print("❌ Lỗi:", str(e))

finally:
    time.sleep(5)
    driver.quit()