class Book:
    # Default and parametrized constructor
    def __init__(self, title=None, author_name=None, author_surname=None, genre=None, year=None):
        self.title = title
        self.author_name = author_name
        self.author_surname = author_surname
        self.genre = genre
        self.year = year

    # Methods
    def display_info(self):
        print(
            f'The book named "{self.title}" is written by {self.author_name} {self.author_surname}. The genre of the '
            f'book is {self.genre}. It was published in {self.year}.')

    def is_author(self):
        print(f'The author of "{self.title}" is {self.author_name} {self.author_surname}.')

    def published(self):
        print(f"The book was published in {self.year}.")