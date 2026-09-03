# 6. Nested while loop-ის გამოყენებით შექმენით რიცხვების სამკუთხედი 1-დან 5-მდე.

i = 1

while i <= 5:
    j = 1

    while j <= i:
        print(j, end=" ")
        j += 1

    print()
    i += 1
