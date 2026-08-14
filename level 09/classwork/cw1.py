#level 09:
#1) მომხმარებელს შემოატანინე თავისი ასაკი, შემდეგ შეამოწმე თავისი ასაკია მეტია ან ტოლია 18ზე, კონსოლში გამოვიდეს "სრულწლოვანი ხართ".
#2) მომხმარებელს შემოატანინე ორი რიცხვი (num1, num2), შეამოწმე თუ num1 მეტია num2ზე გამოვიდეს "პირველი რიცხვი მეტია",
#3) მომხმარებელს კიღხე რა არის სწორი რიცხვი. თუ რიცხვი უდრის 777 დაბეჭდოს "რიცხვი გამოცნობილია"
#4) მომხმარებელს შემოატანინე თავისი სიმაღლე, თუ სიმაღლე მეტია ან უდრის 1.70ზე დაბეჭდოს "შენ მაღალი ხარ"

#1)
age = int(input("enter youre age: "))
if age >= 18:
    print("youre adult")

#2)
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

if num1 > num2:
    print("prists number is correct")

#3)
customer = int(input("what correct number: "))
if customer == 777:
    print("number is guessed")

#4)
height = int(input("enter youre height: "))
if customer >= 1.70:
    print("youre tall")