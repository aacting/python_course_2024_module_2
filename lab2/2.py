BOOKS_DATABASE = [
    {
        "id_": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id_": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError('id_ должно быть типа int')
        if id_ < 0:
            raise ValueError('id_ должно быть больше 0')
        self.id_ = id_
        if not isinstance(name, str):
            raise TypeError('Название книги должно быть типа str')
        self.name = name
        if not isinstance(pages, int):
            raise TypeError('Количество страниц должно быть типа int')
        if pages < 0:
            raise ValueError('Количество страниц должно быть больше 0')
        self.pages = pages


class Library:
    def __init__(self, books: list[Book] = None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self, id_: int) -> int:
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].id_ + 1

    @staticmethod
    def get_index_by_book_id(id_: int):
        for identifier, books in enumerate(BOOKS_DATABASE):
            if 'id_' in books and books['id_'] == id_:
                return identifier
            else:
                return ValueError("Книги с запрашиваемым id_ не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id(0))  # проверяем следующий id_ для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id_"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id(1))  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1