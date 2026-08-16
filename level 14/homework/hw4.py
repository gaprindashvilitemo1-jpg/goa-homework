# 4) მომხმარებელს შემოატანინე 5 რიცხვი და იპოვე მათ შორის ყველაზე დიდი რიცხვი.

max_num = int(input("enter youre number: "))
for i in range(4):
    num = int(input('enter youre number: '))
    if num > max_num:
        
        max_num = num
print(max_num)