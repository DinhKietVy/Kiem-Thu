import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_TC_SRC_09(driver):

    def test_clear_search_text():

        try:
            # 1. Mở trang chủ
            driver.get("https://hoanghamobile.com/")

            wait = WebDriverWait(driver, 10)

            # 2. Tìm ô tìm kiếm
            search_box = wait.until(
                EC.presence_of_element_located((By.ID, "kwd"))
            )

            # 3. Nhập text
            search_box.clear()
            search_box.send_keys("abc")

            time.sleep(1)

            # 4. Click nút X
            clear_btn = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-clear"))
            )
            clear_btn.click()

            time.sleep(1)

            # 5. Kiểm tra ô tìm kiếm đã rỗng
            current_text = search_box.get_attribute("value")

            if current_text == "":
                print("✅ PASS: Ô tìm kiếm đã được làm trống")
            else:
                print(f"❌ FAIL: Ô tìm kiếm vẫn còn dữ liệu: '{current_text}'")
                pytest.fail('Test Failed! See log above.')

        except Exception as e:
            print(f"❌ Lỗi: {e}")
            pytest.fail('Test Failed! See log above.')

            time.sleep(5)

    if __name__ == "__main__":
        test_clear_search_text()
