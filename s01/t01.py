print("mip230310")
print("Задача 1.")
print("За день машина проезжает n километров. Сколько дней нужно,\n"
      + "чтобы проехать маршрут длиной m километров?\n"
      + "При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.\n"
      + "Пример: Input: n = 700 и m = 750; Output: 2")

n = int(input("Input N, скорость: "))
m = int(input("Input M, растояние: "))

day = int((m-1)//n+1)

print(f"Нужно дней для преодоления растояния [{n}], с скоростью [{m}]: ", day)