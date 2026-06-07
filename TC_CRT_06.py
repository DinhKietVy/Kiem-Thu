from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--incognito")  # Đảm bảo giỏ hàng trống

driver = webdriver.Chrome(service=Service(), options=options)
wait = WebDriverWait(driver, 20)

try:
    # Mở trang chủ
    driver.get("https://hoanghamobile.com")
    print("✅ Đã mở trang chủ")

    # Bấm icon Giỏ hàng
    cart_icon = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/gio-hang']"))
    )
    driver.execute_script("arguments[0].click();", cart_icon)

    print("✅ Đã mở trang giỏ hàng")

    # Kiểm tra thông báo giỏ hàng trống
    empty_cart = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//strong[contains(text(),'Hiện chưa có sản phẩm nào trong giỏ hàng')]")
    )
)

    if empty_cart.is_displayed():
        print("✅ PASS: Hiển thị 'Giỏ hàng của bạn đang trống'")
    else:
        print("❌ FAIL: Không hiển thị thông báo")
except Exception:
    traceback.print_exc()

finally:
    time.sleep(5)
    driver.quit()