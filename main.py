from inventory import Inventory
from book import Book
from user import User
from window import Window

def main():
    test_books = [Book("Title1", "Daudi", "817525766-0", 1998, "Novel", 29.99),
                  Book("Title2", "John Smith", "123456789-0", 2005, "Mystery", 19.99),
                  Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1925, "Classic", 12.99),
                  Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "9780747532743", 1997, "Fantasy", 24.99),
                  Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", 1960, "Classic", 14.95),
                  Book("1984", "George Orwell", "9780451524935", 1949, "Dystopian", 9.99),
                  Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488", 1951, "Coming-of-Age", 11.49),
                  Book("The Hobbit", "J.R.R. Tolkien", "9780618260300", 1937, "Fantasy", 18.99),
                  Book("Pride and Prejudice", "Jane Austen", "9780141439518", 1813, "Classic", 8.95),
                  Book("The Da Vinci Code", "Dan Brown", "9780307474278", 2003, "Thriller", 16.99)]
    
    window = Window(620, 240)
    #inventory = Inventory()
    
    #for item in test_books:
    #    inventory.add_book(item.get_isbn, item)

    #inventory.print_inventory()
    #inventory.add_book("817525766-0", Book("Title1", "Daudi", "817525766-0", 1998, "Novel", 29.99))
    #inventory.remove_book("817525766-0")
    #query = inventory.find("genre".lower(), "Classic")



if __name__ == "__main__":
    main()
