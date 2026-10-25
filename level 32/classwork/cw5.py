# 5) შექმენი Set სახელად `languages`, რომელშიც იქნება 4 პროგრამირების ენა. `len()` ფუნქციით გაიგე ელემენტების რაოდენობა, `discard()` მეთოდით სცადე ისეთი ენის წაშლა,
# რომელიც Set-ში არ არსებობს, ხოლო `in` ოპერატორით შეამოწმე, არის თუ არა `"Python"` Set-ში. ბოლოს დაბეჭდე Set.

languages = {'python', 'html', 'css', 'javascript', 'c++'}

print(len(languages))
languages.discard('anything')
print('python' in languages)