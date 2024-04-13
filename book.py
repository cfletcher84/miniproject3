class Book():

    def __init__(self, title, author, isbn, genre, publication_date):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.is_available = True


    def check_out(self):
        if self.is_available:
            print(f"You succesfully checked out {self.title}")
            self.is_available = False
            return True
        print(f"{self.title} is not available")
        return False

    def return_book(self):
        self.is_available = True

