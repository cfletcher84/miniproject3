# **Library Management System**

*The Library Management System is designed to allows users to browse, borrow, return, and explore a collection of books.*   
*This system houses a database that contains a list of books, a list of users, and a list of authors.*

## User interaction

**Menu Preview (Command-Line):**  
*Users start by choosing the function they wish to use, by entering the number associated with the option.*
```   
        Welcome to the Library Management System!

        Main Menu:
        1. Book Operations
        2. User Operations
        3. Author Operations
        4. Quit
```
<br />
<br />

**1. User Operations:** *This is where new users can be added along with their necessary details. Users need to be entered first before moving forward with the other Operations:*
```
    Welcome to the user operations!
    
    User Operations:
    1. Add a new user
    2. View user details
    3. Display all users
    4. Main menu
```
Once the user chooses an option they can enter or view details depending on which number they select. Example below:
```
    User Operations:
    1. Add a new user
        What is the new users name?: John Doe
        What is the new users ID number?: 123
    2. View user details
        Here are the user details!
        Name: John Doe, ID # 123 borrowed the following books:
        Name: Jane Doe, ID # 456 borrowed the following books:
    3. Display all users
        Here are the users in the list!
        John Doe has an ID of 123
        Jane Doe has an ID of 456
    4. Main menu
        Takes the user back to main menu
```
<br />
<br />

**2. Book Operations:** *Opens the Book Operations menu where users pick which option they would like to choose. Example below:*

```
    Welcome to the books section!
    
    Book Menu:
    1. Add a new book 
    2. Borrow a book
    3. Return a book
    4. Search for a book
    5. Display all books 
    6. Main menu         
```
Each choice collects and displays different details pertaining to the book menu, as seen below: 

```
    Book Menu:
    1. Add a new book
        What is the title of the book you would like to add?: "To Kill a Mockingbird"
        Who is the author for '"To Kill a Mockingbird"'?: Harper Lee
        What is the ISBN for '"To Kill a Mockingbird"'?: 1234
        What is the genre for '"To Kill a Mockingbird"'?: Fiction
        What is the publication date for '"To Kill a Mockingbird"'?: 08/11/1960

        You have added 'To Kill a Mockingbird' to the Library!
    2. Borrow a book
        What book would you like to borrow?: To Kill a Mockingbird
                Here is the book you searched for:
                Title: To Kill a Mockingbird
                Author: Harper Lee
                ISBN: 1234
                Genre: Fiction
                Publication Date: 08/11/1960
        Who is the user who is checking out To Kill a Mockingbird?: John Doe
                To Kill a Mockingbird has been checked out by John Doe.
                To Kill a Mockingbird is not available to check out.
    3. Return a book
        What book would you like to return?: To Kill a Mockingbird
        Who is the user returning To Kill a Mockingbird?: John Doe

        The book To Kill a Mockingbird was returned by user John Doe!
    4. Search for a book
        What book would you like to search for?: Twilight
                Here is the book you searched for:
                Title: Twilight
                Author: Stephenie Meyer
                ISBN: 4567
                Genre: Fantasy
                Publication Date: 10/05/2005
    5. Display all books
        Here is a list of all the books in the library
        Title: Twilight
        Author: Stephenie Meyer
        ISBN: 4567
        Genre: Fantasy
        Publication Date: 10/05/2005
        Available: True

        Title: To Kill a Mockingbird
        Author: Harper Lee
        ISBN: 1234
        Genre: Fiction
        Publication Date: 08/11/1960
        Available: True
    6. Main menu
        Takes the user back to the main menu 
```
<br />
<br />

**3. Author Operations:** *Is where new authors along with their information can be entered:* 
```
    Welcome to the Authors section!

    Author Operations:
    1. Add a new author
    2. View author details
    3. Display all authors
    4. Main menu
```
Just like the previous operations each option has it's own features which are displayed below:
```
    Welcome to the Authors section!

    Author Operations:
    1. Add a new author
        What is the authors name?: Stephen King
        Please enter the authors biography: Stephen King (born September 21, 1947, Portland, Maine, U.S.) is an American
        novelist and short-story writer whose books are credited with reviving the genre of horror fiction in the late 20th
        century.

        Stephen King has been added to the authors list.
    2. View author details
        Here are the authors in the list!
        Name: Stephen King, Biograpy: Stephen King (born September 21, 1947, Portland, Maine, U.S.) is an American novelist
        and short-story writer whose books are credited with reviving the genre of horror fiction in the late 20th century.

        Name: J. K. Rowling, Biograpy: J.K. Rowling (born July 31, 1965, Yate, near Bristol, England) British author,
        creator of the popular and critically acclaimed Harry Potter series, about a young sorcerer in training.
    3. Display all authors
        Here are the authors in the list!
        Stephen King
        J. K. Rowling
    4. Main menu
        Takes the user back to the main menu
```
<br />
<br />

## Invalid Input

**Error Messages:** *If a user attempts to input or execute something that is not within the application's capabilities or requirements, the application would generate an error message for the user, as seen below:*
```
'Invalid input...please try again ┌( ಠ_ಠ)┘!'
```
**Possible Causes:** *The error message shown above could occur due to various reasons, such as choosing a non existent option, entering an invalid option, or encountering a technical glitch.*

**Resolution:** *To resolve the issue, the user would need to review their input, ensure that it meets the application's capabilities, and correct any mistakes they may have inputted.*

## Authors

**This application was a group effort created by:**     

*Chris Fletcher* https://github.com/cfletcher84

*Savannah Lyles* https://github.com/Savvy325
