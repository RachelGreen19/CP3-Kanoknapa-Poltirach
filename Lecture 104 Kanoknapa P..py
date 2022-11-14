class Customer:
    name = ""
    lastname = ""
    age = 0
    def addCart(self):
        print("Added to",self.name,self.lastname,"'s Cart")
#อะไรที่เกิดหลังพิมพ์เขียวค่อยใส่ทีหลัง
customer1 = Customer()
customer1.name = "Kittikorn"
customer1.lastname = "P"
customer1.addCart()

customer2 = Customer()
customer2.name = "Katya"
customer2.lastname = "Zamolodchikova"
customer2.addCart()

customer3 = Customer()
customer3.name = "Trixie"
customer3.lastname = "Mattel"
customer3.addCart()

customer4 = Customer()
customer4.name = "Kim"
customer4.lastname = "Possible"
customer4.addCart()