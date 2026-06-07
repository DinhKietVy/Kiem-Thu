import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback


def test_TC_CRT_06(driver):



    wait = WebDriverWait(driver, 20)

    try:
        # Mở trang chủ
        driver.get("https://hoanghamobile.com")
        print("✅ Đã mở trang chủ")

        # Bấm icon Giỏ hàng
        cart_icon = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/gio-hang']"))
        )
        driver.execute_script("arguments[0].click();", cart_icon)

        print("✅ Đã mở trang giỏ hàng")

        # Kiểm tra thông báo giỏ hàng trống
        empty_cart = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//strong[contains(text(),'Hiện chưa có sản phẩm nào trong giỏ hàng')]")
        )
    )

        if empty_cart.is_displayed():
            print("✅ PASS: Hiển thị 'Giỏ hàng của bạn đang trống'")
        else:
            print("❌ FAIL: Không hiển thị thông báo")
            pytest.fail('Test Failed! See log above.')
    except Exception:
        traceback.print_exc()

        time.sleep(5)

