In my 'book' file I created the Book class which is a template for creating objects.In this case objects will be created by users. Inside the class There are several methods. Firstly, I initialized the
attributes of __init__ methods. Also I created method that displays all the information about the book, mothod that shows who is the author of the book and when the book is published. 

In my main file I created the variable n which defines how many books a user wants to create. Next, I created an empty list 'books' to append there user's books. Firstly, program asks the user how many 
books they want to create and if they want to use parametrized constructor. If the user wants to use parametrized constructor, then my program asks the user to enter title, author name and surnname, 
genre, and the year when his book was publised n times. If their answer was 'no', then attributes are assigned to None. Next, according to the data that user entered, book object is
created and appended to the 'books' list. 

As a result, using for loop, user gets information about each book object they created.
