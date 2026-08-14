#4) მომხმარებელს შეაყვანინეთ რიცხვები. სანამ მომხმარებელი არ შეიყვანს 0-ს, დაამატეთ რიცხვები total ცვლადში. 0-ის შეყვანისას გამოიყენეთ break და ბოლოს გამოიტანეთ ჯამი.

total = 0

while True:
    num = int(input('enter youre num: '))
    if num == 0:
        break
    total += num

print(total)
