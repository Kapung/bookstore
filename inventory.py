import json
from book import Book

class Inventory():

    def __init__(self) -> None:
        #Creates empty inventory and loads all the books.json into it
        self.__current_inventory = {}
        self.load_inventory()


    def add_book(self, isbn, book):
        #Adds new book to current inventory and saves it to books.json
        self.__current_inventory[isbn] = book
        book.save()


    def remove_book(self, isbn):
        #Checks if the ISBN is in the inventory keys and tries to remove them from the books.json as well as inventory
        if self.__current_inventory:
            if isbn in self.__current_inventory.keys():
                file = self.load_info()
                try:
                    file = [book for book in file if book.get("ISBN") != isbn]

                    with open("books.json", "w") as books:
                        json.dump(file, books, indent = 4)

                except Exception as e:
                    pass

                print(f"Book removed: {self.__current_inventory.pop(isbn)}")
            else:
                print(f"The book could not be found by {isbn}")
        else:
            print("No values to delete")


    def update(self, type_search, update_value):
        if self.__current_inventory:
            pass
        else:
            raise Exception("No values to update")

    def load_info(self):
        #Loads books.json and returns contents
        try:
            with open("books.json", "r") as books:
                return json.load(books)
        except Exception as e:
            return []
        
    def get_different_book_number(self):
        return len(self.__current_inventory)
    
    def get_inventory(self):
        inv = []
        if self.__current_inventory:
            for value in self.__current_inventory.values():
                inv.append(value)
            return inv
        else:
            print("Inventory empty")

    def search_values(self, type_search, value):
        if self.__current_inventory:
            query = None
            #Checks for search type
            match type_search:
                case "Title":
                    query = [book for _, book in self.__current_inventory.items() if value.lower() in book.get_title().lower()]
                case "Author":
                    query = [book for _, book in self.__current_inventory.items() if value.lower() in book.get_author().lower()]
                case "ISBN":
                    query = [book for _, book in self.__current_inventory.items() if value in book.get_isbn()]
                case "Year":
                    query = [book for _, book in self.__current_inventory.items() if int(value) == book.get_year()]
                case "Genre":
                    query = [book for _, book in self.__current_inventory.items() if value.lower() in book.get_genre().lower()]
                case "Price":
                    query = [book for _, book in self.__current_inventory.items() if book.get_price() >= float(value)]
                case "Quantity":
                    query = [book for _, book in self.__current_inventory.items() if book.get_quantity() >= int(value)]
                case _:
                    raise Exception("Value type not found")
                
            #If books found print all of them
            if query:
                return query
            else:
                print("Books not found")

    def load_inventory(self):
        current_inventory = self.load_info()

        #Loads all the books into current inventory
        for book in current_inventory:
            packed_book = Book(book["Title"], book["Author"], book["ISBN"], book["Year"], book["Genre"], book["Price"])
            self.__current_inventory[packed_book.get_isbn()] = packed_book


    def print_inventory(self):
        if self.__current_inventory:
            for value in self.__current_inventory.values():
                print(value)
        else:
            print("Inventory empty")
        
