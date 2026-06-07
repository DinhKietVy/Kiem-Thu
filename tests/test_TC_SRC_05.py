import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_TC_SRC_05(driver):

    def test_search_nonexistent_product():

        try:
            # 1. Mở trang chủ
            driver.get("https://hoanghamobile.com/")
            print("✅ Đã mở trang chủ")

            wait = WebDriverWait(driver, 10)

            # 2. Chờ thanh tìm kiếm xuất hiện trong DOM
            search_box = wait.until(
                EC.presence_of_element_located((By.ID, "kwd"))
            )

            # --- ĐOẠN XỬ LÝ POPUP QUẢNG CÁO ĐÈ GIAO DIỆN ---
            try:
                # Tìm và tắt modal quảng cáo dựa trên class 'close-modal' của thư viện jquery-modal
                close_popup_btn = wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'close-modal')]"))
                )
                close_popup_btn.click()
                print("✅ Đã tự động tắt popup quảng cáo.")
                time.sleep(1)  # Chờ hiệu ứng đóng của modal hoàn tất
            except:
                # Nếu không có popup xuất hiện thì bỏ qua block này và chạy tiếp
                pass
            # -----------------------------------------------

            # 3. Click vào thanh tìm kiếm (Sử dụng JavaScript click để loại bỏ hoàn toàn rủi ro bị đè)
            driver.execute_script("arguments[0].click();", search_box)

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
                pytest.fail('Test Failed! See log above.')

            print("URL hiện tại:", driver.current_url)

        except Exception as e:
            print("❌ Lỗi:", e)
            pytest.fail('Test Failed! See log above.')

            time.sleep(5)

    if __name__ == "__main__":
        test_search_nonexistent_product()
