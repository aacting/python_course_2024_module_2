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
        """
        Инициализирует объект книги с заданными параметрами.

        Параметры:
            id_ (int): Уникальный идентификатор книги.
            name (str): Название книги.
            pages (int): Количество страниц в книге.

        Исключения:
            TypeError: Если id_ не является целым числом, name не является строкой, или pages не является целым числом.
            ValueError: Если id_ меньше 0 или pages меньше 0.
        """
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

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.

        Возвращает:
            str: Строка, представляющая книгу в формате 'Книга "название"'.
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает неформальное строковое представление книги.

        Возвращает:
            str: Строка, представляющая книгу в формате 'Book(id_=id_, name=name, pages=pages)'.
        """
        return f'{self.__class__.__name__}(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


if __name__ == '__main__':
    # Инициализируем список книг из базы данных
    list_books = [
        Book(id_=book_dict["id_"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # Проверяем метод __str__

    print(list_books)  # Проверяем метод __repr__
