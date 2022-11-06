menulist = []

def showBill():
  total = 0
  print("--------------My shop---------------")
  for i in range(len(menulist)):
    print(menulist[i])
    total += menulist[i][1]
  print("Total:",total,"THB")


while True:
  menuName = input("Plese Enter Menu :")
  if(menuName.lower() == "exit"):
    break
  else:
    menuPrice = int(input("Price: "))
    menulist.append([menuName,menuPrice])

print(menulist)
showBill()