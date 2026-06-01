from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Cấu hình Chrome (có thể dùng WebDriverManager để tự động tải driver)
def test_search_hoangha():
    # Khởi tạo driver
    driver = webdriver.Chrome()  # Hoặc dùng Service nếu cần chỉ định path
    
    try:
        # 1. Mở trang chủ
        driver.get("https://hoanghamobile.com/")
        driver.maximize_window()
        print("✅ Đã mở trang Hoàng Hà Mobile")
        
        # Chờ trang load
        time.sleep(3)
        
        # 2. Tìm thanh tìm kiếm theo ID (như bạn cung cấp)
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "kwd"))
        )
        
        # 3. Nhập từ khóa tìm kiếm
        tu_khoa = "iPhone 16"   # Bạn có thể thay đổi từ khóa
        search_box.clear()      # Xóa nếu có text mặc định
        search_box.send_keys(tu_khoa)
        print(f"✅ Đã nhập từ khóa: {tu_khoa}")
        
        # 4. Submit tìm kiếm (nhấn Enter)
        search_box.send_keys(Keys.ENTER)
        
        # Hoặc click nút tìm kiếm nếu có (thường trang này submit bằng Enter)
        # search_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        # search_button.click()
        
        # 5. Chờ kết quả load
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-item, .search-result, .list-product"))
        )
        
        time.sleep(3)  # Đợi thêm để trang render đầy đủ
        
        # 6. Kiểm tra kết quả
        results = driver.find_elements(By.CSS_SELECTOR, ".product-item, .item-product, .search-product")
        print(f"✅ Tìm thấy {len(results)} sản phẩm với từ khóa '{tu_khoa}'")
        
        if len(results) > 0:
            print("✅ Chức năng tìm kiếm hoạt động tốt!")
            # In ra vài sản phẩm đầu tiên
            for i, item in enumerate(results[:5]):
                try:
                    name = item.find_element(By.CSS_SELECTOR, "h3, .product-name, .title").text
                    print(f"   {i+1}. {name}")
                except:
                    pass
        else:
            print("⚠️ Không tìm thấy sản phẩm nào!")
        
        # Kiểm tra URL có chứa từ khóa không (tùy trang)
        current_url = driver.current_url
        if tu_khoa.lower().replace(" ", "-") in current_url.lower() or "search" in current_url.lower():
            print("✅ URL kết quả tìm kiếm hợp lệ")
            
    except Exception as e:
        print(f"❌ Lỗi: {e}")
    
    finally:
        time.sleep(5)
        driver.quit()

# Chạy test
if __name__ == "__main__":
    test_search_hoangha()