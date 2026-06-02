from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    # Mở trang điện thoại
    driver.get("https://hoanghamobile.com/dien-thoai-di-dong")
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    # Chọn hãng Samsung
    samsung = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@alt='Samsung']")
        )
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", samsung)
    driver.execute_script("arguments[0].click();", samsung)

    print("✅ Đã chọn bộ lọc Samsung")

    # Chờ trang tải lại
    time.sleep(5)

    # Lưu URL sau khi lọc
    filtered_url = driver.current_url
    print("URL sau khi lọc:", filtered_url)

    # Nhấn F5 (refresh)
    driver.refresh()

    print("🔄 Đã nhấn F5")

    # Chờ trang tải lại
    time.sleep(5)

    # Kiểm tra URL có còn chứa samsung không
    current_url = driver.current_url

    print("URL sau khi F5:", current_url)

    # Kiểm tra trạng thái bộ lọc
    if "samsung" in current_url.lower():
        print("✅ PASS: Bộ lọc Samsung vẫn được giữ sau khi F5")
    else:
        print("❌ FAIL: Bộ lọc Samsung bị mất sau khi F5")

except Exception as e:
    import traceback
    traceback.print_exc()

finally:
    time.sleep(5)
    driver.quit()