
#print — დაბეჭდე ერთი წინადადება, სადაც წერია შენი სახელი, ასაკი და ქალაქი.
#ცვლადი — შექმენი ორი ცვლადი: name და age, შემდეგ ორივე დაბეჭდე.
#input — მომხმარებელს შეაყვანინე სახელი და ქალაქი, შემდეგ დაბეჭდე ორივე ერთად.
#int — მომხმარებელს შეაყვანინე ორი რიცხვი და დაბეჭდე მათი ჯამი.
#float — მომხმარებელს შეაყვანინე პროდუქტის ფასი და რაოდენობა, შემდეგ გამოთვალე საერთო ფასი.
#არითმეტიკული ოპერატორები — შეიყვანე ორი რიცხვი და დაბეჭდე მათი ჯამი, სხვაობა და ნამრავლი.
#შედარებითი ოპერატორები — შეიყვანე ორი რიცხვი და შეამოწმე, ტოლია თუ არა ისინი.
#and — შეიყვანე ასაკი და შეამოწმე, არის თუ არა ასაკი 13-ზე მეტი და 18-ზე ნაკლები.
#or — შეიყვანე რიცხვი და შეამოწმე, არის თუ არა ის 10-ის ან 20-ის ტოლი.
#not — შეიყვანე რიცხვი და not-ის გამოყენებით შეამოწმე, არის თუ არა ის 10-ისგან განსხვავებული.
#if — შეიყვანე რიცხვი. თუ რიცხვი დადებითია, დაბეჭდე Positive.
#if + else — შეიყვანე რიცხვი და დაადგინე, არის თუ არა ის ლუწი.
#if + elif + else — შეიყვანე ქულა და გამოიტანე:

#90–100 → A
#70–89 → B
#50–69 → C
#50-ზე ნაკლები → Fail

#while — while-ის გამოყენებით დაბეჭდე რიცხვები 10-დან 1-მდე.
#for — for-ის გამოყენებით დაბეჭდე 1-დან 20-მდე მხოლოდ ლუწი რიცხები.

print('my name is temo, im 16, i live in marneuli')
name = 'temo'
age = 16
text = input('enter youre name and where you live: ')
print(text)

num = int(input('enter youre number: '))
num2 = int(input('enter youre second number: '))
print(num + num2)

price = float(input('enter youre products price: '))
pricesec = float(input('enter youre products total: '))
print(price * pricesec)

num1 = 5
num2 = 10
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)

num1 = 10
num2 = 12
print(num1 == num2)

age = 16
print(age > 13 and 18 < age)

num = 10
print(num == 10 or 20 == num)

num = 20
print(not num == 20)

num = 10
if num >= 0:
    print('positive')

num = 20
if num % 2 == 0:
    print('ლუწია')
else:
    print('კენტია')

score = 100
if score > 90 < 100:
    print('A')
elif score > 70 < 89:
    print('B')
elif score > 50 < 69:
    print('C')
else:
    print('fail')

i = 10
while i >= 1:
    print(i)
    i -= 1


for i in range(1, 20):
    if i % 2 == 0:
        print(i)

