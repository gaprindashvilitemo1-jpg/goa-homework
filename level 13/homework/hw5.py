#5) მომხმარებელს შემოატანინეთ რიცხვი n და while loop-ის გამოყენებით გამოთვალეთ 1-დან n-მდე ყველა ლუწი რიცხვის ჯამი.

n = int(input('ennter n: '))
total = 0
num = 1

while num <= n:
    if num % 2 == 0:
        total += num
    num += 1

print(total)
