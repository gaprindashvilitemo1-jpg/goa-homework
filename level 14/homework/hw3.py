# 3) მომხმარებელს შემოატანინე 5 რიცხვი და for loop-ის გამოყენებით იპოვე მათი ჯამი.

total = 0

for i in range(5):
    user = float(input('enter youre number: '))
    total += user
print(total)