from typing import List

import strawberry

# Create and activate a venv.
# step 1. pip install requirements.txt
# step 2. strawberry server schema.schema -> this loads up our server, open the webpage
# step 3. Add some documentation to the book type
# step 4. refresh your your web page -> check the documetnation is added to the book type
# step 5. Let's create a mutation to add a book to the database.
# Step 6. Let's add a query to get all books from the database.
from dataclasses_json import dataclass_json

from schema.database import Database

print("Opening database")
db = Database()

@dataclass_json
@strawberry.type(description="")
class Book:
    title: str # This is the title of the book hooray
    author: str

# This isnt returning anything from our database this is a rubbish single item
example_book = Book(
            title='The Great Gatsby',
            author='F. Scott Fitzgerald',
        )


def get_books() -> List[Book]:
    # 1. Lets actually get our books from the database here
    # book_list = []
    # for book in db.get_all_books():
    #     book = Book.from_dict(book)
    #     book_list.append(book)
    #
    # return book_list

    # 2. We shouldn't actually return junk. Get rid of this
    return [example_book]


def get_book_by_title(book_title: str = "F. Scott Fitzgerald") -> Book:
    return get_books()[0]


@strawberry.type(description="This is the root level query description")
class Query:
    books: List[Book] = strawberry.field(resolver=get_books, description="")
    #get_book_by_title: Book = strawberry.field(resolver=get_book_by_title)


@strawberry.type
class Mutation:

    @strawberry.field
    def add_book(self, title: str, author: float) -> Book:

        added_book = Book(title=title, author=author)
        print(type(author))

        # 1. Let's check if our inputs are valid GIGO you put junk in you'll get junk out....
        # validation = Book.schema().validate(added_book.to_dict())
        # print(validation)
        # if validation != {}:
        #     raise Exception(f"Invalid book {validation }")

        # 2. Let's actually add a book to the database here
        # db.store_book(added_book.to_dict())
        # print("stored a book")

        # 3. Returning a book for adding a book is a little weird lets return a bool or something a bit saner / an id
        return added_book


#This is all you have to do to turn the above into a graphql interface
schema = strawberry.Schema(query=Query, mutation=Mutation)
