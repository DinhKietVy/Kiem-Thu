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

sku = "2510DRA23ETM"

try:
    # ====================== 1. MỞ TRANG SẢN PHẨM ======================
    driver.get("https://hoanghamobile.com/dien-thoai/xiaomi-redmi-note-15-6gb-128gb")

    add_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.add-buy.add-cart.inventory")
        )
    )

    driver.execute_script("arguments[0].click();", add_button)
    print("✅ Đã thêm sản phẩm vào giỏ hàng")

    time.sleep(3)

    # ====================== 2. VÀO GIỎ HÀNG ======================
    driver.get("https://hoanghamobile.com/gio-hang")

    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-items"))
    )

    # ====================== 3. TĂNG SỐ LƯỢNG TỪ 1 -> 3 ======================
    for i in range(2):
        plus_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"button[data-sku='{sku}']")
            )
        )

        driver.execute_script("arguments[0].click();", plus_button)

        time.sleep(2)

        print(f"✅ Đã bấm + lần {i + 1}")

    print("✅ Đã tăng số lượng lên 3")

    # ====================== 4. REFRESH TRANG ======================
    driver.refresh()

    print("✅ Đã tải lại trang (F5)")

    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-items"))
    )

    time.sleep(2)

    # ====================== 5. KIỂM TRA VALUE ======================
    quantity_input = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, f"//button[@data-sku='{sku}']/preceding-sibling::input")
        )
    )

    current_value = quantity_input.get_attribute("value")

    print("Số lượng sau refresh:", current_value)

    if current_value == "3":
        print("✅ PASS: Thuộc tính value vẫn là 3 sau khi refresh")
    else:
        print(f"❌ FAIL: Mong đợi 3, thực tế = {current_value}")

except Exception as e:
    print("❌ Lỗi:", str(e))

finally:
    time.sleep(5)
    driver.quit()