#4. Nested while loop-ის გამოყენებით დაბეჭდეთ 1-დან 5-მდე რიცხვების გამრავლების ტაბულა.


i = 1

while i <= 5:
    j = 1

    while j <= 5:
        print(i, "x", j, "=", i * j)
        j += 1

    i += 1