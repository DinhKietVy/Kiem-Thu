from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    # Mở trang điện thoại
    driver.get("https://hoanghamobile.com/dien-thoai-di-dong")
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    # Tìm kiếm "iphone"
    search_box = wait.until(
        EC.presence_of_element_located((By.ID, "kwd"))
    )

    search_box.clear()
    search_box.send_keys("iphone")
    search_box.send_keys(Keys.ENTER)

    print("✅ Đã tìm kiếm 'iphone'")

    # Chờ kết quả tìm kiếm tải
    time.sleep(5)

    # Chọn bộ lọc Samsung
    samsung = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@alt='Samsung']")
        )
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", samsung)
    driver.execute_script("arguments[0].click();", samsung)

    print("✅ Đã chọn bộ lọc Samsung")

    # Chờ kết quả cập nhật
    time.sleep(5)

    # Kiểm tra thông báo không có sản phẩm
    page_source = driver.page_source.lower()

    if "không có sản phẩm phù hợp" in page_source:
        print("✅ PASS: Hiển thị thông báo 'Không có sản phẩm phù hợp'")
    else:
        print("❌ FAIL: Không xuất hiện thông báo mong đợi")

except Exception as e:
    import traceback
    traceback.print_exc()

finally:
    time.sleep(5)
    driver.quit()