from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Cấu hình Chrome (khuyến nghị dùng ChromeDriver tự động)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--headless")  # Bỏ comment nếu muốn chạy ngầm

# Khởi tạo driver
driver = webdriver.Chrome(options=options)

try:
    # Mở trang đăng nhập
    url = "https://member.hoanghamobile.com/Account/Login?ReturnUrl=http://hoanghamobile.com/"
    driver.get(url)
    print("Đã mở trang đăng nhập")

    # Chờ trang load
    wait = WebDriverWait(driver, 15)

    # ==================== TÌM Ô NHẬP SỐ ĐIỆN THOẠI ====================
    
    # Cách 1: Tìm theo placeholder (thường là "Nhập số điện thoại")
    try:
        phone_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'điện thoại') or contains(@placeholder, 'Số điện thoại')]"))
        )
        print("Tìm thấy input theo placeholder")
    except:
        # Cách 2: Tìm input type tel hoặc name chứa phone/sdt
        phone_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='tel' or contains(@name, 'phone') or contains(@name, 'sdt') or contains(@id, 'phone')]"))
        )
        print("Tìm thấy input theo type/name")

    # Xóa text cũ (nếu có) rồi nhập số điện thoại
    phone_input.clear()
    phone_number = "0793188788"   # ← Thay bằng số điện thoại test của bạn
    phone_input.send_keys(phone_number)
    print(f"Đã nhập số điện thoại: {phone_number}")

    # ==================== NHẤN NÚT TIẾP TỤC / ĐĂNG NHẬP ====================
    try:
        # Tìm nút Tiếp tục (thường có text "TIẾP TỤC")
        continue_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'TIẾP TỤC') or contains(text(), 'Tiếp tục')]"))
        )
        continue_btn.click()
        print("Đã nhấn nút TIẾP TỤC")
    except:
        # Thử cách khác
        continue_btn = driver.find_element(By.XPATH, "//button[@type='submit'] | //input[@type='submit']")
        continue_btn.click()

    # Chờ chuyển trang hoặc hiện form OTP/mật khẩu
    time.sleep(3)
    print("Đang chờ bước tiếp theo (OTP hoặc mật khẩu)...")

    # ===================== KIỂM TRA KẾT QUẢ =====================
    current_url = driver.current_url
    print(f"URL hiện tại: {current_url}")

except TimeoutException:
    print("Timeout: Không tìm thấy element trong thời gian quy định")
except NoSuchElementException as e:
    print(f"Không tìm thấy element: {e}")
except Exception as e:
    print(f"Lỗi: {e}")

finally:
    time.sleep(20)   # Giữ trình duyệt mở để xem kết quả
    if 'driver' in locals():
        driver.quit()