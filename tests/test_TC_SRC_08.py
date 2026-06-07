import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_TC_SRC_08(driver):

    def test_spam_enter_search():

        try:
            # 1. Mở trang chủ
            driver.get("https://hoanghamobile.com/")

            # Chờ ô tìm kiếm xuất hiện
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "kwd"))
            )

            # 2. Nhập từ khóa
            search_box.clear()
            search_box.send_keys("iphone")

            before_url = driver.current_url

            # 3. Spam Enter 5 lần liên tiếp
            actions = ActionChains(driver)

            for _ in range(5):
                actions.send_keys(Keys.ENTER)

            actions.perform()

            # Chờ trang tải
            WebDriverWait(driver, 10).until(
                lambda d: d.current_url != before_url
            )

            after_url = driver.current_url

            # 4. Kiểm tra đã chuyển trang
            if after_url != before_url:
                print("✅ PASS: Đã chuyển sang trang kết quả tìm kiếm")
            else:
                print("❌ FAIL: Không chuyển sang trang tìm kiếm")
                pytest.fail('Test Failed! See log above.')

            # 5. Kiểm tra trình duyệt vẫn hoạt động
            print(f"Tiêu đề: {driver.title}")
            print("✅ PASS: Trình duyệt không bị treo/crash")

            # 6. Kiểm tra chỉ có 1 tab
            if len(driver.window_handles) == 1:
                print("✅ PASS: Không mở tab thừa")
            else:
                print("❌ FAIL: Có tab phát sinh bất thường")
                pytest.fail('Test Failed! See log above.')

        except Exception as e:
            print(f"❌ Lỗi: {e}")
            pytest.fail('Test Failed! See log above.')

            time.sleep(5)

    if __name__ == "__main__":
        test_spam_enter_search()
