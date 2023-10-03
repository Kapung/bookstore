class Inventory():

    def __init__(self) -> None:
        self.__current_inventory = {}


    def add_book(self, isbn, book):
        self.__current_inventory[isbn] = book
        book.save()


    def remove_book(self, isbn):
        if self.__current_inventory:
            if isbn in self.__current_inventory.keys():
                print(f"Book removed: {self.__current_inventory.pop(isbn)}")
            else:
                raise Exception("The book could not be found")
        else:
            raise Exception("No values to delete")


    def update(self, type_search, update_value):
        if self.__current_inventory:
            pass
        else:
            raise Exception("No values to update")


    def find(self, type_search, value):
        if self.__current_inventory:
            query = None
            match type_search:
                case "title":
                    query = [book for _, book in self.__current_inventory.items() if book.get_title() == value]
                case "author":
                    query = [book for _, book in self.__current_inventory.items() if book.get_author() == value]
                case "genre":
                    query = [book for _, book in self.__current_inventory.items() if book.get_genre() == value]
                case _:
                    raise Exception("Value type not found")
                
            if query:
                for book in query:
                    print(book)


    def print_inventory(self):
        if self.__current_inventory:
            for value in self.__current_inventory.values():
                print(value)
        else:
            raise Exception("Inventory empty")
        
