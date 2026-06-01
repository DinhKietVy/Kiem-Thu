from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(), options=options)
wait = WebDriverWait(driver, 20)

sku = "2510DRA23EXD"
color_name = "Xanh băng"

try:
    # ====================== 1. MỞ TRANG SẢN PHẨM & THÊM VÀO GIỎ ======================
    driver.get("https://hoanghamobile.com/dien-thoai/xiaomi-redmi-note-15-6gb-128gb")
    print("✅ Mở trang sản phẩm")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(2)

    # Chọn màu
    try:
        color_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, 
                f"//div[contains(@class,'color-price')]//span[text()='{color_name}']"))
        )
        driver.execute_script("arguments[0].click();", color_element)
        print(f"✅ Đã chọn màu: {color_name}")
        time.sleep(2)
    except:
        print("⚠️ Không chọn được màu")

    # Thêm vào giỏ
    add_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.add-buy.add-cart.inventory")))
    driver.execute_script("arguments[0].click();", add_button)
    print("✅ Đã thêm vào giỏ hàng")
    time.sleep(3)

    # ====================== 2. VÀO TRANG GIỎ HÀNG ======================
    driver.get("https://hoanghamobile.com/gio-hang")
    print("✅ Đã vào trang giỏ hàng")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(2)

    # ====================== 3. TĂNG SỐ LƯỢNG (+1) ======================
    try:
        plus_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, 
                f"//button[contains(@onclick, \"cartPlus('{sku}')\") or @data-sku='{sku}']"))
        )
        
        # Lấy giá trước khi tăng
        price_before = None
        try:
            price_before = driver.find_element(By.CSS_SELECTOR, f"tr[data-sku='{sku}'] .price, .cart-item-price").text
            print(f"Giá trước khi tăng: {price_before}")
        except:
            pass

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", plus_button)
        driver.execute_script("arguments[0].click();", plus_button)
        print("✅ Đã click nút + (tăng số lượng)")
        time.sleep(3)   # Chờ cập nhật tổng tiền

    except Exception as e:
        print("❌ Không tìm thấy nút tăng số lượng:", str(e))

    # ====================== 4. KIỂM TRA TỔNG TIỀN ======================
    time.sleep(2)
    try:
        # Lấy tổng tiền sau khi tăng
        total_element = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, ".cart-total-price, .total-amount, .grand-total, .price-total"
        )))
        
        total_after = total_element.text
        print(f"✅ Tổng tiền sau khi tăng số lượng: {total_after}")

        # Kiểm tra sơ bộ
        if "₫" in total_after and len(total_after) > 5:
            print("✅ Tổng tiền đã được cập nhật (có chứa ₫)")
        else:
            print("⚠️ Tổng tiền chưa cập nhật hoặc selector chưa đúng")

    except:
        print("❌ Không tìm thấy tổng tiền giỏ hàng")

    # ====================== 5. (TÙY CHỌN) XÓA SẢN PHẨM ======================
    print("\n--- Đang xóa sản phẩm để dọn giỏ ---")
    try:
        delete_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, f"//a[contains(@href, \"cartDelete('{sku}')\")]"
        )))
        driver.execute_script("arguments[0].click();", delete_btn)
        print("✅ Đã click xóa sản phẩm")
        time.sleep(2)
    except:
        print("⚠️ Không xóa được sản phẩm")

    print("\n🎉 HOÀN THÀNH TEST: Thêm → Tăng số lượng → Kiểm tra tổng tiền")

except Exception as e:
    print("❌ Lỗi:", str(e))

finally:
    time.sleep(8)
    # driver.quit()