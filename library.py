from book import Book
from user import User
from author import Author

class Library():
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    def add_book(self):
        title = input('What is the title of the book you would like to add? : ')
        author = input(f'Who is the author for {title}? : ')
        isbn = input(f'What is the ISBN for {title}? : ')
        genre = input(f'What is the genre for {title}? : ')
        publication_date = input(f'What is the publication for {title}? : ')
        new_book = Book(title, author, isbn, genre, publication_date)
        self.books.append(new_book)
        print(f'{new_book.title} has been added.')
    
    def borrow_book(self, title):
        book = self.search_book(title)
        if not self.users:
            print('There are no users in the library.')
        if book:
            user = input(f'Who is the user who is checking out {title}? : ')
            no_user = True
            for i in self.users:
                if user == i.get_name():
                    no_user = False
                    i.borrowed_books.append(book)
                    # print(f'These are your borrowed books: {i.borrowed_books}')
                    self.books.remove(book)
                    print(f'These are the books left in lobrary {self.books}')
                    print(f'{title} has been checked out by {i.get_name()}.')
                else:
                    print(f'Sorry {i.get_name()} is not a library user.')
        else:
            print(f'The {title} is not available to check out.')


    def search_book(self, title):
        for i in self.books:
            if i.title == title:
                print(f'Here is the book you searched for:\nTitle: {i.title}\nAuthor: {i.author}\nISBN: {i.isbn}\nGenre: {i.genre}\nPublicaton Date: {i.publication_date}')
                return i
            else:
                print(f'The book {title} does not exist in the library.')

    def return_book(self, title):

        user = input(f'Who is the user returning the {title}? : ')
        no_user = True
        for i in self.users:
            if user == i.get_name():
                no_user = False
                for book in i.borrowed_books:
                    if book.title == title:
                        i.return_book(book)
                        self.books.append(book)
                        print(f'The book {book.title} was returned by user {i.get_name()}!')
            if no_user:
                print(f'Sorry {i.name} is not a library member.')
            else:
                print(f'The book {title} does not exist in the library.')

    def display_all(self):
        print('\nHere is a list of all the books in the library!')
        for i in self.books:
            print(f'\nTitle: {i.title}')
            print(f'Author: {i.author}')
            print(f'ISBN: {i.isbn}')
            print(f'Genre: {i.genre}')
            print(f'Publication Date: {i.publication_date}')
            print(f'Available: {i.is_available}\n')

    def add_user(self):
        name = input('\nWhat is the new users name? : ')
        library_id = input('\nWhat is the new users ID number? : ')
        new_user = User(name, library_id)
        self.users.append(new_user)
        print(f'{new_user.get_name()} has been added to the users list.')

    
    def user_details(self):
        if not self.users:
            print('There are no users in the list!')
        else:
            print('\nHere are the users in the list!')
            for i in self.users:
                print(f'Name: {i.get_name()}, ID# {i.get_library_id()} borrowed the following books:')
                for book in i.borrowed_books:
                    print(f'{book.title}')

    def all_users(self):
        if not self.users:
            print('Sorry there are no users in the list!')
        else:
            print('Here are the users in the list!')
            for i in self.users:
                print(f'{i.get_name()} has an ID of {i.get_library_id()}')

    def add_author(self):
        name = input('\nWhat is the authors name? : ')
        biography = input('\nWhat is the authors biography? : ')
        new_author = Author(name, biography)
        self.authors.append(new_author)
        print(f'{new_author.get_name()} has been added to the authors list.')

    def author_details(self):
        if not self.authors:
            print('There are no authors in the list!')
        else:
            print('\nHere are the authors in the list!')
            for i in self.authors:
                print(f'Name: {i.name}: Biography: {i.biography}')

    def display_authors(self):
        if not self.authors:
            print('There are no authors in the list!')
        else:
            print('\nHere are the authors in the list!')
            for i in self.authors:
                print(f'Name: {i.name}')

    
