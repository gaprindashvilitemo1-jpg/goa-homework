#level 12:

# 1. While loop ის გამოყენებით გამოიტანეთ 1დან 20 მდე რიცხვები

#2. გამოიტანეთ 5 დან 50 მდე მხოლოდ კენტი რიცხვები

#3. გამოიტანეთ რიცხვები 10 დან 50 მდე რომლებიც იყოფა 10ზე

#4. მომხმარებელ შემოატანინეთ პაროლი, სანამ პაროლი არ დაემთხვევა 102110 მანამდე ისე თავიდან შეიყვანოს მომხმარებელმა პაროლი


#1)
i = 1
while i <= 20:
    print(i)
    i += 1

#2)
i = 10
while i <= 50:
    print(i)
    i += 3

#3)
i = 10
while i <= 50:
    print(i)
    i += 10

#4)
password = input("enter pass: ")
while password != '102110':
    password = input('password is incorect, try again: ')
print('password incorect!')
