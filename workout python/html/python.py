# 1)კომენტარების სახით ახსენით თუ რასაკეთებს .append() .insert() .remove() .pop()
# 2)გააკეთეთ თითო მაგალითი სიებზე  .append() .insert() .remove() .pop() ის გამოყენებით
# 3)კომენტარების სახით ახსენით თუ რასაკეთებს sort() reverse() count() index() და შექმენით თქვენთვის სასურველი სია მაგ: [“apple”, “grape”, “peach”, “pineaple”] და გააკეთეთ თითო მაგალითი ზემოთ მოცემულ მეთოდებზე
# 4)კომენტარების სახით ახსენით თუ რაარის tuple და რაში ვიყენებთ მას
# 5)შექმენით touple სახელად city რომელშიც იქნება 5 ქალაქი “გორი”, “თბილისი” ,”ბათუმი”, “ქუთაისი” და დაბეჭდეთ აქედან პირველი და მესამე ელემენტები
# 6)მომხმარებელს შემოაყვაინეთ მისი საყვარელი სპორტი და შემდეგ დაბეჭდეთ მისი პირველი და ბოლო ასო(ინდექსების გამოყენებით)

#1)
# .append() - ამატებს რაიმე ტექსტს ან რიცხვს სიის ბოლოში.

#2)
fruits = ["apple", "grape", "peach", "pineaple"]

fruits.append('orange')
print(fruits)


# .insert() - შეგვიძლია რაიმე წინადადების ან რიცხვის ჩასვა რომელ ინდექსზეც გვინდა

fruits = ["apple", "grape", "peach", "pineaple"]

fruits.insert(2, 'orange')
print(fruits)


# .remove() - ჩვენ შეგვიძლია რომელი ტექსტიც ან რიცხვიც გვინდა წავშალოთ

fruits = ["apple", "grape", "peach", "pineaple"]

fruits.remove('apple')
print(fruits)

# .pop() - ჩვენ ვიღებთ ტექსტს მხოლოდ ბოლოს სიაში დაწერილს

fruits = ["apple", "grape", "peach", "pineaple"]

fruits.pop()
print(fruits)

#3)
# .sort() - თანმიმდევრულად აწყობს ანბანის მიხედვით ტექსტს ან რიცხვს სიაში

fruits = ["apple", "grape", "peach", "pineaple"]

fruits.sort()
print(fruits)

# .reverse() - აბრუნებს ჩვენს სიას და ბოლოდან დაწყებული პირველით დაიწყება.

fruits = ["apple", "grape", "peach", "pineaple"]

fruits.reverse()
print(fruits)

# .count() - ითვლის თუ რამდენჯერ გვხვდება წინადადება  სიაში.

fruits = ["apple", "grape", "peach", "pineaple"]

counted = fruits.count('grape')

print(counted)

# .index() - გვეუბნება თუ რომელ ინდექზე წერია წინადადება ან რიცხვი

fruits = ["apple", "grape", "peach", "pineaple"]

fruit = fruits.index('peach')
print(fruit)

#4)
# tuple - არის იგივე ნაირი სია ოღონდ მასში შეტანილი ინფორმაცისს შეცვლა ან წაშლა არ შეგვიძლია, ის გამოიყენება უფრო პირადი ინფორმაციის შესანახად.

#5)
city = ("გორი", "თბილისი" , "ბათუმი", "ქუთაისი")

print(city[0])
print(city[2])

#6)
sport = input('enter youre fav sport: ')

print(sport[0])
print(sport[-1])








