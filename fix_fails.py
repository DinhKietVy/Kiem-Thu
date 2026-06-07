import os
import re

def fix_fails(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    for line in lines:
        new_lines.append(line)
        # If the line prints a fail icon, add pytest.fail after it
        if re.search(r'^\s*print\(.*❌.*\)', line):
            indent = line[:len(line) - len(line.lstrip())]
            new_lines.append(indent + "pytest.fail('Test Failed! See log above.')\n")
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

def main():
    d = r'd:\Code\KiemThu\tests'
    for f in os.listdir(d):
        if f.endswith('.py'):
            fix_fails(os.path.join(d, f))

if __name__ == '__main__':
    main()
