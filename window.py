import tkinter as tk
from tkinter import ttk
from user import User
from inventory import Inventory
from book import Book

class Window():

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.__root = None
        self.__user = None
        self.__inventory = None
        self.__box = None

        self.start_window()

    def start_window(self):
        self.login_screen()
        self.__root.mainloop()

    def close_window(self):
        print("Shutting down...")
        self.__root.destroy()

    def get_name(self):
        return self.__user

    def login(self, user, passw):
        username = user.get()
        password = passw.get()

        if username == "admin" and password == "root":
            print("Login successful")
            self.__user = User(username)
            self.__root.destroy()
            self.main_menu()
        else:
            print("Login failed")

    def login_screen(self):
        self.__root = tk.Tk()
        self.__root.title("Login")
        self.__root.protocol("WM_DELETE_WINDOW", self.close_window)
        self.__root.bind("<Return>", lambda event=None: button_login.invoke())


        login_frame = ttk.Frame(self.__root)
        label_username = ttk.Label(self.__root, text="Username: ")
        username = ttk.Entry(self.__root)
        label_password = ttk.Label(self.__root, text="Password: ")
        password = ttk.Entry(self.__root, show="*")
        button_login = ttk.Button(self.__root, text="Login", command=lambda: self.login(username, password))

        button_login.pack()
        login_frame.pack()
        label_username.pack()
        username.pack()
        label_password.pack()
        password.pack()


    def main_menu(self):
        self.__root = tk.Tk()
        self.__root.title("Bookstore")
        self.__root.geometry(f"{self.width}x{self.height}")
        self.__root.protocol("WM_DELETE_WINDOW", self.close_window)

        details_t = tk.StringVar()
        details_t.set(f"Title:\nAuthor:\nISBN:\nYear:\nGenre:\nPrice\nCopies left:")

        menu_t = tk.StringVar()
        menu_t.set("Title")

        #Main window frame
        frame = ttk.Frame(self.__root)

        #Frame at top
        top_frame = ttk.Frame(frame)

        #Top left label
        logged = ttk.Label(top_frame, text=f"Logged in as {self.__user.get_username()}")

        #Boot details
        details = ttk.Label(frame, textvariable=details_t)

        #List of books in the bookstore
        self.__box = tk.Listbox(frame)
        self.initialize()
        self.__box.bind("<<ListboxSelect>>", lambda event: self.details(details_t))
        
        #Menubox
        menu_content = ["Title", "Author", "ISBN", "Year", "Genre", "Price", "Quantity"]
        menu = tk.OptionMenu(top_frame, menu_t, *menu_content)

        #Search button for seach queries
        search_button = ttk.Button(top_frame, text="Search books", command=lambda: self.search(menu_t.get(), search_box.get()))
        self.__root.bind("<Return>", lambda event=None: search_button.invoke())

        #Search by different values
        search_box = ttk.Entry(top_frame)

        add_button = ttk.Button(frame, text="Add book", command=self.add_book_to_inventory)
        remove_button = ttk.Button(frame, text="Remove book", command=self.remove)

        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#ccc")

        #Pack all of the GUI objects
        frame.pack(fill=tk.BOTH)
        top_frame.pack(side=tk.TOP, fill=tk.X)
        logged.pack(side=tk.LEFT)
        search_button.pack(side=tk.RIGHT)
        self.__box.pack(side=tk.LEFT)
        search_box.pack(side=tk.RIGHT)
        details.pack(side=tk.LEFT, padx=10, pady=10)
        menu.pack(side=tk.RIGHT)
        add_button.pack(side=tk.BOTTOM)
        remove_button.pack(side=tk.BOTTOM)

    def initialize(self):
        if self.__inventory:
            self.__box.delete(0, tk.END)
        self.__inventory = Inventory()
        for book in self.__inventory.get_inventory():
            self.__box.insert(tk.END, book.get_title())
            
    def details(self, label):
        index = self.__box.curselection()
        if index:
            book = self.__inventory.get_inventory()[index[0]]
            label.set(f"Title: {book.get_title()}\nAuthor: {book.get_author()}\nISBN: {book.get_isbn()}\nYear: {book.get_year()}\nGenre: {book.get_genre()}\nPrice: {book.get_price()}€\nCopies left: {book.get_quantity()}")

    def remove(self):
        index = self.__box.curselection()
        if index:
            book = self.__inventory.get_inventory()[index[0]]
            self.__inventory.remove_book(book.get_isbn())
            self.initialize()
        else:
            print("Failed to remove book")

    def search(self, box_content, value):
        if value:
            values = self.__inventory.search_values(box_content, value)
            if values:
                self.__box.delete(0, tk.END)
                for book in values:
                    self.__box.insert(tk.END, book.get_title())
        else:
            self.__box.delete(0, tk.END)
            for book in self.__inventory.get_inventory():
                self.__box.insert(tk.END, book.get_title())

    def save(self, win, title, author, isbn, year, genre, price):
        if title and author and isbn and year and genre and price:
            book = Book(title, author, isbn, int(year), genre, float(price))
            self.__inventory.add_book(isbn, book)
            print(f"Title: {book.get_title()} saved successfully")
            win.destroy()
            self.initialize()
        else:
            print("Information missing")
            return

    def add_book_to_inventory(self):

        book_window = tk.Toplevel(self.__root)
        book_window.geometry(f"240x270")
        book_window.title("Add book information")

        title_label = ttk.Label(book_window, text="Title:")
        title_entry = ttk.Entry(book_window)

        author_label = ttk.Label(book_window, text="Author:")
        author_entry = ttk.Entry(book_window)

        isbn_label = ttk.Label(book_window, text="ISBN:")
        isbn_entry = ttk.Entry(book_window)

        year_label = ttk.Label(book_window, text="Year:")
        year_entry = ttk.Entry(book_window)

        genre_label = ttk.Label(book_window, text="Genre:")
        genre_entry = ttk.Entry(book_window)

        price_label = ttk.Label(book_window, text="Price:")
        price_entry = ttk.Entry(book_window)

        button = ttk.Button(book_window, text="Save", command=lambda: self.save(book_window, title_entry.get(), author_entry.get(), isbn_entry.get(), year_entry.get(), genre_entry.get(), price_entry.get()))

        title_label.pack()
        title_entry.pack()
        author_label.pack()
        author_entry.pack()
        isbn_label.pack()
        isbn_entry.pack()
        year_label.pack()
        year_entry.pack()
        genre_label.pack()
        genre_entry.pack()
        price_label.pack()
        price_entry.pack()
        button.pack()