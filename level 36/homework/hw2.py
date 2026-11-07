# 2) შექმენი tuple, რომელშიც შეინახავ 6 სხვადასხვა ცხოველის სახელს. გამოიყენე while ციკლი,
# რათა თითოეული ცხოველის სახელი ცალ-ცალკე დაბეჭდო. შემდეგ ყველა ცხოველი დაამატე ახალ list-ში და დაბეჭდე სია.

animals = ('lion', 'tiger', 'crocodile', 'dog', 'cat', 'rabbit')

index = 0

while index < len(animals):
    print(animals[index])
    index += 1

animals_list = []
index = 0
while index < len(animals):
    animals_list.append(animals[index])
    index += 1
print(animals_list)