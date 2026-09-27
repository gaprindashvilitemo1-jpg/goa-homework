#9. შექმენი სია:
# ["Apple", "Samsung", "Xiaomi", "Huawei"]

# append() მეთოდის გამოყენებით დაამატე "Nokia".
# შემდეგ remove() მეთოდის გამოყენებით წაშალე "Xiaomi".
# გამოიტანე მიღებული სია.

fruits = ["Apple", "Samsung", "Xiaomi", "Huawei"]

fruits.append('Nokia')

remove = fruits.remove('Xiaomi')
print(remove)
print(fruits)