from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
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
    print("🌐 Đang mở website Hoàng Hà Mobile...")
    driver.get("https://hoanghamobile.com")

    # =========================
    # CLICK DANH MỤC ĐIỆN THOẠI
    # =========================
    print("📱 Đang tìm danh mục Điện thoại...")

    dien_thoai = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@id='dien-thoai-di-dong']//a")
        )
    )

    # Scroll tới menu
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        dien_thoai
    )

    time.sleep(1)

    # Hover menu
    ActionChains(driver).move_to_element(dien_thoai).perform()

    time.sleep(1)

    # Click menu
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
    time.sleep(5)

    # =========================
    # CHỌN MỨC GIÁ 1-3 TRIỆU
    # =========================
    print("\n💰 Đang chọn mức giá 1 - 3 triệu...")

    gia_filter = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[contains(@href,'1t-3t')]"
            )
        )
    )

    # Scroll tới filter
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        gia_filter
    )

    time.sleep(1)

    # Click filter
    try:
        gia_filter.click()
    except:
        driver.execute_script(
            "arguments[0].click();",
            gia_filter
        )

    print("✅ Đã chọn bộ lọc giá 1 - 3 triệu")

    # =========================
    # CHỜ LOAD SẢN PHẨM
    # =========================
    print("⏳ Đang tải sản phẩm...")
    time.sleep(5)

    # =========================
    # KIỂM TRA URL
    # =========================
    current_url = driver.current_url

    print("\n🔗 URL hiện tại:")
    print(current_url)

    if "1t-3t" in current_url:
        print("✅ URL đúng bộ lọc giá")
    else:
        print("⚠️ URL có thể chưa đúng")

    # =========================
    # LẤY DANH SÁCH SẢN PHẨM
    # =========================
    print("\n📦 Đang kiểm tra giá sản phẩm...")

    products = driver.find_elements(
        By.XPATH,
        "//div[contains(@class,'product')]"
    )

    valid_products = 0
    checked = 0

    for product in products:

        try:
            # Tên sản phẩm
            name_element = product.find_element(By.XPATH, ".//h3")
            product_name = name_element.text.strip()

            # Giá sản phẩm
            price_element = product.find_element(
                By.XPATH,
                ".//span[contains(@class,'price')]"
            )

            price_text = price_element.text.strip()

            # Chuyển giá thành số
            number = re.sub(r"[^\d]", "", price_text)

            if number:

                price_value = int(number)

                checked += 1

                # Kiểm tra giá từ 1 -> 3 triệu
                if 1_000_000 <= price_value <= 3_000_000:

                    valid_products += 1

                    print(f"✅ {product_name}")
                    print(f"   Giá: {price_text}")

                else:

                    print(f"❌ {product_name}")
                    print(f"   Giá sai: {price_text}")

        except:
            continue

        # Giới hạn số lượng kiểm tra
        if checked >= 15:
            break

    # =========================
    # KẾT QUẢ TEST
    # =========================
    print("\n========================")
    print(f"📱 Đã kiểm tra: {checked} sản phẩm")
    print(f"✅ Hợp lệ: {valid_products}")

    if valid_products > 0:
        print("🎉 TEST PASSED")
    else:
        print("❌ TEST FAILED")

except TimeoutException:
    print("❌ Timeout - Không tìm thấy element")

except Exception as e:
    print(f"❌ Lỗi: {e}")

finally:
    print("\n🏁 Kết thúc test")

    input("Nhấn Enter để đóng trình duyệt...")
    driver.quit()