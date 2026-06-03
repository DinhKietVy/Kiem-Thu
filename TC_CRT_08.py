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
    print("✅ Mở trang sản phẩm")

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(2)

    # ====================== 2. THÊM VÀO GIỎ HÀNG ======================
    add_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.add-buy.add-cart.inventory")
        )
    )

    driver.execute_script("arguments[0].click();", add_button)
    print("✅ Đã thêm sản phẩm vào giỏ hàng")

    time.sleep(3)

    # ====================== 3. VÀO GIỎ HÀNG ======================
    driver.get("https://hoanghamobile.com/gio-hang")
    print("✅ Đã vào giỏ hàng")

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(3)

    # ====================== 4. TĂNG SỐ LƯỢNG NHIỀU LẦN ======================
    plus_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//button[@data-sku='{sku}']")
        )
    )

    print("✅ Bắt đầu tăng số lượng")

    # Tăng 50 lần để kiểm tra giới hạn tồn kho
    for i in range(50):
        try:
            driver.execute_script("arguments[0].click();", plus_button)
            time.sleep(0.3)
        except:
            break

    print("✅ Đã thử tăng số lượng 50 lần")

    time.sleep(3)

    # ====================== 5. KIỂM TRA KẾT QUẢ ======================
    page_source = driver.page_source.lower()

    if ("vượt quá số lượng tồn kho" in page_source or
        "hết hàng" in page_source or
        "không đủ số lượng" in page_source):
        print("✅ PASS: Hiển thị thông báo vượt quá số lượng tồn kho")

    else:
        # Tìm ô nhập số lượng nếu có
        try:
            quantity_input = driver.find_element(
                By.XPATH,
                f"//button[@data-sku='{sku}']/parent::*//input"
            )

            current_value = quantity_input.get_attribute("value")
            print(f"Số lượng hiện tại: {current_value}")

            if current_value == "10":
                print("✅ PASS: Hệ thống tự giới hạn số lượng về 10")
            else:
                print(f"⚠️ Không thấy thông báo lỗi. Giá trị hiện tại = {current_value}")

        except:
            print("⚠️ Không tìm được ô số lượng để kiểm tra")

except Exception as e:
    print("❌ Lỗi:", str(e))

finally:
    time.sleep(5)
    driver.quit()