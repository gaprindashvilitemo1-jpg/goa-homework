#6) მომხმარებელს შეაყვანინეთ რიცხვები. თუ მომხმარებელი შეიყვანს უარყოფით რიცხვს, გამოიყენეთ break. დადებითი რიცხვები დაამატეთ total ცვლადში და ბოლოს გამოიტანეთ ჯამი.

total = 0

while True:
    num = int(input('enter youre number: '))
    if num < 0:
        break
    total += num

print(total)