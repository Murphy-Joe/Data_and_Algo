
## This is Not a Screen Shot - You Need to D/L the txt file and copy it into Programiz :)

## Assn 2 Custom Array Class - Joe Murphy

class Book:
    def __init__(self, name):
        self.name = name 

    def getName(self):
        return self.name


class Bookshelf:
    # class attribute
    shelf = [] #of books

    # constructor
    def __init__(self, firstBook):
        self.shelf = [firstBook]

    def print(self):
        for book in self.shelf:
            print(book.getName())

    def insert(self, book, position):
        if len(self.shelf) == 0 and position == 0:
            self.shelf = [book]
            return
        if position < 0 or position > len(self.shelf):
            return

        new_list_size = len(self.shelf) + 1
        newBookshelf = new_list_size*[None]
        
        for i in range(len(newBookshelf)):
            if i < position:
                newBookshelf[i] = self.shelf[i]
            elif i > position: 
                newBookshelf[i] = self.shelf[i-1]
            else:
                newBookshelf[i]= book

        self.shelf = newBookshelf
    
    def remove_book(self, name_of_book):
        if len(self.shelf) == 0:
            return

        new_list_size = len(self.shelf) - 1
        newBookshelf = new_list_size*[None]

        for i in range(new_list_size):
            book_name = self.shelf[i].getName()
            if name_of_book != book_name:
                newBookshelf[i] = self.shelf[i]
            else:
                stopped_at = i
                for ix in range(len(newBookshelf[stopped_at:])):
                    pickup_index = stopped_at + ix
                    newBookshelf[pickup_index] = self.shelf[pickup_index+1]
                break

        self.shelf = newBookshelf

    def remove_position(self, index_to_remove):
        if len(self.shelf) == 0:
            return
        if index_to_remove < 0 or index_to_remove > len(self.shelf):
            return 

        new_list_size = len(self.shelf) - 1
        newBookshelf = new_list_size*[None]
        
        for i in range(new_list_size):
            if i < index_to_remove:
                newBookshelf[i] = self.shelf[i]
            if i >= index_to_remove:
                newBookshelf[i] = self.shelf[i+1]

        self.shelf = newBookshelf


## This is Not a Screen Shot - You Need to D/L the txt file and copy it into Programiz :)

def run_demo_prints():
    print("\nIn Order:")
    shelf1 = Bookshelf(Book("Book One"))
    shelf1.insert(Book("Book Two"), 1)
    shelf1.insert(Book("Book Three"), 2)
    shelf1.print()

    print("\nReverse Order:")
    shelf2 = Bookshelf(Book("Book One"))
    shelf2.insert(Book("Book Two"), 0)
    shelf2.insert(Book("Book Three"), 0)
    shelf2.print()

    print("\nMixed Order:")
    shelf3 = Bookshelf(Book("Book One"))
    shelf3.insert(Book("Book Two"), 0)
    shelf3.insert(Book("Book Three"), 1)
    shelf3.print()

def run_created_defs():
    print("\n\tShelf to Manipulate")
    shelf4 = Bookshelf(Book("Book One"))
    shelf4.insert(Book("Book Two"), 1)
    shelf4.insert(Book("Book Three"), 2)
    shelf4.insert(Book("Book Four"), 3)
    shelf4.insert(Book("Book Five"), 4)
    shelf4.print()


    print("\n\tRemove Book Two, Manually")
    shelf4.remove_book("Book Two")
    shelf4.print()


    print("\n\tRemove Position Zero, Manually")
    shelf4.remove_position(0)
    shelf4.print()



## This is Not a Screen Shot - You Need to D/L the txt file and copy it into Programiz :)
print("\n########################################\n   Demo from Java converted to Python\n########################################")
run_demo_prints()
print("\n########################################\n\tAdditional Array Functions\n########################################")
run_created_defs()



