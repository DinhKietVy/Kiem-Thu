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

    time.sleep(3)

    # Chọn mức giá 20 đến 25 triệu
    price_filter = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[contains(normalize-space(.),'20 đến 25 triệu')]")
        )
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", price_filter)
    driver.execute_script("arguments[0].click();", price_filter)

    # Chờ danh sách sản phẩm cập nhật
    time.sleep(5)

    # Lấy danh sách tên sản phẩm
    products = driver.find_elements(By.TAG_NAME, "h3")

    samsung_found = False

    print("===== DANH SÁCH SẢN PHẨM =====")

    for product in products:
        name = product.text.strip()

        if not name:
            continue

        print(name)

        if "samsung" in name.lower():
            samsung_found = True
        else:
            print(f"❌ Phát hiện sản phẩm không phải Samsung: {name}")

    print("\n===== KẾT QUẢ KIỂM THỬ =====")

    if samsung_found:
        print("✅ Tìm thấy sản phẩm Samsung")
    else:
        print("❌ Không tìm thấy sản phẩm Samsung")

    # Kiểm tra tất cả sản phẩm đều là Samsung
    all_samsung = True

    for product in products:
        name = product.text.strip()

        if name and "samsung" not in name.lower():
            all_samsung = False
            break

    if all_samsung:
        print("✅ PASS: Chỉ hiển thị điện thoại Samsung")
    else:
        print("❌ FAIL: Có sản phẩm không phải Samsung")

except Exception as e:
    import traceback
    traceback.print_exc()

finally:
    time.sleep(5)
    driver.quit()