#level 14:
#1) გამოიტანე რიცხვები 1-დან 20-მდე, მხოლოდ ლუწები.
#2) გამოიტანე რიცხვები 5-დან 50-მდე, რომლებიც იყოფა 5-ზე.
#3) მომხმარებელს შემოატანინე რიცხვი და for loop-ის გამოყენებით გამოიტანე 1-დან ამ რიცხვამდე ყველა რიცხვი.
#4) მომხმარებელს შემოატანინე რიცხვი და გამოიტანე მისი გამრავლების ტაბულა 1-დან 10-მდე.
#5) იპოვე რიცხვების 1-დან 100-მდე ჯამი

#1)
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

#2)
for i in range(5, 51):
    if i % 5 == 0:
        print(i)

#3)
num = int(input('enter youre num: '))

for i in range(1, num):
    print(i)

#4)
num = int(input('enter youre num: '))

for i in range(1, 11):
    print(num * i)

#5)
total = 0

for i in range(1, 101):
    total += 1
print(total)