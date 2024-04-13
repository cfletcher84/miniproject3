


class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.borrowed_books = []

    def set_library_id(self, new_library_id):
        self.__library_id = (new_library_id)
        
    def get_library_id(self):
        return self.__library_id
    
    def get_name(self):
        return self.__name
    
    def borrowed_books(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)

