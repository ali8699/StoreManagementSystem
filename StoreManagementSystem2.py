import sys


class Store:
    def __init__(self, listofproducts):
        self.availableproducts = listofproducts

    def displayAvailableproducts(self):
        print("\nThe Products we have in our store are as follows: ")
        print("==================")
        for product in self.availableproducts:
            print(product)

    def sellProduct(self, requestedProduct):
        if requestedProduct in self.availableproducts:
            print("The product you requested has now been bought")
            self.availableproducts.remove(requestedProduct)
        else:
            print("Sorry the product you have requested is currently not available in the store")

    def addProduct(self, returnedProduct):
        self.availableproducts.append(returnedProduct)
        print("Your new product has been added to the store")


class Customer:
    def __init__(self):
        self.product = []
        self.price = []

    def requestProduct(self):
        print("Enter the name of the product you'd like to buy>>")
        self.product = input()
        return self.product

    def returnProduct(self):
        print("Enter the name of the product you'd like to add>>")
        self.product = input()
        return self.product


def main():
    store = Store(["Iphone X", "Infix Note 10", "Samsung A52", "Iphone XS Max", "Samsung Note 10", "Iphone 13 Pro Max",
                   "Samsung A72", "Spark 4"])
    customer = Customer()
    done = False
    while done == False:
        print("""                      ======  STORE MENU  =======
                  1. Display all available product
                  2. Buy a product
                  3. Add/Return a product
                  4. Exit
                  """)
        choice = int(input("Enter Choice: "))
        if choice == 1:
            store.displayAvailableproducts()
            print("==================")

        elif choice == 2:
            store.sellProduct(customer.requestProduct())
        elif choice == 3:
            store.addProduct(customer.returnProduct())
        elif choice == 4:
            sys.exit()


main()
