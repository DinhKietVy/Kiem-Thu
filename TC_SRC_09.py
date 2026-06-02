from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_clear_search_text():
    driver = webdriver.Chrome()

    try:
        # 1. Mở trang chủ
        driver.get("https://hoanghamobile.com/")
        driver.maximize_window()

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

    except Exception as e:
        print(f"❌ Lỗi: {e}")

    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    test_clear_search_text()