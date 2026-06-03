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

    # Ô nhập số điện thoại
    phone_input = wait.until(
        EC.presence_of_element_located((By.ID, "Phone"))
    )

    # Nhập số điện thoại có mã vùng quốc tế
    phone_input.clear()
    phone_input.send_keys("+84793188788")

    time.sleep(1)

    # Bấm TIẾP TỤC
    continue_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[contains(@onclick,'checkLogin')]")
        )
    )

    driver.execute_script("arguments[0].click();", continue_btn)

    time.sleep(3)

    # Lấy giá trị hiện tại trong ô nhập
    actual_value = phone_input.get_attribute("value")

    print("Giá trị trong ô:", actual_value)
    print("URL hiện tại:", driver.current_url)

    # Kiểm tra kết quả
    if actual_value == "0793188788":
        print("✅ PASS - Hệ thống tự quy đổi +84 thành số 0")
    elif "otp" in driver.current_url.lower() or "verify" in driver.current_url.lower():
        print("✅ PASS - Hệ thống chấp nhận định dạng +84")
    else:
        print("⚠️ Cần kiểm tra thêm phản hồi thực tế của hệ thống")

except Exception as e:
    print("Lỗi:", e)

finally:
    time.sleep(5)
    driver.quit()