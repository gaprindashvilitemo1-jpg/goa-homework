# შექმენი ორი Set სახელად `fruits1` და `fruits2`.
#  პირველში შეინახე 5 ხილი, ხოლო მეორეში 5 ხილი. გამოიყენე `union()` მეთოდი, რათა მიიღო ორივე Set-ის ყველა უნიკალური ხილი და დაბეჭდე მიღებული შედეგი.

fruits1 = {'apple', 'banana', 'orange', 'peach', 'pomegranate'}
fruits2 = {'grape', 'mango', 'pear', 'watermelon', 'melon'}

n = fruits1.union(fruits2)

print(n)