import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time


def test_TC_CRT_12(driver):


    wait = WebDriverWait(driver, 20)

    try:
        # ====================== 1. MỞ TRANG SẢN PHẨM ======================
        driver.get("https://hoanghamobile.com/dien-thoai/xiaomi-redmi-note-15-6gb-128gb")

        wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

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

        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".cart-items")
            )
        )

        time.sleep(2)

        # ====================== 4. COPY SỐ 10 ======================
        pyperclip.copy("10")

        # ====================== 5. TÌM Ô SỐ LƯỢNG ======================
        quantity_input = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".number input")
            )
        )

        old_value = quantity_input.get_attribute("value")
        print("Số lượng ban đầu:", old_value)

        # ====================== 6. PASTE GIÁ TRỊ 10 ======================

        # Click bằng JavaScript thay vì click thường
        driver.execute_script(
            "arguments[0].click();",
            quantity_input
        )

        quantity_input.send_keys(Keys.CONTROL + "a")
        quantity_input.send_keys(Keys.CONTROL + "v")

        print("✅ Đã paste số 10")

        # kích hoạt onchange
        quantity_input.send_keys(Keys.TAB)

        # chờ phần tử cũ bị reload
        try:
            wait.until(EC.staleness_of(quantity_input))
        except:
            pass

        time.sleep(3)

        # ====================== 7. TÌM LẠI INPUT SAU KHI AJAX UPDATE ======================
        quantity_input = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".number input")
            )
        )

        new_value = quantity_input.get_attribute("value")

        print("Số lượng sau khi paste:", new_value)

        # ====================== 8. KIỂM TRA KẾT QUẢ ======================
        if new_value == "10":
            print("✅ PASS: Paste thành công, số lượng = 10")
        else:
            print(f"❌ FAIL: Mong đợi 10, thực tế = {new_value}")
            pytest.fail('Test Failed! See log above.')

    except Exception as e:
        print("❌ Lỗi:", str(e))
        pytest.fail('Test Failed! See log above.')

        time.sleep(5)

