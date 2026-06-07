import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_TC_SRC_06(driver):


    try:
        driver.get("https://hoanghamobile.com/")

        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "kwd"))
        )

        search_box.clear()
        search_box.send_keys("Sam")
        search_box.send_keys(Keys.ENTER)

        # Chờ chuyển sang trang tìm kiếm
        WebDriverWait(driver, 10).until(
            EC.url_contains("tim-kiem")
        )

        time.sleep(5)

        print("URL:", driver.current_url)

        # Kiểm tra URL đúng
        if "kwd=Sam" in driver.current_url:
            print("✅ URL tìm kiếm hợp lệ")

        # Lấy toàn bộ tiêu đề sản phẩm
        product_names = driver.find_elements(By.TAG_NAME, "h3")

        count = 0
        samsung_found = False

        for item in product_names:
            text = item.text.strip()

            if text:
                count += 1

            if "samsung" in text.lower():
                samsung_found = True

        print("Tổng số tiêu đề sản phẩm:", count)

        if count > 0:
            print("✅ PASS: Có danh sách sản phẩm")

        if samsung_found:
            print("✅ PASS: Có sản phẩm Samsung")

    except Exception as e:
        print("❌ Lỗi:", e)
        pytest.fail('Test Failed! See log above.')

        time.sleep(5)

