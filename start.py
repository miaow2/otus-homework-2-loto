import random
import sys

from loto.game import Game
from loto.players import Computer, Human, Player


def validate_count(answer):
    """
    Функция валидации ввода количества игроков
    """
    try:
        answer = int(answer)
    except ValueError:
        return False
    if answer <= 0:
        return False

    return answer


def validate_answer(answer):
    """
    Функция валидации ввода ответа
    """
    if answer.lower() == "y":
        return True
    elif answer.lower() == "n":
        return False
    else:
        return None


def create_players():
    """
    Функция создания игроков, их типа и количества
    """
    game = Game()

    for x in ["живых", "компьютерных"]:
        has_players = False
        answer = input(f"Добавить в игру {x} игроков? (y/n): ")
        answer = validate_answer(answer)
        if answer:
            has_players = True
        elif answer is None:
            raise SystemExit('Вводите y или n')

        if has_players:
            answer = input("Введите количество: ")
            count = validate_count(answer)
            if count is False:
                raise SystemExit('Вводите положительное число')
            if x == "живых":
                for i in range(count):
                    game.players.append(Human(input("Введите имя игрока: ")))
            elif x == "компьютерных":
                for i in range(count):
                    game.players.append(Computer(f"Computer {i + 1}"))

    if len(game.players) == 1:
        if isinstance(game.players[0], Human):
            game.players.append(Computer("Computer 1"))
        elif isinstance(game.players[0], Computer):
            game.players.append(Computer("Computer 2"))

    return game


def start():
    """
    Главная функция
    """
    print("Добро пожаловать в игру Лото!")
    game = create_players()
    for p in game:
        p.print_card
    print()
    winners = list()
    while game.barrels:
        barrel = random.choice(game.barrels)
        game.barrels.remove(barrel)
        print(f"Выпал бочонок {barrel}, осталось {len(game.barrels)}")
        for player in game:
            if isinstance(player, Human):
                player.print_card()
                player.check_answer(barrel)
                player.mark_number(barrel)
            elif isinstance(player, Computer):
                player.print_card()
                player.mark_number(barrel)
            if player.check_card():
                winners.append(player.name)
        print()
        if winners:
            print(f"Побидитель/и {', '.join(winners)} выиграл!!!!")
            sys.exit(0)


if __name__ == "__main__":
    start()
