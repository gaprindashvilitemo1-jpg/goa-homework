#7) მომხმარებელს შეაყვანინეთ რიცხვები. თუ შეიყვანს 0-ს, გამოიყენეთ break. ყველა დადებითი რიცხვი დაამატეთ total ცვლადში, ხოლო უარყოფითი რიცხვები გამოტოვეთ.

total = 0

while True:
    num = int(input('enter youre number: '))
    if num == 0:
        break
    if num > 0:
        total += num

print(total)
