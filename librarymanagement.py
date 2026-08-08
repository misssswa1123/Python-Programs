class library:
    def __init__(self,no_of_books,books):
        self.no_of_books=no_of_books
        self.books=books
    def printno_of_books(self):
        print("No of books=",self.no_of_books)
        j=1
        for i in self.books:
            print(f"Book {j}={i}")
            j+=1
        self.books.clear()
        print("library is empty=",self.books)

books=['ABC','XYZ','PQR','STU']
no_of_books=len(books)
l=library(no_of_books,books)
l.printno_of_books()

    

