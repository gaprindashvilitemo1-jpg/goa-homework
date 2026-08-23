#ეტაპი 1: მომხმარებლის რეგისტრაცია და ავტორიზაცია
name = input("შეიყვანეთ სახელი: ")

surname = input("შეიყვანეთ გვარი: ")

age = int(input("შეიყვანეთ ასაკი: "))

city = input("შეიყვანეთ ქალაქი: ")

country = input("შეიყვანეთ ქვეყანა: ")

animal = input("საყვარელი ცხოველი: ")

sport = input("საყვარელი სპორტი: ")

balance = float(input("შეიყვანეთ საწყისი ბალანსი: "))


has_ticket = True
has_invitation = False

can_enter = has_ticket and has_invitation
print("ღონისძიებაზე დაშვება:", can_enter)

print(f"გამარჯობა {name} {surname}, თქვენ ცხოვრობთ {city}, {country}-ში.")


password = ""

while password != "python123":
    password = input("შეიყვანეთ პაროლი (python123): ")
    if password == 'python123':
        print('წარმატებით გაიარეთ ავტორიზაცია.')
    else:
        print('პაროლი არასწორია.')


#ეტაპი 2: მთავარი მენიუ (WHILE LOOP)
is_running = True

while is_running:
    print("\n--- მეგა-სისტემის მენიუ ---")
    print("1. საბანკო ემულატორი და ხარჯები")
    print("2. მათემატიკური ჰაბი და ტაბულა")
    print("3. სტრინგების ანალიზატორი")
    print("4. მაღაზიის მარაგები და ფასდაკლება")
    print("5. გეომეტრიული კალკულატორი")
    print("6. სტატისტიკა და შეფასებები")
    print("7. ციკლების ტესტირება")
    print("8. გამოსვლა")
    choice = int(input("აირჩიეთ ოპერაცია (1-8): "))

    if choice == 1:
        # ეტაპი 3: საბანკო ემულატორი
        print(f"მიმდინარე ბალანსი: {balance}")
        withdraw = float(input("შეიყვანეთ გასატანი თანხა: "))

        if withdraw > 0:
            if withdraw <= balance:
                balance = balance - withdraw
                print(f"თანხა წარმატებით გაიტანეთ. ახალი ბალანსი: {balance}")
            else:
                print("არასაკმარისი ბალანსი")
        else:
            print("არასწორი თანხა")
        total_expenses = 0
        while True:
            expense = float(input("შეიყვანეთ ხარჯი (0 - დასრულება): "))
            if expense == 0:
                break
            if expense < 0:
                continue
            total_expenses += expense
            print(f"სულ დახარჯული თანხა: {total_expenses}")

    elif choice == 2:
        # ეტაპი 4: მათემატიკური ჰაბი
        num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
        num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

        print(f"ჯამი (+): {num1 + num2}")
        print(f"სხვაობა (-): {num1 - num2}")
        print(f"ნამრავლი (): {num1 * num2}")
        print(f"განაყოფი (/): {num1 / num2}")
        print(f"ნაშთი (%): {num1 % num2}")
        print(f"მთელზე გაყოფა (//): {num1 // num2}")
        print(f"ხარისხი (): {num1 ** num2}")

        print(f"--- {num1}-ის გამრავლების ტაბულა ---")
        for i in range(1, 10):
            print(f"{num1} * {i} = {num1 * i}")
    elif choice == 3:
        # ეტაპი 5: სტრინგების ანალიზატორი
        text = input("შეიყვანეთ რაიმე ტექსტი: ")
        if len(text) > 10:
            print("ტექსტი არის გრძელი.")
        else:
            print("ტექსტი არის მოკლე.")

        print(f"თქვენი საყვარელი ცხოველია: {animal}")
        print(f"თქვენი საყვარელი სპორტია: {sport}")
        print(f"პროფილის მფლობელი: {name}")

    elif choice == 4:
        # ეტაპი 6: ფასდაკლება და მარაგები
        price = float(input("შეიყვანეთ პროდუქტის ფასი: "))
        discount = float(input("შეიყვანეთ ფასდაკლების % (მაგ: 20): "))
        quantity = int(input("შეიყვანეთ პროდუქტის რაოდენობა: "))

        final_price = price - (price * (discount / 100))
        total_cost = final_price * quantity
        print(f"საბოლოო გადასახდელი თანხა: {total_cost}")

        if quantity > 0:

            if quantity > 10 and total_cost > 200:
                print("საბითუმო შეკვეთა - მარაგი საკმარისია")
            else:
                print("მცირე შეკვეთა")
        else:
            print("მარაგი არ არის!")
    elif choice == 5:
        # ეტაპი 7: გეომეტრიული კალკულატორი 
        width = float(input("შეიყვანეთ მართკუთხედის სიგანე: "))
        height = float(input("შეიყვანეთ მართკუთხედის სიმაღლე: "))

        area = width * height
        print(f"მართკუთხედის ფართობი: {area}")

        sq_num = float(input("შეიყვანეთ რიცხვი კვადრატში ასაყვანად: "))
        square = sq_num ** 2
        print(f"რიცხვის კვადრატი: {square}")

    elif choice == 6:
        # ეტაპი 8: სტატისტიკა და შეფასება
        if age < 6:
            print("კატეგორია: Kindergarten")
        elif age < 18:
            print("კატეგორია: School")
        else:
            print("კატეგორია: University or Work")

        score = float(input("შეიყვანეთ გამოცდის ქულა: "))

        if score >= 90:
            print("Grade C")
        elif score >= 70:
            print("Grade B")
        elif score >= 50:
            print("Grade A")
        else:
            print("Failed")

        if age >= 16 and age <= 60:
            print("შრომისუნარიანი ასაკი")

    elif choice == 7:
        # ეტაპი 9: ციკლების ტესტირება
        print("რიცხვები 20-დან 1-მდე:")
        count = 20
        while count > 0:
            print(count)
            count -= 1

        print("1-დან 50-მდე ლუწი რიცხვები:")
        for i in range(1, 50):
            if i % 2 == 0:
                print(i)

    elif choice == 8:
        print("პროგრამა დასრულდა.")
        is_running = False

    else:
        print('არასწორი არჩევანი გააკეთე!')






