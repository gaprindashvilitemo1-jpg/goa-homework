# 2) შექმენი ორი Set სახელად `favorite_movies` და `popular_movies`. პირველში შეინახე 5 შენი საყვარელი ფილმის სახელი, ხოლო მეორეში — 6 პოპულარული ფილმის სახელი. დარწმუნდი,
#  რომ რამდენიმე ფილმი ორივე Set-ში გვხვდება. გამოიყენე `intersection()` მეთოდი, რათა იპოვო ფილმები, რომლებიც ორივე Set-შია. დაბეჭდე მიღებული შედეგი.

favorite_movies = {'breaking bad','dexter','aot','got','mentalist'}
popular_movies = {'breaking bad','The Dark Knight','Inception','Fight Club','The Wolf of Wall Street','Avatar'}

n = favorite_movies.intersection(popular_movies)

print(n)


