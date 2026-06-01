from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_search_nonexistent_product():
    driver = webdriver.Chrome()

    try:
        # 1. Mở trang chủ
        driver.get("https://hoanghamobile.com/")
        driver.maximize_window()
        print("✅ Đã mở trang chủ")

        # 2. Chờ thanh tìm kiếm xuất hiện
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "kwd"))
        )

        # 3. Click vào thanh tìm kiếm
        search_box.click()

        # 4. Nhập từ khóa không tồn tại
        keyword = "Nokia Đập Đá 123"
        search_box.clear()
        search_box.send_keys(keyword)
        print(f"✅ Đã nhập từ khóa: {keyword}")

        # 5. Nhấn Enter
        search_box.send_keys(Keys.ENTER)

        # 6. Chờ trang kết quả tải
        time.sleep(5)

        # 7. Kiểm tra thông báo không tìm thấy sản phẩm
        page_source = driver.page_source.lower()

        expected_messages = [
            "không tìm thấy",
            "khong tim thay",
            "không có sản phẩm",
            "khong co san pham",
            "0 sản phẩm",
            "0 san pham"
        ]

        found = False
        for message in expected_messages:
            if message in page_source:
                found = True
                break

        if found:
            print("✅ PASS: Hiển thị thông báo không tìm thấy sản phẩm.")
        else:
            print("❌ FAIL: Không tìm thấy thông báo mong đợi.")

        print("URL hiện tại:", driver.current_url)

    except Exception as e:
        print("❌ Lỗi:", e)

    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    test_search_nonexistent_product()