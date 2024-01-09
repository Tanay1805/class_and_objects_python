class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Item ID: {self.item_id}")
        print("Checked Out: Yes" if self.checked_out else "Checked Out: No")

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} has been checked in.")
        else:
            print(f"{self.title} is not currently checked out.")


class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id)
        self.genre = genre

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")


class DVD(LibraryItem):
    def __init__(self, title, author, item_id, duration):
        super().__init__(title, author, item_id)
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Duration: {self.duration} minutes")


class Journal(LibraryItem):
    def __init__(self, title, author, item_id, publication_year):
        super().__init__(title, author, item_id)
        self.publication_year = publication_year

    def display_info(self):
        super().display_info()
        print(f"Publication Year: {self.publication_year}")


# Example usage of the classes
if __name__ == "__main__":
    # Create instances of different library items
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "B001", "Classic")
    dvd1 = DVD("Inception", "Christopher Nolan", "D001", 148)
    journal1 = Journal("Nature", "Various Authors", "J001", 2022)

    # Display information about library items
    print("Information about Library Items:")
    print("-------------------------------")
    book1.display_info()
    print("\n")
    dvd1.display_info()
    print("\n")
    journal1.display_info()

    # Check out and check in library items
    print("\n\nChecking Out and Checking In:")
    print("-------------------------------")
    book1.check_out()
    dvd1.check_out()
    journal1.check_out()

    print("\n")

    book1.check_in()
    dvd1.check_in()
    journal1.check_in()
