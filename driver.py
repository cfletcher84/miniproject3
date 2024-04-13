from library import Library
library = Library()

def main_menu():

    while True:

        print("""

Welcome to the Library Management System!

Main Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Quit

""")
        user_input = input("\nWhich option would you like to choose? 1-4 : ")
        if user_input == '1':
            book_menu()
        elif user_input == '2':
            user_menu()
        elif user_input == '3':
            author_menu()
        elif user_input == '4':
            return
        else:
            print('Invalid input...please try again!')
            


def book_menu():
        
    while True:

        print("""
Welcome to the books section!
    
Book Menu:
    
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books 
6. Main menu
              
""")
        user_input = input('\nWhat would you like to do today? : ')
        if user_input == '1':
            library.add_book()
        elif user_input == '2':
            library.borrow_book(input('\nWhat book would you like to borrow? : '))
        elif user_input == '3':
            library.return_book(input('\nWhat book would you like to return? : '))
        elif user_input == '4':
            library.search_book(input('\nWhat book would you like to search for? : '))
        elif user_input == '5':
            library.display_all()
        elif user_input == '6':
            return
            
def user_menu():

    while True:   

        print("""
Welcome to the user operations!
    
User Operations:
    
1. Add a new user
2. View user details
3. Display all users
4. Main menu
              
""")
        user_input = input('\nPlease choose an option (1-4): ')
        if user_input == '1':
            library.add_user()
        elif user_input == '2':
            library.user_details()
        elif user_input == '3':
            library.all_users()
        elif user_input == '4':
            return
                
def author_menu():

    while True:
        
        print("""
              
Welcome to the Authors section!
    
Author Operations:
1. Add a new author
2. View author details
3. Display all authors
4. Main menu
              
""")
        user_input = input('\nPlease choose an option (1-4): ')
        if user_input == '1':
            library.add_author()
        elif user_input == '2':
            library.author_details()
        elif user_input == '3':
            library.display_authors()
        elif user_input == '4':
            return


main_menu()