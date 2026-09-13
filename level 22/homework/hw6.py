#6) შექმენი სია words = ["hello", "world", "python"]. uppercase მეთოდების და join-ის გამოყენებით, შეაერთე ეს სიტყვები ტირეთი ("-") ისე,
#რომ თითოეული სიტყვის პირველი ასო იყოს დიდი (გამოიყენე title() ან capitalize()). დაბეჭდე შედეგი.

words = ["hello", "world", "python"]

word = '-'.join(words)
print(word.title())
