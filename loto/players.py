import random
import sys

from collections import OrderedDict


class Player:
    """
    Базовый класс игрока
    """

    victory_card = [False] * 15

    def __init__(self, name):
        self._name = name
        self.card = self.create_card()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self}')"

    @property
    def name(self):
        return self._name

    @staticmethod
    def create_card():
        """
        Метод создания карточки игрока
        """
        numbers_dict = OrderedDict()
        for i in random.sample(range(1, 91), 15):
            numbers_dict[i] = True
        return numbers_dict

    def mark_number(self, barrel):
        """
        Метод отметки выпавших бочонков
        """
        if barrel in self.card:
            self.card[barrel] = False

    def check_card(self):
        """
        Метод проверки заполненности карточки
        """
        card_status = [x for x in self.card.values()]
        if card_status == self.victory_card:
            return True

    def print_card(self):
        """
        Вывод на экране карточки
        """
        index_slice = 0
        print(f"Карточка игрока {self}")
        print("-" * 20)
        for i in range(3):
            for part in sorted(list(self.card.keys())[index_slice : index_slice + 5]):
                if self.card[part]:
                    print(f"{part:>3}", end=" ")
                else:
                    print(" - ", end=" ")
            index_slice += 5
            print()
        print("-" * 20)


class Human(Player):
    """
    Игрок человек
    """

    def check_answer(self, barrel):
        """
        Проверка зачеркивает или нет цирфу
        """
        answer = input("Зачеркнуть цифру? (y/n): ")
        while True:
            if answer.lower() == "y":
                if barrel in self.card.keys():
                    self.mark_number(barrel)
                    break
                else:
                    print(f"{barrel} нет в карточке игрока {self}!")
                    print(f"Игрок {self} проиграл!")
                    print("Игра завершена!")
                    sys.exit(0)
            elif answer.lower() == "n":
                if barrel in self.card.keys():
                    print(f"{barrel} есть карточке игрока {self}!")
                    print(f"Игрок {self} проиграл!")
                    print("Игра завершена!")
                    sys.exit(0)
                else:
                    break
            else:
                answer = input("Введите y или n: ")


class Computer(Player):
    """
    Игрок компьютер
    """

    pass
