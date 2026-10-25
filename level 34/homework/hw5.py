# 5) შექმენი ორი Set სახელად `available_books` და `new_books`. პირველში შეინახე ბიბლიოთეკაში არსებული 6 წიგნის სახელი,
#  ხოლო მეორეში — 4 ახალი წიგნის სახელი. ზოგიერთი წიგნი ორივე Set-ში უნდა გვხვდებოდეს. თავდაპირველად გამოიყენე `intersection()` მეთოდი, რათა გაიგო, რომელი ახალი წიგნები უკვე არსებობს
#  ბიბლიოთეკაში.
#  შემდეგ გამოიყენე `union()` მეთოდი, რათა მიიღო ბიბლიოთეკის განახლებული წიგნების სია. დაბეჭდე ორივე შედეგი და საბოლოო წიგნების რაოდენობა.

available_books = {"Harry Potter", "The Hobbit", "1984", "It", "Dune", "Twilight"}

new_books = {"Harry Potter", "Dune", "The Hunger Games", "Dracula"}

e_books = available_books.intersection(new_books)
u_books = new_books.union(e_books)
print(u_books)
print(len(u_books))

