# 4) შექმენი Dictionary სახელად product, რომელშიც შეინახავ პროდუქტის სახელს, კატეგორიას, ფასს და რაოდენობას.
# შემდეგ შეცვალე პროდუქტის ფასი და რაოდენობა ახალი მნიშვნელობებით. დაბეჭდე განახლებული Dictionary.

product = {
    "name": "Phone",
    "category": "electronics",
    "price": 1500,
    "quantity": 10
}


product["price"] = 1200
product["quantity"] = 5

print(product)