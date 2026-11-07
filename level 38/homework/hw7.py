# 7) შექმენი Dictionary სახელად movie, რომელშიც შეინახავ ფილმის სახელს, რეჟისორს, გამოშვების წელს და ჟანრს. მომხმარებელს შემოატანინე Key და შეამოწმე in ოპერატორით,
# არსებობს თუ არა ის Dictionary-ში. შემდეგ წაშალე year Key და დაბეჭდე საბოლოო Dictionary.

movie = {
    "name": "interstellar",
    "director": "Christopher Nolan",
    "year": 2014,
    "genre": "Sci-Fi"
}

key = input('enter another dictionary key: ')
print('key' in movie)

del movie["year"]
print(movie)