class book:
    def __init__(self,title,author) -> None:
            self.author =author
            self.title = title


class library:
    def __init__(self) -> None:
         self.books = []

    def add_books(self,title,author):
        self.books.append(book(title,author))

    def remove_book(self,title):
         for book in self.books:
              if book.title == title:
                   self.books.remove(book)

    def search_book(self,title):
        for book in self.books:
             if book.title == title:
                print(f"name: {book.title}, author: {book.author}")
                break

    def show_books(self):
         for i,book in enumerate(self.books):
            print(f"book {i}: {book.title} by {book.author}")


def main():

    '''            print("welcom to amirreza library management, what would you like to do?")
                user = int(input(
                    """1. add a book
                    2. remove a book
                    3. search for a book
                    4.show all the books in the library"""))'''

    

if __name__ == "__main__":
    main()
