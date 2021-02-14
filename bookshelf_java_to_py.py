
class Book:
    def __init__(self, name):
        self.name = name 

    def getName(self):
        return self.name



class Bookshelf:
    #class attribute
    shelf = [] #of books

    # instance constructor
    def __init__(self, firstBook):
        self.shelf = [firstBook]

    def print(self):
        for book in self.shelf:
            print(book.getName())

    def insert(self, book, position):
        # this shouldn't happen since shelves start with a book, but it could have been deleted
        if len(self.shelf) == 0 and position == 0:
            self.shelf = [book]
            return

        # must insert book in a valid list position
        if position < 0 or position > len(self.shelf):
            return

        newBookshelf = (len(self.shelf) + 1) * [None]

        for i in range(len(newBookshelf)):
            if i < position:
                newBookshelf[i] = self.shelf[i]
            elif i > position: 
                newBookshelf[i] = self.shelf[i-1]
            else:
                newBookshelf[i]= book

        self.shelf = newBookshelf


print("\nIn Order:")
shelf1 = Bookshelf(Book("Book One"))
shelf1.insert(Book("Book Two"), 1)
shelf1.insert(Book("Book Three"), 2)
shelf1.insert(Book("Book Four"), 3)
shelf1.insert(Book("Book Five"), 4)
shelf1.print()

print("\nReverse Order:")
shelf2 = Bookshelf(Book("Book One"))
shelf2.insert(Book("Book Two"), 0)
shelf2.insert(Book("Book Three"), 0)
shelf2.insert(Book("Book Four"), 0)
shelf2.insert(Book("Book Five"), 0)
shelf2.print()

print("\nMixed Order:")
shelf3 = Bookshelf(Book("Book One"))
shelf3.insert(Book("Book Two"), 1)
shelf3.insert(Book("Book Three"), 2)
shelf3.insert(Book("Book Four"), 1)
shelf3.insert(Book("Book Five"), 2)
shelf3.print()
