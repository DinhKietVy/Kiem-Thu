import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_TC_LOG_14(driver):


    try:
        driver.get("https://member.hoanghamobile.com/Account/Login?ReturnUrl=http://hoanghamobile.com/")

        wait = WebDriverWait(driver, 15)

        # Tìm ô nhập SĐT
        phone_input = wait.until(
            EC.presence_of_element_located((By.ID, "Phone"))
        )

        # Nhập số điện thoại
        phone_input.send_keys("098")

        time.sleep(2)

        print("Trước khi F5:", phone_input.get_attribute("value"))

        # Refresh trang
        driver.refresh()

        # Tìm lại ô nhập sau khi refresh
        phone_input = wait.until(
            EC.presence_of_element_located((By.ID, "Phone"))
        )

        actual_value = phone_input.get_attribute("value")

        print("Sau khi F5:", repr(actual_value))

        # Kiểm tra kết quả
        if actual_value == "":
            print("✅ PASS - Ô nhập liệu được làm trống sau khi tải lại trang")
        else:
            print("❌ FAIL - Dữ liệu vẫn còn sau khi tải lại trang")
            pytest.fail('Test Failed! See log above.')

    except Exception as e:
        print("Lỗi:", e)

        time.sleep(5)

