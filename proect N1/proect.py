pas = (input('enter youre password: '))

while pas != 'python123':
    print('password incorect')
    pas = (input('enter youre password: '))
print('right password')

name = input('enter youre name: ')
lastname = input('enter youre lastname: ')
age = int(input('enter youre age: '))
city = input('enter youre city: ')
country = input('enter youre county: ')
balance = float(input('youre balance: '))

is_adult = age >= 18

print(f'youre name {name}, last name {lastname}, enter youre age {age},where you live {city}, whats youre country {country},and whatss youre balance {balance}, {type(name)}{type(age)},{type(city)}{type(country)}{type(balance)}')

name_of_product = input('youre products name: ')
price = float(input('price of the product: '))
how_much = int(input('how much product: '))

total = price * how_much
print(total)

if balance >= total:
    if how_much > 10 and total > 100:
        discount = 20
        print('you have 20% discount on the product')
    elif how_much > 50:
        discount = 10
        print('you have 10% discount on youre product')
    else:
        discount = 0
        print('didnt recieved discount')

    discount_amount = (total * discount) // 100
    finnal_price = total - discount_amount
    balance = balance - finnal_price 
    print(finnal_price)
    print(balance)

    bonus_price = int(finnal_price // 10)
    point = finnal_price % 10
    print(bonus_price)
    print(point)

else:
    print('you dont have enought money')

total_expenses = 0

while True:
    expenses  = float(input('how much you spend: '))
    if expenses <= 0:
        print('expenses are end')
        break
    total_expenses + expenses

print(f'total expenses {total_expenses}')

balance_square = balance ** 2
balance_cube = balance ** 3
print('balance_square')
print('balance-cube')

int_balance = int(balance)
if int_balance % 2 == 0:
    print('even')
else:
    print('odd')

print(balance)

    



        
        

