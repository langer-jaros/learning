import re

string = " \t \r124.561.123 " # 'Cat \n eND'
string = "04.1 a–c"

number = r"(\d+(\.\d+)*)"
letter = r"[a-zA-Z]"
dash = r"[-–]"
comma = r"(\s*,\s*)"
letters = fr"({letter}+(({dash}|{comma}){letter}+)?)"
pattern = fr"\A\s*{number}\s*{letters}?\s*\Z"

# pattern = fr"\A\s*{number}{letter}+.*\Z"

findings = re.match( pattern, string, flags=re.I | re.DOTALL)

finding = findings.group(0) if (findings is not None) else findings
print(finding)
