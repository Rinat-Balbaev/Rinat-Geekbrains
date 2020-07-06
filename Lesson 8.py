from random import randint

def number_gen (count, min, max):
    if count > max - min + 1:
        raise ValueError('Incorrect value')
    rand_number = []
    while len(rand_number) < count:
        new = randint(min, max)
        if new not in rand_number:
            rand_number.append(new)
    return rand_number

class Barrel:
    __num = None

    def __init__(self):
        self.__num = randint(1, 90)

    @property
    def num(self):
        return self.__num

    def __str__(self):
        return str(self.__num)

class Card:
    __rows = 3
    __cols = 9
    __nums_in_row = 5
    __data = None
    __emptynum = 0
    __crossednum = -1

    def __init__(self):
        uniques_count = self.__nums_in_row * self.__rows
        uniques = number_gen(uniques_count, 1, 90)

        self.__data = []
        for i in range(0, self.__rows):
            tmp = sorted(uniques[self.__nums_in_row * i: self.__nums_in_row * (i + 1)])
            empty_nums_count = self.__cols - self.__nums_in_row
            for j in range(0, empty_nums_count):
                index = randint(0, len(tmp))
                tmp.insert(index, self.__emptynum)
            self.__data += tmp

    def __str__(self):
        delimiter = '--------------------------'
        ret = delimiter + '\n'
        for index, num in enumerate(self.__data):
            if num == self.__emptynum:
                ret += '  '
            elif num == self.__crossednum:
                ret += ' -'
            elif num < 10:
                ret += f' {str(num)}'
            else:
                ret += str(num)

            if (index + 1) % self.__cols == 0:
                ret += '\n'
            else:
                ret += ' '

        return ret + delimiter

    def __contains__(self, item):
        return item in self.__data

    def cross_num(self, num):
        for index, item in enumerate(self.__data):
            if item == num:
                self.__data[index] = self.__crossednum
                return
        raise ValueError(f'Number not in card: {num}')

    def closed(self) -> bool:
        return set(self.__data) == {self.__emptynum, self.__crossednum}


class Game:
    __usercard = None
    __compcard = None
    __numbarrels = 90
    __barrels = []
    __gameover = False

    def __init__(self):
        self.__usercard = Card()
        self.__compcard = Card()
        self.__barrels = number_gen(self.__numbarrels, 1, 90)

    def play_round(self) -> int:
        """
        :return:
        0 - game must go on
        1 - user wins
        2 - computer wins
        """

        barrel = self.__barrels.pop()
        print(f'Новый бочонок: {barrel} (осталось {len(self.__barrels)})')
        print(f'----- Ваша карточка ------\n{self.__usercard}')
        print(f'-- Карточка компьютера ---\n{self.__compcard}')

        useranswer = input('Зачеркнуть цифру? (y/n)').lower().strip()
        if useranswer == 'y' and not barrel in self.__usercard or \
           useranswer != 'y' and barrel in self.__usercard:
            return 2

        if barrel in self.__usercard:
            self.__usercard.cross_num(barrel)
            if self.__usercard.closed():
                return 1
        if barrel in self.__compcard:
            self.__compcard.cross_num(barrel)
            if self.__compcard.closed():
                return 2

        return 0


if __name__ == '__main__':
    game = Game()
    while True:
        score = game.play_round()
        if score == 1:
            print('Вы выиграли!')
            break
        elif score == 2:
            print('Вы проиграли')
            break