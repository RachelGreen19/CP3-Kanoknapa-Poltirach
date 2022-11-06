menulist = []
pricelist = []

def showBill():
  print("--------------My shop---------------")
  for i in range(len(menulist)):
    print(menulist[i],pricelist[i])
  print("Total:", sum(pricelist), "THB")

while True:
  menuName = input("Plese Enter Menu :")
  if(menuName.lower() == "exit"):
    break
  else:
    menuPrice = int(input("Price: "))
    menulist.append(menuName)
    pricelist.append(menuPrice)
showBill()



