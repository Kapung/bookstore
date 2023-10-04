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
        self.t = self.d = self.i = self.y = self.g = self.p = self.q = ""

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
        
        #Search button for seach queries
        search_button = ttk.Button(top_frame, text="Search books", command=lambda: self.search(book_list, details_t))

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

        
        pass
    def initialize(self, box):
        self.__inventory = Inventory().get_inventory()
        for book in self.__inventory:
            box.insert(tk.END, book.get_title())
            
    def details(self, books):
        pass

    def search(self, books, label):
        index = books.curselection()
        print(index)
        print(index)
        if index:
            book = self.__inventory[index[0]]
            label.set(f"Title: {book.get_title()}\nAuthor: {book.get_author()}\nISBN: {book.get_isbn()}\nYear: {book.get_year()}\nGenre: {book.get_genre()}\nPrice: {book.get_price()}€\nCopies left: {book.get_quantity()}")
            print(self.t)

    def add_to_cart(self):
        pass

    def process_order(self):
        pass

