class Library:
    def __init__(self,listofBooks):
        self.books=listofBooks                  #Storing all books in self.books variable
        
    def ListofavailableBooks(self):
        print("Number of books available are:")
        for book in self.books:
            print("*"+book)


    def issueBook(self,bookname):
        if bookname in self.books:
            print(f"you have been issued {bookname}.Plz keep it safe n clean !")
            self.books.remove(bookname)
        else:
            print("this book is not available")

    def returnBook(self,bookname):
            print(f"Thanks for returning {bookname}")
            self.books.append(bookname)

class Student():
    def rqstbook(self):
        self.book=input("Enter a book u wanna a request: ")
        return self.book
    def returnBook(self):
        self.book=input("Enter a book u wanna a return: ")
        return self.book



if __name__=="__main__":
    l = Library(["Database", "Server", "DotNet", "Python"])
    s = Student()
    while(True):

        print('''*******LMS Menu*******\n
              1.Display\n
              2.Request\n
              3.Return\n
              4.Exit''')


        choice=int(input("Please Enter your choice(1-4)\n"))
        if choice == 1:
            l.ListofavailableBooks()

        elif choice==2:

            l.issueBook(s.rqstbook())
        elif choice==3:

            l.returnBook(s.returnBook())
        elif choice==4:
            print("Thanks for using Library Management System !")
            exit()

        else:
            print("Invalid Choice")



