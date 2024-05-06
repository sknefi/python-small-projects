# SPRÁVA KNIŽNICE

from abc import ABC, abstractmethod
import json


class ItemNotAvailableError(Exception):
    pass


class ItemNotFoundError(Exception):
    pass


class ItemNotCheckedOutError(Exception):
    pass


class Item(ABC):
    def __init__(self, title):
        self.title = title
        self._checked_out = False

    @property
    def is_checked_out(self) -> bool: return self._checked_out

    def checkout(self): self._checked_out = True

    def return_item(self): self._checked_out = False

    @abstractmethod
    def __str__(self): pass


class Book(Item):
    def __init__(self, title, author, isbn):
        super().__init__(title)
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class Magazine(Item):
    def __init__(self, title, volume, issue_number):
        super().__init__(title)
        self.volume = volume
        self.issue_number = issue_number

    def __str__(self):
        return f"Magazine: {self.title}, Volume {self.volume}, Issue {self.issue_number}"


class Library:
    def __init__(self):
        self.items = []

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < len(self.items):
            current_item = self.items[self.current_index]
            self.current_index += 1
            return current_item
        else:
            raise StopIteration

    def add_item(self, item):
        self.items.append(item)

    def get_books(self):
        return [item for item in self.items if isinstance(item, Book)]

    def get_magazines(self):
        return [item for item in self.items if isinstance(item, Magazine)]

    def checkout_item(self, title: str):
        for item in self.items:
            if item.title == title:
                if not item.checkout():
                    item.checkout()
                    return
                else:
                    raise ItemNotAvailableError(f"{title} is already checked out.")

        raise ItemNotFoundError(f"{title} not found in the library.")

    def return_item(self, title: str):
        for item in self.items:
            if item.title == title:
                if item.is_checked_out:
                    item.return_item()
                    return
                else:
                    raise ItemNotCheckedOutError(f"{title} is not checked out.")

        raise ItemNotFoundError(f"{title} not found in the library.")

    def load_from_file(self, filename: str):
        with open(filename, 'r') as file:
            data = json.load(file)
            for book_data in data['books']:
                book = Book(title=book_data['title'], author=book_data['author'], isbn=book_data['isbn'])
                self.add_item(book)

            for magazine_data in data['magazines']:
                magazine = Magazine(title=magazine_data['title'], volume=magazine_data['volume'],
                                    issue_number=magazine_data['issue_number'])
                self.add_item(magazine)