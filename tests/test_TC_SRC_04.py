import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_TC_SRC_04(driver):

    def test_empty_search():

        try:
            # 1. Mở trang chủ
            driver.get("https://hoanghamobile.com/")

            wait = WebDriverWait(driver, 10)

            # Chờ thanh tìm kiếm xuất hiện trong DOM
            search_box = wait.until(
                EC.presence_of_element_located((By.ID, "kwd"))
            )

            # --- ĐOẠN XỬ LÝ POPUP QUẢNG CÁO (NẾU CÓ) ---
            try:
                # Tìm nút Close/X của modal dựa trên cấu trúc modal blocker đang che
                # Thường nút tắt modal của jquery-modal có class 'close-modal'
                close_popup_btn = wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'close-modal')]"))
                )
                close_popup_btn.click()
                print("Đã tự động tắt popup quảng cáo.")
                time.sleep(1) # Chờ hiệu ứng tắt popup biến mất hẳn
            except:
                # Nếu không tìm thấy nút tắt hoặc không có popup thì bỏ qua
                pass
            # --------------------------------------------

            # Lưu URL ban đầu
            original_url = driver.current_url

            # 2. Click vào thanh tìm kiếm (Sử dụng JavaScript Click để chống bị đè)
            driver.execute_script("arguments[0].click();", search_box)

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
                pytest.fail('Test Failed! See log above.')
                print(f"Ban đầu: {original_url}")
                print(f"Hiện tại: {current_url}")

            # 7. Kiểm tra không chuyển sang trang tìm kiếm
            if "/tim-kiem" not in current_url.lower() and "search" not in current_url.lower():
                print("✅ PASS: Vẫn ở trang hiện tại")
            else:
                print("❌ FAIL: Đã chuyển sang trang tìm kiếm")
                pytest.fail('Test Failed! See log above.')

        except Exception as e:
            print(f"❌ Lỗi: {e}")
            pytest.fail('Test Failed! See log above.')

            time.sleep(5)

    if __name__ == "__main__":
        test_empty_search()
