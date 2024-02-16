import time
class Library():

    def __init__(self):
        with open("books.txt", "a+" , encoding="UTF-8") as file:
            self.file = file

    def __del__(self):
        self.file.close()

    def ListBook(self):
        with open("books.txt", "r", encoding="UTF-8") as file:
            lines = file.readlines()
            for i in lines:
                # With *_, values after title and author are ignored.
                title, author, *_ = i.strip().split(',')
                print(f"Book: {title}, Author: {author}")

    def AddBook(self):
        title = input("Please write the title:").capitalize()
        author = input("Please write the author:").capitalize()
        bookPage = input("Please write the book page number:")
        datePublication = input("Please write the date of publication:")
        with open("books.txt", "a+" , encoding="UTF-8") as file:
            file.write(f"{title},{author},{bookPage},{datePublication}\n")
        time.sleep(2)
        print("Book added successfully.")  

    def RemoveBook(self):
        book_to_delete = input("Enter the title of the book to remove:").capitalize()
        check = False
        with open("books.txt", "r", encoding="UTF-8") as file:
            lines = file.readlines()
        with open("books.txt", "w", encoding="UTF-8") as file:
            for line in lines:
                #Skips values after the book title.
                title, _, _, _ = line.strip().split(',')
                if (title != book_to_delete):
                    file.write(line)
                else:
                    check = True
        if (check == True):
            time.sleep(2)
            print(f"{book_to_delete} removed successfully.")
        else:
            time.sleep(2)
            print("The library doesn't have this book.")

    def Choices(self):
        while True:
            print("**********Welcome to Menu**********\n1-List Book\n2-Add Book\n3-Remove Book\n4-Quit('q')\n")
            choice = input("Choice:").lower()
            if (choice == 'q'):
                break
            elif (choice == '1'):
                time.sleep(2)
                self.ListBook()
            elif (choice == '2'):
                time.sleep(2)
                self.AddBook()
            elif (choice == '3'):
                time.sleep(2)
                self.RemoveBook()
            else:
                print("Please make the right choice.")
        del self

lib = Library()
lib.Choices()