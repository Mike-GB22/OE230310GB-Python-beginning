print("mip230310")
print("Задача №4. Домашка\n"
      + "Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.\n"
      + "Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое\n"
      + "количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?\n"
      + "Прирмер:\n"
      + "6 -> 1 4 1\n"
      + "24 -> 4 16 4\n"
      + "60 -> 10 40 10\n"
      )
      


number = int(input("Введите общую сумму журавликов: "))
remainder = number % 6
if remainder != 0:
      number = number - remainder
      print("По идее сумма должна быть кратная 6, но сделаем допущение, что сумма журавликов равна:", number)

basisCount = number // 6
restCount = number - basisCount * 2
print("\nОтчет по каждому ребенку:")
print("Петя   сделал:", basisCount)
print("Катя  сделала:", restCount)
print("Сережа сделал:", basisCount)
