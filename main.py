from book import Book

if __name__ == '__main__':
    print('Hello')

n = int(input("How many book objects do you want to create?"))
books = []


for i in range(n):
    parametrized_const = input(f"Do you want to use parametrized constructor for your book #{i+1} (yes/no)? ")
    if parametrized_const == 'yes':
        title = input("Enter the title of your book: ")
        author_name = input("What is the name of the author of the book? ")
        author_surname = input("What is the surname of the author? ")
        genre = input("Enter the genre of your book: ")
        year = int(input("Which year was the book published? "))
        book = Book(title, author_name, author_surname, genre, year)
    else:
        book = Book()

    books.append(book)

for i in range(len(books)):
    books[i].display_info()