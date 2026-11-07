# 5) შექმენი ორი set, სახელად subjects1 და subjects2. თითოეულში შეინახე 5 სხვადასხვა სასკოლო საგანი. გამოიყენე for ციკლი, რათა პირველი Set-ის ყველა ელემენტი დაბეჭდო.
# შემდეგ გამოიყენე union() და intersection() მეთოდები და დაბეჭდე ორივე Set-ის გაერთიანება და საერთო ელემენტები.


subjects1 = {"Math", "English", "History", "Geography", "Physics"}
subjects2 = {"Math", "Biology", "Chemistry", "English", "Art"}

for i in subjects1:
    print(i)

print(subjects1.union(subjects2))

print(subjects1.intersection(subjects2))