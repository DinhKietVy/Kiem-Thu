from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

# =========================
# KHỞI TẠO CHROME
# =========================
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

try:
    # =========================
    # MỞ WEBSITE
    # =========================
    print("🌐 Mở website Hoàng Hà Mobile...")
    driver.get("https://hoanghamobile.com")

    # =========================
    # CLICK MENU ĐIỆN THOẠI
    # =========================
    print("📱 Tìm menu Điện thoại...")

    dien_thoai = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@id='dien-thoai-di-dong']//a")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        dien_thoai
    )

    time.sleep(1)

    ActionChains(driver).move_to_element(dien_thoai).perform()

    time.sleep(1)

    try:
        dien_thoai.click()
    except:
        driver.execute_script(
            "arguments[0].click();",
            dien_thoai
        )

    print("✅ Đã vào danh mục Điện thoại")

    # =========================
    # CHỜ LOAD
    # =========================
    time.sleep(4)

    # =========================
    # CLICK APPLE
    # =========================
    print("\n🍎 Đang chọn hãng Apple...")

    apple_btn = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//a[contains(@href,'Apple') or contains(text(),'Apple')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        apple_btn
    )

    time.sleep(1)

    try:
        apple_btn.click()
    except:
        driver.execute_script(
            "arguments[0].click();",
            apple_btn
        )

    print("✅ Đã click Apple")

    # =========================
    # CHỜ LOAD SẢN PHẨM APPLE
    # =========================
    print("⏳ Đang tải danh sách sản phẩm Apple...")
    time.sleep(5)

    # =========================
    # KIỂM TRA URL
    # =========================
    current_url = driver.current_url

    print(f"\n🔗 URL hiện tại:")
    print(current_url)

    if "Apple" in current_url or "iphone" in current_url.lower():
        print("✅ Đã vào đúng trang Apple")
    else:
        print("⚠️ Có thể chưa vào đúng trang")

    # =========================
    # LẤY DANH SÁCH SẢN PHẨM
    # =========================
    print("\n📦 Đang kiểm tra sản phẩm...")

    products = driver.find_elements(
        By.XPATH,
        "//h3"
    )

    iphone_products = []

    for product in products:
        text = product.text.strip()

        if text and "iphone" in text.lower():
            iphone_products.append(text)

    # =========================
    # KẾT QUẢ TEST
    # =========================
    print(f"\n📱 Tìm thấy {len(iphone_products)} sản phẩm iPhone")

    if len(iphone_products) > 0:

        print("\n✅ TEST PASSED")
        print("Các sản phẩm iPhone đầu tiên:\n")

        for i, name in enumerate(iphone_products[:10], 1):
            print(f"{i}. {name}")

    else:
        print("\n❌ TEST FAILED")
        print("Không tìm thấy sản phẩm iPhone")

except TimeoutException:
    print("❌ Timeout - Không tìm thấy element")

except Exception as e:
    print(f"❌ Lỗi: {e}")

finally:
    print("\n🏁 Kết thúc test")

    input("Nhấn Enter để đóng trình duyệt...")
    driver.quit()