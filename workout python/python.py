#1)საკის შემოწმება
 #   მომხმარებელს შეაყვანინე ასაკი. თუ ასაკი 18 ან მეტია, დაბეჭდე Adult, სხვა შემთხვევაში Minor.
#    გამოიყენე: input, int, if, else
#2) სამი რიცხვიდან უდიდესი
# შეაყვანინე მომხმარებელს სამი რიცხვი და იპოვე უდიდესი.
# გამოიყენე: input, int, if, elif, else
#3)რიცხვის დადებითობა
 #შეაყვანინე რიცხვი და დაადგინე დადებითია, უარყოფითია თუ ნულია.
# გამოიყენე: input, int, if, elif, else
#4)ლუწი თუ კენტი
#  შეაყვანინე რიცხვი და შეამოწმე ლუწია თუ კენტი.
#  გამოიყენე: input, int, if, %
#5) საშუალო ქულა
#  შეაყვანინე სამი ქულა და გამოთვალე მათი საშუალო. თუ საშუალო 50-ზე მეტია ან ტოლია, დაბეჭდე Passed, წინააღმდეგ შემთხვევაში Failed.
#  გამოიყენე: input, float, +, /, if, else
#6) პაროლის შემოწმება
#  მომხმარებელს შეაყვანინე პაროლი. თუ პაროლი არის "python123", დაბეჭდე Correct password, სხვა შემთხვევაში Wrong password.
#  გამოიყენე: input, if, else
#7) რიცხვის დიაპაზონი
#  შეაყვანინე რიცხვი. შეამოწმე არის თუ არა ის 10-დან 50-მდე.
#  გამოიყენე: input, int, if, and
#8) ფასდაკლება
#  შეაყვანინე პროდუქტის ფასი. თუ ფასი 100-ზე მეტია, დააკელი 20%. სხვა შემთხვევაში ფასი უცვლელი დატოვე.
#  გამოიყენე: input, float, if, else, გამრავლება
#9) სამუშაო საათები
#  შეაყვანინე საათი 0-დან 23-მდე. თუ საათი 9-დან 18-მდეა, დაბეჭდე Working time, სხვა შემთხვევაში Free time.
#  გამოიყენე: input, int, if, and, else
#10) ორი რიცხვის შედარება
#  შეაყვანინე ორი რიცხვი და დაბეჭდე რომელი უფრო დიდია, ან თუ ტოლია, დაბეჭდე Equal.
#  გამოიყენე: input, int, if, elif, else
#11) სამკუთხედის შემოწმება
#  შეაყვანინე სამი გვერდის სიგრძე. შეამოწმე შესაძლებელია თუ არა ამ გვერდებით სამკუთხედის შექმნა.
#  გამოიყენე: input, int, if, and
#12) ტემპერატურა
#  შეაყვანინე ტემპერატურა.
# 30-ზე მეტი → Hot
# 15-დან 30-მდე → Warm
# 15-ზე ნაკლები → Cold
#    გამოიყენე: input, float, if, elif, else

#1)
age = int(input('enter youre age:'))
if age >= 18:
    print('adult')
else:
    print('minor')

#2)
num1 = int(input('enter youre number: '))
num2 = int(input('enter youre sec number: '))
num3 = int(input('enter youre third number: '))

if num1 >= num2 and num2>= num3:
    print(num1)
elif num2 >= num3 and num1 >= num3:
    print(num2)
else:
    print(num3)

#3)
num = int(input('enter youre number: '))
if num >= 0:
    print('dadebitia')
elif num <= 0:
    print('uaryofitia')
else:
    print('nulia')

#4)
num = int(input('enter youre number: '))
if num % 2 == 0:
    print('luwia')
else:
    print('kentia')

#5)
score = int(input('enter first score: '))
score2 = int(input('enter youre second score: '))
score3 = int(input('enter youre third score: '))
if score >= 50 and score2 >= 50 and score3 >= 50:
    print('chaabare')
else:
    print('chaiweri')

#6)
password = int(input('enter password python123:'))
if password == 'python123':
    print('right password')
else:
    print('wrong password')

#7)
num = int(input('enter youre number: '))
if num >= 10 and num <= 50:
    print('sworia')

#8)
price = float(input('enter youre price: '))
if price >= 100:
    print('discount 20%')
else:
    print('same price')

#9)
clock = float(input('enter clock 0-23: '))
if clock >= 9 and clock <= 18:
    print('working time')
else:
    print('free time')

#10)
num1 = int(input('enter youre first number: '))
num2 = int(input('enter youre second number: '))

if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)

#11)






#12)

temperature = int(input('enter youre temp: '))
if temperature >= 30:
    print('Hot')
elif temperature >= 15 and temperature <= 30:
    print('warm')
elif temperature <= 15:
    print('cold')
  

    







 