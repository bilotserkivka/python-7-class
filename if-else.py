
user_name = input("Як тебе звати? ")
user_age = int(input("Скільки тобі років? "))
# print("Користувачу", user_name, " зараз ",user_age, "років")
# print(f"Користувачу {user_name}  зараз {user_age} років, а через 3 роки йому буде {user_age + 3}")
if user_age > 13:
    print(f"{user_name}, ти старший за семикласника")
    print("Я буду звертатися на ви")
elif user_age == 13:
    print(f"{user_name}, ти семикласник, давай дружити")
elif user_age <= 0:
    print(f"{user_name}, ти не правильно ввів вік")
else:
    print(f"{user_name}, ти молодший за семикласника")
    print("Я буду звертатися на ти")
print("Кінець програми")
