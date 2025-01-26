from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Базовый класс для всех животных.
    """
    def __init__(self, name: str, age: int):
        self._name = name  # Имя животного, непубличный атрибут
        self._age = age    # Возраст животного, непубличный атрибут

    def __str__(self) -> str:
        return f"Animal(Name: {self._name}, Age: {self._age})"

    def __repr__(self) -> str:
        return f"Animal(name={self._name!r}, age={self._age!r})"

    @abstractmethod
    def make_sound(self) -> str:
        """
        Абстрактный метод для издания звука животным.
        """
        pass

class Dog(Animal):
    """
    Дочерний класс для собак.
    """
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed  # Порода собаки

    def __str__(self) -> str:
        return f"Dog(Name: {self._name}, Age: {self._age}, Breed: {self.breed})"

    def __repr__(self) -> str:
        return f"Dog(name={self._name!r}, age={self._age!r}, breed={self.breed!r})"

    def make_sound(self) -> str:
        """
        Перегрузка метода make_sound для собак.
        """
        return "Woof!"

    def fetch(self, item: str) -> str:
        """
        Метод для команды собаке принести предмет.
        """
        return f"{self._name} fetched the {item}!"

class Cat(Animal):
    """
    Дочерний класс для кошек.
    """
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color  # Цвет кошки

    def __str__(self) -> str:
        return f"Cat(Name: {self._name}, Age: {self._age}, Color: {self.color})"

    def __repr__(self) -> str:
        return f"Cat(name={self._name!r}, age={self._age!r}, color={self.color!r})"

    def make_sound(self) -> str:
        """
        Перегрузка метода make_sound для кошек.
        """
        return "Meow!"

    def scratch(self) -> str:
        """
        Метод для команды кошке поцарапать.
        """
        return f"{self._name} is scratching!"

# Пример использования
dog = Dog(name="Buddy", age=3, breed="Golden Retriever")
cat = Cat(name="Whiskers", age=2, color="Black")

print(dog)  # Dog(Name: Buddy, Age: 3, Breed: Golden Retriever)
print(cat)  # Cat(Name: Whiskers, Age: 2, Color: Black)

print(dog.make_sound())  # Woof!
print(cat.make_sound())  # Meow!

print(dog.fetch("ball"))  # Buddy fetched the ball!
print(cat.scratch())      # Whiskers is scratching!