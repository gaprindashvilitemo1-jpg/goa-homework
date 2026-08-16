# 4) მომხმარებელს შემოატანინე 5 რიცხვი და იპოვე მათ შორის ყველაზე დიდი რიცხვი.


for i in range(5):
    num = float(input('enter youre number: '))
    if i == 0 or num > max_num:
        max_num = num
print(max_num)