from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://member.hoanghamobile.com/Account/Login?ReturnUrl=http://hoanghamobile.com/")

    wait = WebDriverWait(driver, 15)

    # Tìm ô SĐT
    phone_input = wait.until(
        EC.presence_of_element_located(
            (By.XPATH,
             "//input[contains(@placeholder,'điện thoại') or "
             "contains(@placeholder,'Điện thoại') or "
             "@type='tel']")
        )
    )

    # Copy chuỗi không hợp lệ vào clipboard
    pyperclip.copy("abcdef")

    # Click vào ô nhập
    phone_input.click()

    # Ctrl + V
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .send_keys('v') \
        .key_up(Keys.CONTROL) \
        .perform()

    time.sleep(1)

    # Lấy giá trị thực tế trong ô
    actual_value = phone_input.get_attribute("value")

    print("Giá trị sau khi paste:", repr(actual_value))

    # Kiểm tra
    if actual_value == "":
        print("✅ PASS - Hệ thống chặn hoàn toàn ký tự chữ")
    elif actual_value.isdigit():
        print("✅ PASS - Hệ thống chỉ giữ lại số")
    else:
        print("❌ FAIL - Hệ thống cho phép nhập ký tự không hợp lệ")

except Exception as e:
    print("Lỗi:", e)

finally:
    time.sleep(5)
    driver.quit()