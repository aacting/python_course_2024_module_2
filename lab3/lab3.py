class Book:
    """ Базовый класс книги.

    Атрибуты:
        _name (str): Название книги.
        _author (str): Автор книги.
    """

    def __init__(self, name: str, author: str):
        """Инициализирует экземпляр класса Book.

        Аргументы:
            name (str): Название книги.
            author (str): Автор книги.
        """
        self._name = name
        self._author = author

    @property
    def name(self):
        """Возвращает название книги."""
        return self._name

    @property
    def author(self):
        """Возвращает автора книги."""
        return self._author

    def __str__(self):
        """Возвращает строковое представление книги."""
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        """Возвращает формальное строковое представление книги."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс. Бумажная книга.

    Атрибуты:
        pages (int): Количество страниц в книге.
    """

    def __init__(self, name: str, author: str, pages: int):
        """Инициализирует экземпляр класса PaperBook.

        Аргументы:
            name (str): Название книги.
            author (str): Автор книги.
            pages (int): Количество страниц в книге.
        """
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, value):
        """Устанавливает количество страниц в книге.

        Аргументы:
            value (int): Количество страниц.

        Исключения:
            TypeError: Если количество страниц не является целым числом.
            ValueError: Если количество страниц меньше или равно 0.
        """
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("В книге должна быть хотя бы одна страница")
        self._pages = value

    def __str__(self):
        """Возвращает строковое представление бумажной книги."""
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self):
        """Возвращает формальное строковое представление бумажной книги."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Дочерний класс. Аудиокнига.

    Атрибуты:
        duration (float): Продолжительность аудиокниги в часах.
    """

    def __init__(self, name: str, author: str, duration: float):
        """Инициализирует экземпляр класса AudioBook.

        Аргументы:
            name (str): Название книги.
            author (str): Автор книги.
            duration (float): Продолжительность аудиокниги в часах.
        """
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        """Возвращает продолжительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value):
        """Устанавливает продолжительность аудиокниги.

        Аргументы:
            value (float): Продолжительность аудиокниги.

        Исключения:
            TypeError: Если продолжительность не является числом.
            ValueError: Если продолжительность меньше или равна 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность книги должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность книги должна быть больше 0")
        self._duration = value

    def __str__(self):
        """Возвращает строковое представление аудиокниги."""
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        """Возвращает формальное строковое представление аудиокниги."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
