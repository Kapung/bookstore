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

                    if len(file) == self.get_different_book_number():
                        print(f"No books by that ISBN in the inventory")
                    with open("books.json", "w") as books:
                        json.dump(file, books, indent = 4)

                except Exception as e:
                    print(e)

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

    def load_info(self):
        #Loads books.json and returns contents
        try:
            with open("books.json", "r") as books:
                return json.load(books)
        except Exception as e:
            return []
        
    def get_different_book_number(self):
        return len(self.__current_inventory)


    def find(self, type_search, value):
        if self.__current_inventory:
            query = None
            #Checks for search type
            match type_search:
                case "title":
                    query = [book for _, book in self.__current_inventory.items() if book.get_title() == value]
                case "author":
                    query = [book for _, book in self.__current_inventory.items() if book.get_author() == value]
                case "genre":
                    query = [book for _, book in self.__current_inventory.items() if book.get_genre() == value]
                case _:
                    raise Exception("Value type not found")
            
            #If books found print all of them
            if query:
                for book in query:
                    print(book)
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
            raise Exception("Inventory empty")
        
