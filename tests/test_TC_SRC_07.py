import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_TC_SRC_07(driver):

    def test_search_max_length():

        try:
            # 1. Mở trang chủ
            driver.get("https://hoanghamobile.com/")

            # 2. Chờ ô tìm kiếm xuất hiện
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "kwd"))
            )

            # 3. Tạo chuỗi 300 ký tự 'a'
            long_text = "a" * 300

            # 4. Nhập vào ô tìm kiếm
            search_box.clear()
            search_box.send_keys(long_text)

            # 5. Lấy giá trị thực tế trong ô tìm kiếm
            actual_value = search_box.get_attribute("value")
            actual_length = len(actual_value)

            print(f"Độ dài đã nhập: {len(long_text)}")
            print(f"Độ dài thực tế trong ô tìm kiếm: {actual_length}")

            # 6. Nhấn Enter
            search_box.send_keys(Keys.ENTER)

            time.sleep(3)

            # 7. Kiểm tra hệ thống không bị crash
            if driver.title:
                print("✅ PASS: Hệ thống vẫn hoạt động bình thường")
            else:
                print("❌ FAIL: Trang có dấu hiệu lỗi")
                pytest.fail('Test Failed! See log above.')

            # 8. Kiểm tra giới hạn ký tự
            MAX_LENGTH = 255

            if actual_length <= MAX_LENGTH:
                print(f"✅ PASS: Độ dài <= {MAX_LENGTH}")
            else:
                print(f"❌ FAIL: Độ dài = {actual_length} > {MAX_LENGTH}")
                pytest.fail('Test Failed! See log above.')

            # 9. In URL để kiểm tra thêm
            print("URL hiện tại:", driver.current_url)

        except Exception as e:
            print("❌ Lỗi:", e)
            pytest.fail('Test Failed! See log above.')

            time.sleep(5)

    if __name__ == "__main__":
        test_search_max_length()
