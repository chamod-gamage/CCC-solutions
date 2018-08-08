digits = []
for i in range(4):
    digits.append(int(input()))
eightnine = [8,9]
if digits[0] in eightnine and digits[3] in eightnine and digits[2] == digits[1]:
    print('ignore')
else:
    print('answer')

