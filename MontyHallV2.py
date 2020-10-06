__author__ = 'Sean Grogan'
# Monty Hall Problem statistical demo

import random


def main(n, iteration):
    random_picker = Ticker()
    smart_picker = Ticker()
    never_switcher = Ticker()
    i = 0
    while i < iteration:
        door = []
        for j in range(n):
            door.append(0)
        door[random.randint(0, n-1)] = 1
        first_choice = random.randint(0, n-1)
        if door[first_choice] == 1:
            smart_picker.fail()
            never_switcher.win()
            door.remove(0)
            random.randint(0,1)
            if door[random.randint(0,1)] == 1:
                random_picker.win()
            else:
                random_picker.fail()
        else:
            smart_picker.win()
            never_switcher.fail()
            door.remove(0)
            if door[random.randint(0,1)] == 1:
                random_picker.win()
            else:
                random_picker.fail()
        i += 1

    print('smart', list(smart_picker.tally()))
    print('never switcher', list(never_switcher.tally()))
    print('random picker', list(random_picker.tally()))


class Ticker:
    def __init__(self):
        self._win = 0
        self._fail = 0

    def win(self):
        self._win += 1

    def fail(self):
        self._fail += 1

    def tally(self):
        ret = (self._win, self._fail)
        return ret

main(3, 10000)
