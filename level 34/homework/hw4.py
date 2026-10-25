# 4) შექმენი სამი Set სახელად `monday`, `tuesday` და `wednesday`. თითოეულში შეინახე იმ მოსწავლეების სახელები, რომლებიც შესაბამის დღეს გაკვეთილს დაესწრნენ.
#  თითოეულ Set-ში უნდა იყოს მინიმუმ 5 სახელი და რამდენიმე სახელი უნდა მეორდებოდეს.
#  გამოიყენე `intersection()` მეთოდი, რათა იპოვო მოსწავლეები,
#   რომლებიც სამივე დღეს ესწრებოდნენ გაკვეთილს. დაბეჭდე მიღებული შედეგი და მათი რაოდენობა.

monday = {'guga','saba','nika','temo','luka'}
tuesday = {'saba','temo','gabrieli','mate','luka'}
wednesday = ('temo','leqso','vaja','amiko','edi')

students = monday.intersection(tuesday, wednesday)
print(students)
print(len(students))
