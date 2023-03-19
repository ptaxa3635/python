# Задание №1
# Создайте функцию, которая принимает в качестве параметра - натуральное целое число.
# Данная функция находит факториал полученного числа
# Например, факториал числа 3 это число 6.
# Теперь создайте список факториалов чисел от получившегося ранее факториала 6, до 1.
# В итоге, на вход программа получает например число 3, возвращает число 6 (факториал числа 3) и вам нужно сделать
# список из факториалов числа 6 в убывающем порядке. Находим факториал числа 6 - это 720, затем от числа 5 - это 120 и так
# далее вплоть до 1
# То есть, результирующий список будет выглядеть в нашем примере так:
# [720, 120, 24, 6, 2, 1]
def fac(n):
    if n == 0:
        return 1
        return fac(n-1) * n
        y=int(input())
        for i in range(y,0,-1):
            print(fac(i))


#Задание №2
import collections
pets = {

    1: {
        "Лаки": {
            "Вид питомца": "хомяк",
            "Возраст питомца": 2,
            "Имя владельца": "Надежда"
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 12,
            "Имя владельца": "Анна"
        },
    },
}

def get_suffix(age):
    if age == 1:
        return "год"
    elif age > 1 and age < 5:
        return "года"
    else:
        return "лет"

def create():
    print("### Комманда create")
    key = input("Кличка питомца: ")
    fields = ["Вид питомца", "Возраст питомца", "Имя владельца"]
    temp = {key: dict()}
    for field in fields:
        res = input(f"{field}: ")
        temp[key][field] = int(res) if res.isnumeric() else res
        last = collections.deque(pets, maxlen=1)[0]
        pets[last + 1] = temp

def read():
    print("### Комманда read")
    ID = input("Введите ID: ")
    pet = get_pet(ID)
    if not pet:
        print(f"Нет питомца с таким ID:{ID}")
        return
        key = [x for x in pets.keys()][0]
        string = f'Это {pets[key]["Вид питомца"]} по кличке "{key}". ' \
                 f'Возраст питомца: {pets[key]["Возраст питомца"]} {get_suffix(pets[key]["Возраст питомца"])}. ' \
                 f'Имя владельца: {pets[key]["Имя владельца"]}'
        print(string)

def update():
    print("### Комманда update")
    ID = int(input("Введите ID: "))
    pet = get_pet(ID)
    if not pet:
        print(f"Нет питомца с таким ID:{ID}")
        return

kkey = [x for x in pets.keys()][0]
print("Введите данные или оставьте поле пустым. Нажмите Enter")

temp = dict()
for key, value in pets[kkey].items():
    res = input(f"{key}: ")
    if res:
        temp[key] = int(res) if res.isnumeric() else res
        pets[kkey].update(temp)

def delete():
    print("### Комманда delete")
    ID = int(input("Введите ID: "))
    pets.pop(ID, None)

def get_pet(ID):
    return pets.get(ID, False)

def pets_list():
    for key, val in pets.items():
        print(f"ID:{key}", val)

commands = {
    "create": create,
    "read": read,
    "update": update,
    "delete": delete,
    "list": pets_list,
    "stop": 0
}

def print_commands():
    print("Список доступных комманд:")
    for key in commands:
        print("> ", key)
    while True:
        print_commands()
        command = input("Введите команду: ")
        if command not in commands.keys():
            continue
            if command == "stop":
                break
        commands[command]()
input("Продолжить...")

