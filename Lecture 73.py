sysmenMenu = {"pork":10,"duck":20,"salmon":30}
menulist = []
def showBill():
  total = 0
  print("--------------My shop---------------")
  for i in range(len(menulist)):
    print(menulist[i])
    total = total + menulist[i][1]
  print("Total:",total,"THB")

while True:
  menuName = input("Plese Enter Menu :")
  if(menuName.lower() == "exit"):
    break
  else:
    menulist.append([menuName,sysmenMenu[menuName]])

print(menulist)
showBill()

