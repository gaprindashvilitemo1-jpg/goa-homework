# 5. მომხმარებელს შემოატანინეთ რიცხვი და გამოიტანეთ 1-დან ამ რიცხვამდე მხოლოდ კენტი რიცხვები.

num = int(input('enter youre number: '))
i = 1

while i <= num:
    if i % 2 != 0:
        print(i)
    i += 1
