import os
import re

def refactor_test(filepath, output_dir):
    filename = os.path.basename(filepath)
    new_filename = f"test_{filename}" if not filename.startswith("test_") else filename
    out_filepath = os.path.join(output_dir, new_filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    imports = [
        "import pytest\n",
        "from selenium.webdriver.common.keys import Keys\n",
        "from selenium.webdriver.common.action_chains import ActionChains\n"
    ]
    body = []
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("import ") or stripped.startswith("from "):
            if "selenium.webdriver.chrome.service" not in stripped and "webdriver" not in stripped or "By" in stripped or "WebDriverWait" in stripped or "expected_conditions" in stripped:
                # Keep imports like By, WebDriverWait, EC, time, traceback, etc.
                if stripped not in [i.strip() for i in imports]:
                    imports.append(stripped + "\n")
        elif "options = " in stripped or "options.add_argument" in stripped or "webdriver.ChromeOptions()" in stripped:
            continue
        elif "driver = webdriver.Chrome" in stripped:
            continue
        elif "driver.maximize_window()" in stripped:
            continue
        elif "driver.quit()" in stripped:
            continue
        elif stripped == "finally:":
            continue
        elif "if 'driver' in locals():" in stripped:
            continue
        else:
            body.append(line)
            
    # Clean up empty finally blocks that were left over
    body_str = "".join(body)
    body_str = re.sub(r'^\s*finally:\s*$', '', body_str, flags=re.MULTILINE)
    
    test_function_name = new_filename.replace('.py', '')
    
    indented_body = ""
    for line in body_str.split("\n"):
        if line.strip():
            indented_body += "    " + line + "\n"
        else:
            indented_body += "\n"
            
    final_content = "".join(imports) + f"\n\ndef {test_function_name}(driver):\n{indented_body}"
    
    with open(out_filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(root_dir, 'tests')
    
    os.makedirs(tests_dir, exist_ok=True)
    
    for f in os.listdir(root_dir):
        if f.endswith('.py') and f not in ('conftest.py', 'refactor_tests.py', 'run_tests.py'):
            filepath = os.path.join(root_dir, f)
            refactor_test(filepath, tests_dir)
            os.remove(filepath)

if __name__ == '__main__':
    main()
