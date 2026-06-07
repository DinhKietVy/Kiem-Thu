import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import unquote
import time


def test_TC_SRC_10(driver):

    def test_search_xss_html():

        try:
            # 1. Mở trang chủ
            driver.get("https://hoanghamobile.com/")

            # Chờ ô tìm kiếm xuất hiện
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "kwd"))
            )

            # Chuỗi kiểm thử
            payload = "<h1>Test</h1>"

            # 2. Nhập payload vào ô tìm kiếm
            search_box.clear()
            search_box.send_keys(payload)

            # 3. Nhấn Enter
            search_box.send_keys(Keys.ENTER)

            # Chờ chuyển trang
            time.sleep(3)

            # 4. Lấy URL hiện tại
            current_url = driver.current_url

            print(f"URL hiện tại: {current_url}")

            # 5. Kiểm tra payload có bị encode trên URL hay không
            if "%3C" in current_url and "%3E" in current_url:
                print("✅ PASS: Ký tự HTML đã được Encode trên URL")
            else:
                print("❌ FAIL: Payload không được Encode đúng cách")
                pytest.fail('Test Failed! See log above.')

            # 6. Kiểm tra không render thẻ HTML trên giao diện
            page_source = driver.page_source

            if "<h1>Test</h1>" not in page_source:
                print("✅ PASS: Thẻ HTML không được render")
            else:
                print("❌ FAIL: HTML được render trên trang")
                pytest.fail('Test Failed! See log above.')

            # 7. Hiển thị URL đã giải mã để tham khảo
            print("URL sau khi decode:")
            print(unquote(current_url))

        except Exception as e:
            print(f"❌ Lỗi: {e}")
            pytest.fail('Test Failed! See log above.')

            time.sleep(5)

    if __name__ == "__main__":
        test_search_xss_html()
