class User():

    def __init__(self, name, email) -> None:
        self.__name = name
        self.__email = email
        self.__shopping_cart = []


    def add_shopping_cart(self, book):
        self.__shopping_cart.append(book)


    def remove_shopping_cart(self, book):
        if self.__shopping_cart:
            self.__shopping_cart.remove(book)
        else:
            raise Exception("Shopping cart is already empty")
        

    def print_shopping_cart(self):
        if self.__shopping_cart:
            for item in self.__shopping_cart:
                print(item.get_title())
        else:
            raise Exception("Shopping cart is empty")