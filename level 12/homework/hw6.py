# 6. მომხმარებელს შემოატანინეთ პაროლი. სანამ პაროლი არ იქნება "python123", მანამდე მომხმარებელს თავიდან შეაყვანინეთ პაროლი.

pas = input('enter youre password: ')

while pas != 'python123':
    print('wrong password')
    pas = input('enter youre password: ')
print("right pasword")
