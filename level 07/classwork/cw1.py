#level 06:
#1) შექმენი ორი ცვლადი სადაც მომხმარელებს შემოატანინებ რიცხვებს
#2) პირველ დავალებაში შექმნილი ცვლადები გადაიყვანე ინტეჯერად რო მოახდინო მათემატიკური მოქმედებები
#3) დაბეჭდე ყველა მათემატიკური მოქმედება წინა დავალებაში შექმნილ ცვლადებზე (+, -, *, /, %, //)
#4)  შექმენი ცვლადები სადაც მომხმარებელს შემოატანინებ სახელს და ასაკს
#5) დაბეჭდე f სტრინგით "My name is {მომხმარებლის სახელი} and my age is {მომხმარებლის ასაკი}" 
#(გამოიყენე მეოთხე დავალებაში შექმნილი ცვლადები)


#1)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(num1 + num2)

#2) #3)
print("ჯამი:", num1 + num2)
print("გამოკლება:", num1 - num2)
print("გამრავლება:", num1 * num2)
print("გაყოფა:", num1 / num2)
print("ნაშთი:", num1 % num2)
print("მთელი გაყოფა:", num1 // num2)

#4) #5)
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and my age is {age}")