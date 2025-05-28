#№3#
class Book:
    def __init__(self, title, author, year=2024):
        if self.validate(year):
            self.__title = title
            self.__author = author
            self.__year = year
    
    @staticmethod
    def validate(year):
        if not isinstance(year, int):
            raise ValueError("Ошибка, год должен быть числом")
        elif year > 2024:
            raise ValueError("Некорректный год издания")
        else:
            return True
    
    def get_info(self):
        return f"{self.__title}, автор: {self.__author}, год: {self.__year}"
    
    @classmethod
    def create_default_year(cls, title, author):
        return cls(title, author)


book1 = Book("1984", "George Orwell", 1949)
print(book1.get_info()) 

book2 = Book.create_default_year("Brave New World", "Aldous Huxley")
print(book2.get_info()) 