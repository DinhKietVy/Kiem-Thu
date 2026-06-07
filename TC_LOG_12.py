from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://member.hoanghamobile.com/Account/Login?ReturnUrl=http://hoanghamobile.com/")

    wait = WebDriverWait(driver, 15)

    # Tìm ô SĐT lần 1
    phone_input = wait.until(
        EC.presence_of_element_located((By.ID, "Phone"))
    )

    # Nhập SĐT có chứa dấu cách
    phone_input.clear()
    phone_input.send_keys("079 318 8788")

    time.sleep(1)

    # Bấm nút Tiếp tục (Sửa lại XPath dùng onclick cho chuẩn xác như file trước)
    continue_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@onclick, 'checkLogin(1)')]")
        )
    )

    continue_btn.click()

    # Chờ 2 giây để hệ thống AJAX xử lý và render lại giao diện
    time.sleep(2)

    # --- ĐOẠN SỬA LỖI STALE ELEMENT ---
    # Tìm lại ô SĐT lần 2 để cập nhật phần tử mới trên DOM sau khi bấm nút
    phone_input = wait.until(
        EC.presence_of_element_located((By.ID, "Phone"))
    )
    # ----------------------------------

    # Lấy giá trị thực tế trong ô sau khi hệ thống xử lý
    actual_value = phone_input.get_attribute("value")

    print("Giá trị sau xử lý:", repr(actual_value))

    # Kiểm tra Auto-trim
    if actual_value.replace(" ", "") == "0793188788":
        print("✅ PASS - Hệ thống tự động loại bỏ dấu cách và nhận diện SĐT hợp lệ")
    else:
        print("❌ FAIL - Hệ thống không xử lý dấu cách đúng cách")

except Exception as e:
    print("Lỗi:", e)

finally:
    time.sleep(5)
    driver.quit()