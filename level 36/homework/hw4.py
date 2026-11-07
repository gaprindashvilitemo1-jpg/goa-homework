# 4) შექმენი list, რომელშიც შეინახავ 12 რიცხვს. გამოიყენე while ციკლი და დაბეჭდე მხოლოდ უარყოფითი რიცხვები.
# ყველა დადებითი რიცხვი კი დაამატე ცალკე tuple-ში (შეგიძლია ჯერ ცალკე List გამოიყენო და შემდეგ Tuple-ად გადააქციო).


numbers = [5, -2, 8, -4, 10, -7, 3, -1, 6, -9, 12, -3]

positive = []

i = 0

while i < len(numbers):
    if numbers[i] < 0:
        print(numbers[i])
    else:
        positive.append(numbers[i])

    i += 1

positive_tuple = tuple(positive)

print(positive_tuple)