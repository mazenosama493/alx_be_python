class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.__is_checked_out=False
    def get_state(self):
        return self.__is_checked_out
    def set_state(self,state):
        self.__is_checked_out=state
class Library :
    def __init__(self):
        self.__books=[]
    def add_book(self,title,author):
        book=Book(title,author)
        self.__books.append(book)
        
    def list_available_books(self):
        for book in self.__books:
            if book.get_state()==False:
                print(f"{book.title} by {book.author}")
    def check_out_book(self,title):
        for book in self.__books:
            if book.title==title :
                book.set_state(True)
            else:
                book.set_state(False)
        else:
            return "we don't have this book"
    def return_book(self,title):
        for book in self.__books:
            if book.title == title:
                book.set_state(False)


        



