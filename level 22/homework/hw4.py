#4) მომხმარებელს შემოაყვანინე ტექსტი. replace() მეთოდით ყველა ჰარი (space) ჩაანაცვლე დეფისით ("-"),
# ხოლო upper() მეთოდით გადაიყვანე ყველა ასო დიდში. დაბეჭდე მიღებული ტექსტი.

text = input('enter youre text: ')

text = text.replace(" ", "-").upper()
print(text)