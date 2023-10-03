import json

class Book():

    def __init__(self, title, author, isbn, year, genre, price) -> None:
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__year = year
        self.__genre = genre
        self.__price = price
        self.__quantity = 0


    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author 
    
    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, value):
        self.__isbn = value

    def get_year(self):
        return self.__year
    
    def set_year(self, value):
        self.__year = value

    def get_genre(self):
        return self.__genre
    
    def set_genre(self, value):
        self.__genre = value
    
    def get_price(self):
        return self.__price
    
    def set_price(self, value):
        self.__price = value

    def get_quantity(self):
        return self.__quantity

    def increase_quantity(self, value):
        self.__quantity += value

    def get_data(self):
        #Data for comparison
        data = {"Title" : self.__title,
                "Author": self.__author,
                "ISBN" : self.__isbn,
                "Year" : self.__year,
                "Genre" : self.__genre,
                "Price" : self.__price,
                "Quantity" : self.__quantity}
        
        return data

    def save(self):
        file = []
        data = self.get_data()
        try:
            with open("books.json", "r") as books:
                file = json.load(books)
        except Exception as e:
            pass

        #Converts data and file into JSON strings for comparison
        json_data = json.dumps(data, sort_keys=True)
        json_file = [json.dumps(item, sort_keys=True) for item in file]

        #If new book isn't duplicate add it to the file
        if json_data not in json_file:
            file.append(data)

        with open("books.json", "w") as books:
            json.dump(file, books, indent = 4)
    
    def __str__(self):
        return f"\nTitle: {self.__title}\nAuthor: {self.__author}\nIsbn: {self.__isbn}\nYear: {self.__year}\nGenre: {self.__genre}\nPrice: {self.__price}€\nQuantity: {self.__quantity}\n"