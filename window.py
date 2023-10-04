import tkinter as tk
from tkinter import ttk
from user import User
from inventory import Inventory

class Window():

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.__root = None
        self.__user = None
        self.__inventory = None

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
        login_frame.pack()

        label_username = ttk.Label(self.__root, text="Username: ")
        label_username.pack()

        username = ttk.Entry(self.__root)
        username.pack()

        label_password = ttk.Label(self.__root, text="Password: ")
        label_password.pack()

        password = ttk.Entry(self.__root, show="*")
        password.pack()

        button_login = ttk.Button(self.__root, text="Login", command=lambda: self.login(username, password))
        button_login.pack()


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
        book_list = tk.Listbox(frame)
        self.initialize(book_list)
        book_list.bind("<<ListboxSelect>>", lambda event: self.details(book_list, details_t))
        
        #Menubox
        menu_content = ["Title", "Author", "ISBN", "Year", "Genre", "Price", "Quantity"]
        menu = tk.OptionMenu(top_frame, menu_t, *menu_content)

        #Search button for seach queries
        search_button = ttk.Button(top_frame, text="Search books", command=lambda: self.search(menu_t.get(), search_box.get(), book_list))
        self.__root.bind("<Return>", lambda event=None: search_button.invoke())


        #Search by different values
        search_box = ttk.Entry(top_frame)

        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#ccc")

        #Pack all of the GUI objects
        frame.pack(fill=tk.BOTH)
        top_frame.pack(side=tk.TOP, fill=tk.X)
        logged.pack(side=tk.LEFT)
        search_button.pack(side=tk.RIGHT)
        book_list.pack(side=tk.LEFT)
        search_box.pack(side=tk.RIGHT)
        details.pack(side=tk.LEFT, padx=10, pady=10)
        menu.pack(side=tk.RIGHT)

        
        pass
    def initialize(self, box):
        self.__inventory = Inventory()
        for book in self.__inventory.get_inventory():
            box.insert(tk.END, book.get_title())
            
    def details(self, books, label):
        index = books.curselection()
        if index:
            book = self.__inventory.get_inventory()[index[0]]
            label.set(f"Title: {book.get_title()}\nAuthor: {book.get_author()}\nISBN: {book.get_isbn()}\nYear: {book.get_year()}\nGenre: {book.get_genre()}\nPrice: {book.get_price()}€\nCopies left: {book.get_quantity()}")

    def search(self, box_content, value, box):
        if value:
            values = self.__inventory.search_values(box_content, value)
            if values:
                box.delete(0, tk.END)
                for book in values:
                    box.insert(tk.END, book.get_title())
        else:
            box.delete(0, tk.END)
            for book in self.__inventory.get_inventory():
                box.insert(tk.END, book.get_title())

    def add_to_cart(self):
        pass

    def process_order(self):
        pass

