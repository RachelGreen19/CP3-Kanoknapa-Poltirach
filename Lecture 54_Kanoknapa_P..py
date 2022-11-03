def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)


print("Welcome to Ooky Spooky Shop")
x = login()
if x == True:
    showMenu()
    if menuSelect() == 1:
        totalPrice = int(input("Total Price: "))
        print("Total Incl. VAT: ",vatCalculate(totalPrice))
    elif 2:
        print("Total Incl. VAT: ",(priceCalculate()))
else:
    print("Try again")




