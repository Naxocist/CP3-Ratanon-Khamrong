class Customer:
    name = ""
    Lastname = ""
    age = 0

    def addCart(self):
        print("Added to " + self.name + " " + self.Lastname + "'s cart")


customer1 = Customer()
customer1.name = "Somchai"
customer1.Lastname = "HII"
customer1.addCart()

customer2 = Customer()
customer2.name = "Ratanon"
customer2.Lastname = "Khamrong"
customer2.addCart()

customer3 = Customer()
customer3.name = "Pomipon"
customer3.Lastname = "Tumarai"
customer3.addCart()

customer4 = Customer()
customer4.name = "Peemapot"
customer4.Lastname = "Tatawan"
customer4.addCart()
