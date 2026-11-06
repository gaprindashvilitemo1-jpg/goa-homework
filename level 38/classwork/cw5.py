# 5) შექმენი Dictionary სახელად game, რომელშიც შეინახავ თამაშის სახელს, ჟანრს და რეიტინგს. შემდეგ:
# დაამატე ახალი Key developer, რომელშიც შეინახავ თამაშის შემქმნელის სახელს.
# შეამოწმე in ოპერატორით, არსებობს თუ არა rating Key.
# წაშალე genre Key.
# შეცვალე თამაშის სახელი.
# დაბეჭდე საბოლოო ობიექტი.

game = {
    'name': 'cs2',
    'type': 'online',
    'rating': 5
}

game["developer"] = "Steam"

print("rating" in game)

del game["type"]

game["name"] = "Minecraft"

print(game)

