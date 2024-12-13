import doctest


class Furniture:
    def __init__(self, material: str, height: float, width: float):
        """
        Инициализация объекта Furniture.

        :param material: Материал, из которого изготовлена мебель. Должен быть строкой.
        :param height: Высота мебели в сантиметрах. Должна быть положительным числом.
        :param width: Ширина мебели в сантиметрах. Должна быть положительным числом.

        :raises ValueError: Если height или width не положительные.

        >>> chair = Furniture("Wood", 100, 50)
        """
        if height <= 0 or width <= 0:
            raise ValueError("Height and width must be positive numbers.")

        self.material = material
        self.height = height
        self.width = width

    def assemble(self) -> None:
        """
        Метод для сборки мебели.
        """
        ...

    def disassemble(self) -> None:
        """
        Метод для разборки мебели.
        """
        ...


class Tree:
    def __init__(self, species: str, age: int, height: float):
        """
        Инициализация объекта Tree.

        :param species: Вид дерева. Должен быть строкой.
        :param age: Возраст дерева в годах. Должен быть неотрицательным целым числом.
        :param height: Высота дерева в метрах. Должна быть положительным числом.

        :raises ValueError: Если age отрицательный или height не положительная.

        >>> oak = Tree("Oak", 50, 20.5)
        """
        if age < 0 or height <= 0:
            raise ValueError("Age must be non-negative and height must be positive.")

        self.species = species
        self.age = age
        self.height = height

    def grow(self, years: int) -> None:
        """
        Метод для роста дерева на заданное количество лет.

        :param years: Количество лет для роста. Должно быть неотрицательным целым числом.

        :raises ValueError: Если years отрицательный.
        """
        ...

    def shed_leaves(self) -> None:
        """
        Метод для сбрасывания листьев деревом.
        """
        ...


class SocialMedia:
    def __init__(self, name: str, user_count: int, launch_year: int):
        """
        Инициализация объекта SocialMedia.

        :param name: Название социальной сети. Должен быть строкой.
        :param user_count: Количество пользователей. Должно быть неотрицательным целым числом.
        :param launch_year: Год запуска социальной сети. Должен быть целым числом.

        :raises ValueError: Если user_count отрицательный или launch_year нецелый.

        >>> facebook = SocialMedia("Facebook", 2900000000, 2004)
        """
        if user_count < 0:
            raise ValueError("User count must be non-negative.")

        self.name = name
        self.user_count = user_count
        self.launch_year = launch_year

    def add_user(self) -> None:
        """
        Метод для добавления нового пользователя.
        """
        ...

    def remove_user(self) -> None:
        """
        Метод для удаления пользователя.
        """


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
