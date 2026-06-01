from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_empty_search():
    driver = webdriver.Chrome()

    try:
        # 1. Mở trang chủ
        driver.get("https://hoanghamobile.com/")
        driver.maximize_window()

        # Chờ trang tải
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "kwd"))
        )

        # Lưu URL ban đầu
        original_url = driver.current_url

        # 2. Click vào thanh tìm kiếm
        search_box = driver.find_element(By.ID, "kwd")
        search_box.click()

        # 3. Để trống ô tìm kiếm
        search_box.clear()

        # 4. Nhấn Enter
        search_box.send_keys(Keys.ENTER)

        # Chờ phản hồi
        time.sleep(3)

        # 5. Lấy URL hiện tại
        current_url = driver.current_url

        # 6. Kiểm tra URL không thay đổi
        if current_url == original_url:
            print("✅ PASS: URL không thay đổi")
        else:
            print(f"❌ FAIL: URL đã thay đổi")
            print(f"Ban đầu: {original_url}")
            print(f"Hiện tại: {current_url}")

        # 7. Kiểm tra không chuyển sang trang tìm kiếm
        if "/tim-kiem" not in current_url.lower() and "search" not in current_url.lower():
            print("✅ PASS: Vẫn ở trang hiện tại")
        else:
            print("❌ FAIL: Đã chuyển sang trang tìm kiếm")

    except Exception as e:
        print(f"❌ Lỗi: {e}")

    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    test_empty_search()