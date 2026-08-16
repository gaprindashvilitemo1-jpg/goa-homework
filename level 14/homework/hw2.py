#2) მომხმარებელს შემოატანინე რიცხვი და დათვალე, რამდენი რიცხვია 1-დან ამ რიცხვამდე ისეთი, რომელიც 3-ზე იყოფა.

#2)
num = int(input("Enter a number: "))

count = 0

for i in range(1, num, 1):
    if i % 3 == 0:
        count += 1

print(count)