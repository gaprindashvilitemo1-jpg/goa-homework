#2) while loop-ის გამოყენებით გამოთვალეთ 1-დან 100-მდე ყველა კენტი რიცხვის ჯამი.

total = 0
num = 1

while num <= 100:
    if num % 2 != 0:
        total += num
    num += 1

print(total)