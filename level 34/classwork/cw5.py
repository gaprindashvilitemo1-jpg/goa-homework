# 5) შექმენი სამი Set სახელად `python_students`, `javascript_students` და `react_students`. თითოეულში შეინახე იმ მოსწავლეების სახელები,
#  რომლებიც შესაბამის ტექნოლოგიას სწავლობენ. გამოიყენე `union()` მეთოდი, რათა მიიღო ყველა უნიკალური მოსწავლის სახელი.
#   შემდეგ გამოიყენე `intersection()` მეთოდი `python_students` და `javascript_students` Set-ებზე,
#  რათა იპოვო მოსწავლეები, რომლებიც ორივე ტექნოლოგიას სწავლობენ. ორივე შედეგი დაბეჭდე ეკრანზე

python_students = {"gio", "nika", "ana", "luka"}
javascript_students = {"ana", "luka", "mari", "saba"}
react_students = {"nick", "mari", "dato"}

all_students = python_students.union(javascript_students, react_students)
print(all_students)

both_students = python_students.intersection(javascript_students)
print(both_students)
