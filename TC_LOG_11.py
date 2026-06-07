from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Mở trang đăng nhập
    driver.get(
        "https://member.hoanghamobile.com/Account/Login?ReturnUrl=http://hoanghamobile.com/"
    )

    wait = WebDriverWait(driver, 15)

    # Tìm ô SĐT
    phone_input = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//input[contains(@placeholder,'điện thoại') or "
                "contains(@placeholder,'Điện thoại') or "
                "@type='tel']"
            )
        )
    )

    # Payload XSS
    xss_payload = "<script>alert(1)</script>"

    # Nhập payload
    phone_input.clear()
    phone_input.send_keys(xss_payload)

    print("Đã nhập:", xss_payload)

    # Bấm nút Tiếp tục (Đã sửa XPath: định vị chính xác bằng hàm onclick của nút TIẾP TỤC)
    continue_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@onclick, 'checkLogin(1)')]")
        )
    )

    continue_btn.click()
    print("Đã click nút TIẾP TỤC")

    time.sleep(3)

    # Kiểm tra xem có alert xuất hiện không
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text

        print("❌ FAIL - Alert xuất hiện:", alert_text)

        alert.accept()

    except:
        print("✅ PASS - Không xuất hiện popup alert")

    # Kiểm tra thông báo lỗi
    page_source = driver.page_source.lower()

    if ("số điện thoại" in page_source or
        "không hợp lệ" in page_source):
        print("✅ PASS - Hệ thống báo lỗi định dạng SĐT")
    else:
        print("⚠ Không tìm thấy thông báo lỗi định dạng")

except Exception as e:
    print("Lỗi:", e)

finally:
    time.sleep(5)
    driver.quit()