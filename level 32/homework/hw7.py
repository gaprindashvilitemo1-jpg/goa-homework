# 7) შექმენი Set სახელად `animals`, რომელშიც იქნება 6 ცხოველი. `remove()` მეთოდით წაშალე ერთ-ერთი ცხოველი,
# `add()` მეთოდით დაამატე ახალი ცხოველი და `discard()` მეთოდით სცადე ისეთი ცხოველის წაშლა, რომელიც Set-ში არ არსებობს. ბოლოს დაბეჭდე Set.

animals = {'dog', 'cat', 'parot', 'tiger','lion'}

animals.remove('dog')
animals.add('bobcat')
animals.discard('leopardi')
print(animals)