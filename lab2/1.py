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

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        # self.__class__.__name__ вместо явного указания названия класса
        return f'{self.__class__.__name__}(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id_"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
