import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback


def test_TC_FLT_06(driver):


    try:
        # Mở trang điện thoại
        driver.get("https://hoanghamobile.com/dien-thoai-di-dong")

        wait = WebDriverWait(driver, 20)

        # Đếm số sản phẩm ban đầu
        time.sleep(5)
        initial_products = driver.find_elements(By.TAG_NAME, "h3")
        initial_count = len([p for p in initial_products if p.text.strip()])

        print(f"Số sản phẩm ban đầu: {initial_count}")

        # Chọn Apple
        apple = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//img[@alt='Apple']")
            )
        )

        driver.execute_script("arguments[0].scrollIntoView(true);", apple)
        driver.execute_script("arguments[0].click();", apple)

        print("✅ Đã chọn bộ lọc Apple")

        # Chờ trang tải
        time.sleep(5)

        # Bấm Apple lần thứ 2 để bỏ chọn
        apple = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//img[@alt='Apple']")
            )
        )

        driver.execute_script("arguments[0].scrollIntoView(true);", apple)
        driver.execute_script("arguments[0].click();", apple)

        print("✅ Đã bỏ chọn bộ lọc Apple")

        # Chờ trang tải lại
        time.sleep(5)

        # Đếm số sản phẩm sau khi bỏ lọc
        final_products = driver.find_elements(By.TAG_NAME, "h3")
        final_count = len([p for p in final_products if p.text.strip()])

        print(f"Số sản phẩm sau khi bỏ lọc: {final_count}")

        print("\n===== KẾT QUẢ KIỂM THỬ =====")

        if final_count >= initial_count:
            print("✅ PASS: Danh sách sản phẩm được khôi phục")
        else:
            print("❌ FAIL: Danh sách sản phẩm chưa được khôi phục hoàn toàn")
            pytest.fail('Test Failed! See log above.')

    except Exception as e:
        traceback.print_exc()

        time.sleep(5)

