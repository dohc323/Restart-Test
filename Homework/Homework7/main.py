from Inside import Author
from Inside import BookItem
from Inside import BookStore

def main():

    author1 = Author(name = "Stephen King", author_id = "King-Stephen")
    author2 = Author(name = "Tim Pool", author_id = "Pool-Tim")
    author3 = Author(name = "Alex Jones", author_id = "Jones-Alex")

    book_item1 = BookItem(name = "Christine", author = author1, year_published = 1985)
    book_item2 = BookItem(name = "Coffee Bew", author = author2, year_published = 2017)
    book_item3 = BookItem(name = "Info Wars", author = author3, year_published = 2016)
    book_item_storage = [book_item1, book_item2, book_item3]
    book_store1 = BookStore(name = "Steves Library", book_shelve = book_item_storage)

    print(book_store1.__dict__)

if __name__ == "__main__":
    main()