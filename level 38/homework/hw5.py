# 5) შექმენი Dictionary სახელად school, რომელშიც შეინახავ სკოლის სახელს, მოსწავლეების რაოდენობას და ქალაქს. შემდეგ:
# - დაამატე ახალი Key director, რომელშიც შეინახავ დირექტორის სახელს.
# - შეამოწმე in ოპერატორით, არსებობს თუ არა students Key.
# - წაშალე city Key.
# - შეცვალე სკოლის სახელი.
# - დაბეჭდე საბოლოო Dictionary.

school = {
    "name": "public School",
    "students": 500,
    "city": "Tbilisi"
}

school['director'] = 'levani'
print('director' in school)

del school["city"]
school['name'] = 'Private school'
print(school)