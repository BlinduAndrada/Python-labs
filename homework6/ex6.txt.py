class LibraryItem:
    def __init__(self, borrow_date, return_check):
        self.borrow_date = borrow_date
        self.return_check = return_check

    def was_returned(self):
        if self.return_check != 0:
            return ". The item was returned. "
        else:
            return ". The item was not returned yet. "


class Book(LibraryItem):
    def __init__(self, borrow_date, return_check, name, info):
        LibraryItem.__init__(self, borrow_date, return_check)
        self.info = info
        self.name = name

    def __str__(self):
        return "Name of the book : " + str(self.name) + " : " + "Info : " + str(
            self.info) + ". The book was borrowed at the date : " + str(self.borrow_date) + str(self.was_returned())


class DVD(LibraryItem):
    def __init__(self, borrow_date, return_check, name, info):
        LibraryItem.__init__(self, borrow_date, return_check)
        self.info = info
        self.name = name

    def __str__(self):
        return "Name of DVD : " + str(self.name) + " : " + "Info : " + str(
            self.info) + ". The DVD was borrowed at the date : " + str(self.borrow_date) + str(self.was_returned())

class Magazine(LibraryItem):
    def __init__(self, borrow_date, return_check, name, info):
        LibraryItem.__init__(self, borrow_date, return_check)
        self.info = info
        self.name = name

    def __str__(self):
        return "Name of the Magazine : " + str(self.name) + " : " + "Info : " + str(
            self.info) + ". The Magazine was borrowed at the date : " + str(self.borrow_date) + str(self.was_returned())


book1 = Book("11-10-2024", 0, "Twilight", "A book about vampires")
print(book1)

dvd1 = DVD("2-09-2024", 1, "Lady Gaga", "All of her albums")
print(dvd1)

magazine1=Magazine("19-10-2024",0,"TimesNews","All the news around")
print(magazine1)