# შექმენი tuple, რომელშიც შეინახავ 7 სხვადასხვა ქალაქის სახელს.
#  while ციკლის გამოყენებით დაბეჭდე თითოეული ქალაქი ცალ-ცალკე. ციკლი უნდა გაგრძელდეს მანამ, სანამ Tuple-ის ყველა ელემენტს არ დაბეჭდავ.

cities = ("Tbilisi", "Batumi", "Kutaisi", "Paris", "London", "Berlin", "Rome")

i = 0

while i < len(cities):
    print(cities[i])
    i += 1
