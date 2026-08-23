#3.მომხმარებელს შეაყვანინე 7 რიცხვი და გამოიტანე მხოლოდ დადებითი რიცხვები.

for i in range(7):
    num = int(input('enter youre number: '))
    if num < 0:
        continue
    print(num)