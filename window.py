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

        #Main window frame
        frame = ttk.Frame(self.__root)

        #Frame at top
        top_frame = ttk.Frame(frame)

        #Top left label
        logged = ttk.Label(top_frame, text=f"Logged in as {self.__user.get_username()}")

        #Search button for seach queries
        search_button = ttk.Button(top_frame, text="Search books", command=self.search)

        #List of books in the bookstore
        book_list = tk.Listbox(frame)
        book_list.bind("<<ListboxSelect>>", self.details)
        self.initialize(book_list)
        
        #Search by different values
        search_box = ttk.Entry(top_frame)

        #Boot details
        details = tk.Text(self.__root, wrap=tk.WORD, height=10, width=40)
        details.pack(side=tk.RIGHT, padx=10, pady=10)

        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#ccc")

        #Pack all of the GUI objects
        frame.pack(fill=tk.BOTH)
        top_frame.pack(side=tk.TOP, fill=tk.X)
        logged.pack(side=tk.LEFT)
        search_button.pack(side=tk.RIGHT)
        book_list.pack(side=tk.LEFT)
        search_box.pack(side=tk.RIGHT)

        def details(self):
            index = book_list.curselection()

            if index:
                index = index[0]

        
        pass
    def initialize(self, box):
        self.__inventory = Inventory()
        for book in self.__inventory.get_inventory():
            box.insert(tk.END, book.get_title())
            

    def search(self):
        pass

    def add_to_cart(self):
        pass

    def process_order(self):
        pass

