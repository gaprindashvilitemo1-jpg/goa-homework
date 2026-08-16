# 1) იპოვე ყველა ლუწი რიცხვის ჯამი 1-დან 100-მდე
total = 0

for i in range(1, 100):
    if i % 2 == 0:
        total += i
print(total)