class Library:
    def __init__(self,list_of_books,name):
        self.name=name
        self.Bookslist=list_of_books
        self.lendict={}

        def displayBooks(self):
            print(f"We have following books in our Library:{self.name}")
            
            for book in self.bookslist:
                print(book)

        def lendbook(self,user,book):
            if book not in self.bookslist:
                print("sorry we donot have that book")
            elif book in self.lendict:
                print("The book is already being used by {self.lendict[book]}")
            else :
                self.lendict[book]=user
                print("Lender-Book database has been updated. You can take the book now")


        def addbook(self,book):
            self.bookslist.append(book)
            print(f"the {book} has been added to the book list")
        def returnBook(self,book):
            if book in self.lendict:
                del self.lendict[book]
                print("Book has been returned")
            else:
                print("the book was not lend from us")
            
            

    



       