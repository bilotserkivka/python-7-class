n = int(input("Скільки сторін у фігури? "))
if n == 3 or n ==4:
    if n == 3:
        a = int(input("Введіть сторону a = "))
        b = int(input("Введіть сторону b = "))
        c = int(input("Введіть сторону c = "))
        p = a + b + c
    else:
        a = int(input("Введіть сторону a = "))
        b = int(input("Введіть сторону b = "))
        c = int(input("Введіть сторону c = "))
        d = int(input("Введіть сторону d = "))
        p = a + b + c + d

    print(f"Периметр фігури: {p}")
else:
    print("Кількість сторін має бути 4 або 3")
    if 2 > n:
        if n <= 0:
            print("Такої фігури не існує")
        else:
            print("Це відрізок")
    elif n == 2:
        print("Це незамкнена фігура")
    else:
        print("Забагато сторін")
