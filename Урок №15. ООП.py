# #Задание №1
# Создайте объект Autobus, который унаследует все переменные и методы родительского класса Transport и выведете его.
# Ожидаемый результат вывода:
# Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        class Bus(Transport):
            def __init__(self, name, max_speed, mileage):
                uper().__init__(name, max_speed, mileage)
            def __str__(self):
                return "Название автомобиля: "+self.name+" Скорость: " + str(self.max_speed)+" Пробег: " + str(self.mileage)
                bus = Bus("Renault Logan", 180, 12)
                print(bus)


# Задание №2
# Создайте класс Autobus, который наследуется от класса Transport.
# Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
# Используйте переопределение метода.
# Используйте следующий код для родительского класса транспортного средства:
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        def seating_capacity(self, capacity):
            return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"
            class car(Transport):
                def seating_capacity(self, capacity = 50):
                    return super().seating_capacity(capacity = 50)
                    bus = car("School Volvo", 180, 12)
                    print(bus.seating_capacity())