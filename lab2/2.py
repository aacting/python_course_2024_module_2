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
    """
    Класс, представляющий книгу.

    Атрибуты:
        id_ (int): Уникальный идентификатор книги.
        name (str): Название книги.
        pages (int): Количество страниц в книге.

    Исключения:
        TypeError: Если id_ не является целым числом, name не является строкой, или pages не является целым числом.
        ValueError: Если id_ меньше 0 или pages меньше 0.
    """

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
    """
    Класс, представляющий библиотеку, содержащую книги.

    Атрибуты:
        books (list[Book]): Список книг в библиотеке.

    Методы:
        get_next_book_id(id_: int) -> int: Возвращает следующий доступный идентификатор для новой книги.
        get_index_by_book_id(id_: int) -> int: Возвращает индекс книги в библиотеке по её идентификатору.
    """

    def __init__(self, books: list[Book] = None):
        """
        Инициализирует библиотеку с заданным списком книг.

        Параметры:
            books (list[Book], optional): Список книг для инициализации библиотеки. По умолчанию пустой список.
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self, id_: int) -> int:
        """
        Возвращает следующий доступный идентификатор для новой книги.

        Параметры:
            id_ (int): Идентификатор, который будет использоваться для проверки.

        Возвращает:
            int: Следующий доступный идентификатор книги.
        """
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].id_ + 1

    @staticmethod
    def get_index_by_book_id(id_: int):
        """
        Возвращает индекс книги в библиотеке по её идентификатору.

        Параметры:
            id_ (int): Идентификатор книги.

        Возвращает:
            int: Индекс книги в библиотеке.

        Исключения:
            ValueError: Если книга с запрашиваемым id_ не существует.
        """
        for identifier, books in enumerate(BOOKS_DATABASE):
            if 'id_' in books and books['id_'] == id_:
                return identifier
        raise ValueError("Книги с запрашиваемым id_ не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id(0))  # проверяем следующий id_ для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id_"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id(1))  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
