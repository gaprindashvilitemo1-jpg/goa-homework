#4)მომხამარებს შეაყვანინე 5 რიცხვი. თითვეული რიცხვი გამოიტანე მაგრამ თუ რიცხვი უარყოფითი გამოიყენე continue და არ დაბეჭდო.

for i in range(5):
    num = int(input('enter youre number: '))
    if num < 0:
        continue
    print(i)

