def greet(fx):
    def greet1(*args, **kwargs):
        print("--------------------------------------------")
        print("Welcome in library management system......")
        fx(*args, **kwargs)
        print("Thanks for using it......")

    return greet1


class Library:
    def __init__(self, book):
        self.__book = book
        self.__book_len = len(self.__book)

    @greet
    def Library_Books(self):
        print(f"Book in library is\t: {self.__book}")
        print(f"Number of books in library is\t: {self.__book_len}")


Input = int(input("How many books you want to add in Library:"))
Start = 0
List = []
while Start < Input:
    Book_Insert = input("Enter name of book that you want to keep:")
    List.append(Book_Insert)
    Start += 1

library = Library(List)
library.Library_Books()
