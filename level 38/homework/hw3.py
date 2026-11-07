# 3) შექმენი Dictionary სახელად country, რომელშიც შეინახავ ქვეყნის სახელს, დედაქალაქს, მოსახლეობას და ფართობს. მომხმარებელს შემოატანინე Key და in ოპერატორის გამოყენებით შეამოწმე,
# არსებობს თუ არა ეს Key Dictionary-ში. დაბეჭდე შესაბამისი შეტყობინება.

country = {
    "name": "Georgia",
    "capital": "Tbilisi",
    "population": 3700000,
    "area": 69700
}

key = input('enter key: ')

print(key in country)