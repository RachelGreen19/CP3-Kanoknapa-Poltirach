usernameInput = input("username : ")
passwordInput = input("password : ")
if usernameInput and passwordInput == "admin":
    print("Welcome to IT Queen's Shop")
    print("Select an item")
    print("1. Banana =", 10)
    print("2. Orenge =", 15)
    print("3. Kiwi =", 30)
    print("4. Melon =", 120)
    print("5. Mango =", 50)
    customerSelected = (input(">>"))
    if customerSelected == "1":
        amountInput = int(input("amount = "))
        print("Banana x ",amountInput)
        print("total =",10*amountInput)
    if customerSelected == "2":
        amountInput = int(input("amount = "))
        print("Orenge x ",amountInput)
        print("total =",15*amountInput)
    if customerSelected == "3":
        amountInput = int(input("amount = "))
        print("Kiwi x ", amountInput)
        print("total =",30*amountInput)
    if customerSelected == "4":
        amountInput = int(input("amount = "))
        print("Melon x ", amountInput)
        print("total =",120*amountInput)
    if customerSelected == "5":
        amountInput = int(input("amount = "))
        print("Mango = ", amountInput)
        print("total =",50*amountInput)
    print("-----------Thank you------------")
else:
    print("Try again")
