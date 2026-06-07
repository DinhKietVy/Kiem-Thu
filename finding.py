from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
import time


def test_search_hoangha():

    driver = webdriver.Chrome()

    try:
        # 1. Mở trang chủ
        driver.get("https://hoanghamobile.com/")
        driver.maximize_window()

        print("✅ Đã mở trang Hoàng Hà Mobile")

        # 2. Chờ ô tìm kiếm xuất hiện
        search_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "kwd"))
        )

        # 3. Nhập từ khóa
        tu_khoa = "iPhone 16"

        search_box.clear()
        search_box.send_keys(tu_khoa)

        print(f"✅ Đã nhập từ khóa: {tu_khoa}")

        # 4. Tìm kiếm
        search_box.send_keys(Keys.ENTER)

        # 5. Chờ chuyển sang trang kết quả
        WebDriverWait(driver, 15).until(
            EC.url_contains("tim-kiem")
        )

        print("✅ Đã chuyển sang trang kết quả")

        # Đợi JS render
        time.sleep(5)

        print("📌 URL:", driver.current_url)
        print("📌 Title:", driver.title)

        # Tìm tất cả phần tử chứa chữ iPhone 16
        products = driver.find_elements(
            By.XPATH,
            "//*[contains(text(),'iPhone 16')]"
        )

        # Loại bỏ text trùng lặp
        product_names = []

        for p in products:
            text = p.text.strip()

            if (
                text
                and "iPhone 16" in text
                and text not in product_names
            ):
                product_names.append(text)

        print(
            f"\n✅ Tìm thấy {len(product_names)} kết quả chứa '{tu_khoa}'"
        )

        if product_names:

            print("\n===== DANH SÁCH SẢN PHẨM =====")

            for i, name in enumerate(product_names[:20], start=1):
                print(f"{i}. {name}")

            print("\n✅ Chức năng tìm kiếm hoạt động tốt!")

        else:

            print("⚠️ Không tìm thấy sản phẩm nào!")

            # In thử 1000 ký tự đầu để debug
            print("\n===== DEBUG HTML =====")
            print(driver.page_source[:1000])

    except Exception as e:

        print("\n❌ Lỗi:")
        print(type(e).__name__)
        print(e)

        traceback.print_exc()

    finally:

        time.sleep(5)
        if 'driver' in locals():
            driver.quit()


if __name__ == "__main__":
    test_search_hoangha()