#8) მომხმარებელს შემოაყვანინე ტექსტი. isdigit() მეთოდით შეამოწმე,
#  არის თუ არა შეყვანილი ტექსტი მხოლოდ ციფრები. თუ არის, slicing-ით [0:3] დაბეჭდე პირველი 3 ციფრი.

text = input('enter youre text: ')

text = text.isdigit()
text = text[0:3]

print(text)