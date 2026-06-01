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

    # Chọn hãng Apple
    apple = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@alt='Apple']")
        )
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", apple)
    driver.execute_script("arguments[0].click();", apple)

    time.sleep(3)

    # Chọn hãng Xiaomi
    xiaomi = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@alt='Xiaomi']")
        )
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", xiaomi)
    driver.execute_script("arguments[0].click();", xiaomi)

    # Chờ danh sách sản phẩm cập nhật
    time.sleep(5)

    # Lấy danh sách tên sản phẩm
    products = driver.find_elements(By.TAG_NAME, "h3")

    apple_found = False
    xiaomi_found = False

    print("===== DANH SÁCH SẢN PHẨM =====")

    for product in products:
        name = product.text.strip()

        if not name:
            continue

        print(name)

        # Apple thường là iPhone
        if "iphone" in name.lower():
            apple_found = True

        # Xiaomi
        if "xiaomi" in name.lower():
            xiaomi_found = True

    print("\n===== KẾT QUẢ KIỂM THỬ =====")

    if apple_found:
        print("✅ Tìm thấy sản phẩm Apple")
    else:
        print("❌ Không tìm thấy sản phẩm Apple")

    if xiaomi_found:
        print("✅ Tìm thấy sản phẩm Xiaomi")
    else:
        print("❌ Không tìm thấy sản phẩm Xiaomi")

    # PASS khi có cả Apple và Xiaomi
    if apple_found and xiaomi_found:
        print("✅ PASS: Danh sách chứa cả Apple và Xiaomi")
    else:
        print("❌ FAIL: Danh sách không chứa đồng thời Apple và Xiaomi")

except Exception as e:
    import traceback
    traceback.print_exc()

finally:
    time.sleep(5)
    driver.quit()