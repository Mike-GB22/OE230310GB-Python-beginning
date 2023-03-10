print("mip230310")
print("Задача №8. Домашка\n"
      + "Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,\n"
      + "если разрешается сделать ОДИН РАЗЛОМ!!! по прямой между дольками\n"
      + "(то есть разломить шоколадку на два прямоугольника).\n"
      + "3 2 4 -> yes\n"
      + "3 2 1 -> no\n"
      )

print("Введите размер шокоадки:")
n = int(input("Линий: "))
m = int(input("Полосочек: "))
k = int(input("\nСколько долек должно быть в нашем отломленном кусочке: "))

flagWeCanDoIt = False
print("\nВозможные кусочки шоколадки:")
print(" - деление по полосочкам:")
for i in range(m,0, -1):
      total = n * i 
      print(f"   - {n} x {i} = {total}")
      if total == k:
            flagWeCanDoIt = True
            print("     ^^^^^^^^^^^^^^ как раз то что нам нужно")            

print(" - деление по линиям:")
for j in range(n-1,0, -1):
      total = m * j 
      print(f"   - {j} x {m} = {total}")
      if total == k:
            flagWeCanDoIt = True
            print("     ^^^^^^^^^^^^^^ как раз то что нам нужно")            

yesNo = ["Нет", "Да!"]
print("\nИ теперь ответ.\n"
      + f"Можем ли мы одним делением шоколадки размером [{n} х {m}] получить кусочек из [{k}] долек?\n"
      + f"И ответ... {yesNo[flagWeCanDoIt]} можем!\n")





