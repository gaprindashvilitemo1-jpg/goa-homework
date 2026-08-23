#1.გამოიტანე რიცხვები 1-დან 15-მდე, მაგრამ არ გამოიტანო 7.

for i in range(1, 15):
    if i == 7:
        continue
    print(i)
