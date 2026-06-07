import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def test_TC_LOG_09(driver):

    # Cấu hình Chrome


    try:
        # Mở trang đăng nhập
        driver.get("https://member.hoanghamobile.com/Account/Login?ReturnUrl=http://hoanghamobile.com/")
        print("Đã mở trang đăng nhập")

        wait = WebDriverWait(driver, 15)

        # Tìm ô nhập số điện thoại
        phone_input = wait.until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//input[contains(@placeholder,'điện thoại') or "
                 "contains(@placeholder,'Điện thoại') or "
                 "@type='tel']")
            )
        )

        # Nhập dấu cách
        phone_input.clear()
        phone_input.send_keys("   ")
        print("Đã nhập dấu cách vào ô SĐT")

        # Nhấn nút Tiếp tục
        continue_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(.,'TIẾP TỤC') or contains(.,'Tiếp tục')]")
            )
        )
        continue_btn.click()
        print("Đã nhấn nút Tiếp tục")

        # Chờ thông báo lỗi xuất hiện
        error_msg = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(text(),'Vui lòng nhập số điện thoại của bạn.')]"
                )
            )
        )

        actual_text = error_msg.text.strip()

        if actual_text == "Vui lòng nhập số điện thoại của bạn.":
            print("✅ TEST PASS")
            print("Thông báo hiển thị đúng:", actual_text)
        else:
            print("❌ TEST FAIL")
            pytest.fail('Test Failed! See log above.')
            print("Thông báo thực tế:", actual_text)

    except TimeoutException:
        print("❌ TEST FAIL: Không tìm thấy thông báo lỗi")
        pytest.fail('Test Failed! See log above.')

    except Exception as e:
        print("❌ Lỗi:", e)
        pytest.fail('Test Failed! See log above.')

        time.sleep(5)

