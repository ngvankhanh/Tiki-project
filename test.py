## Test chức năng
cal = '''
 _____________________
|  _________________  |
| |               0.| |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''

raw = cal[60:67]
user = input()
new_cal = cal.replace(raw, str(eval(user)))
print(new_cal)
