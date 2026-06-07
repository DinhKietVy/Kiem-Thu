import os
import subprocess
import sys
import time

def main():
    # Lấy thư mục hiện tại và tên file này
    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_file = os.path.basename(__file__)
    
    # Tìm tất cả các file .py trong thư mục hiện tại (loại trừ chính file này)
    test_files = [f for f in os.listdir(current_dir) if f.endswith('.py') and f != current_file]
    
    total_tests = len(test_files)
    pass_count = 0
    fail_count = 0
    unknown_count = 0
    
    print("="*60)
    print(f"🚀 BẮT ĐẦU CHẠY {total_tests} FILE TEST")
    print("="*60)
    
    for i, test in enumerate(test_files, 1):
        print(f"[{i:02d}/{total_tests}] Đang chạy {test:20} ... ", end="", flush=True)
        
        start_time = time.time()
        test_path = os.path.join(current_dir, test)
        
        try:
            # Chạy file test, thiết lập encoding utf-8 để tránh lỗi khi in ký tự đặc biệt (❌, ✅)
            env = os.environ.copy()
            env["PYTHONIOENCODING"] = "utf-8"
            
            result = subprocess.run(
                [sys.executable, test_path], 
                capture_output=True, 
                text=True, 
                encoding='utf-8', 
                errors='replace', 
                timeout=300,
                env=env,
                cwd=current_dir
            )
            
            # Chỉ lấy stdout (những gì code test cố ý in ra bằng hàm print)
            # Tránh gộp stderr vì Chrome/Selenium thường in ra rất nhiều log cảnh báo "failed", "exception" gây nhiễu
            stdout_lower = result.stdout.lower()
            
            is_fail = False
            is_pass = False
            
            # Phân tích lỗi
            # 1. Bị crash (ngoại lệ không được catch)
            if result.returncode != 0:
                is_fail = True
            # 2. Hoặc code test chủ động in ra kết quả Fail / Lỗi
            elif "❌" in result.stdout or "fail" in stdout_lower or "lỗi" in stdout_lower:
                is_fail = True
                
            # Phân tích Pass (chỉ xét khi không bị Fail)
            if not is_fail:
                if "✅" in result.stdout or "🎉" in result.stdout or "pass" in stdout_lower or "hoàn thành" in stdout_lower:
                    is_pass = True
                
            duration = time.time() - start_time
            
            # Xuất kết quả
            if is_fail:
                print(f"❌ FAIL ({duration:.1f}s)")
                fail_count += 1
            elif is_pass:
                print(f"✅ PASS ({duration:.1f}s)")
                pass_count += 1
            else:
                print(f"⚠️ UNKNOWN ({duration:.1f}s)")
                unknown_count += 1
                
        except subprocess.TimeoutExpired:
            print("⏳ TIMEOUT (Quá 5 phút)")
            fail_count += 1
        except Exception as e:
            print(f"❌ ERROR: {e}")
            fail_count += 1

    print("\n" + "="*60)
    print("📊 TỔNG KẾT KẾT QUẢ KIỂM THỬ:")
    print("="*60)
    print(f"Tổng số file chạy : {total_tests}")
    print(f"✅ Số file PASS   : {pass_count}")
    print(f"❌ Số file FAIL   : {fail_count}")
    if unknown_count > 0:
        print(f"⚠️ Số file UNKNOWN: {unknown_count}")
    print("="*60)

if __name__ == "__main__":
    main()
