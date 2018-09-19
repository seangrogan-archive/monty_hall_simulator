import random
import time


def monty_hall_sim(runs=10000, random_seed=None):
    """Runs a simulation of a series of monty hall games. 'runs=' is the variable to
    determine the number of times you run the test.  The program will run 3 cases, always
    switch ("theoretical" optimal solution),  Never switching(sub-optimal solution), and
    Sometimes switching (ignoring the first bit of information in the monty hall problem).
    """
    t_1 = time.time()
    if random_seed is not None:
        random.seed(random_seed)
    game = GameShow()
    always_switch = [0, 0]
    never_switch = [0, 0]
    sometimes_switch = [0, 0]
    for i in range(runs):
# always switch --------------------------------------------------------------------------
        j = game.play(strategy=0)
        if j is True:
            always_switch[0] += 1
        else:
            always_switch[1] += 1
# never switch ---------------------------------------------------------------------------
        k = game.play(strategy=1)
        if k is True:
            never_switch[0] += 1
        else:
            never_switch[1] += 1
# sometimes switch -----------------------------------------------------------------------
        l = game.play(strategy=2)
        if l is True:
            sometimes_switch[0] += 1
        else:
            sometimes_switch[1] += 1
    t_2 = time.time()
# Print Results --------------------------------------------------------------------------
    print('Results:')
    print('Runs: ', runs)
    print('Time: ', int((t_2-t_1)*100)/100, 'seconds')
    if random_seed is not None:
        print('Seed: ', random_seed)
    print('==========================')
    print('Always Switch:')
    print('Win:   ', always_switch[0])
    print('Loss:  ', always_switch[1])
    print('Percentage: ', int((always_switch[0]/runs)*100), '%')
    print('==========================')
    print('Never Switch:')
    print('Win:   ', never_switch[0])
    print('Loss:  ', never_switch[1])
    print('Percentage: ', int((never_switch[0]/runs)*100), '%')
    print('==========================')
    print('Sometimes Switch:')
    print('Win:   ', sometimes_switch[0])
    print('Loss:  ', sometimes_switch[1])
    print('Percentage: ', int((sometimes_switch[0]/runs)*100), '%')
    print('==========================')


class GameShow:
    def __init__(self):
        """Initializes GameShow to a new instance"""
        self._doors = [0, 0, 0]
        self._first_choice = None
        self._second_choice = None
        self._reveal = None

    def results(self):
        """Prints a result table for testing"""
        print('Results Table')
        print('Car:    ', self._doors.index(1))
        print('First:  ', self._first_choice)
        print('Reveal: ', self._reveal)
        print('Second: ', self._second_choice)

    def play(self, strategy=0):
        """Strategy is how one plays the game
        0 is always switch to the other door
        1 is never switch (first choice is second choice)
        2 is sometimes switch (random choice on second choice)
        Any other value will give the 0 strategy"""
        self.set_up()
        self.first_pick()
        self.reveal()
        if strategy is 0:
            self.second_pick(True)
        elif strategy is 1:
            self.second_pick(False)
        elif strategy is 2:
            s = random.choice([True, False])
            self.second_pick(s)
        else:  # Uses the 0 strategy if a silly input is done
            self.second_pick(True)
        return self.is_win()

    def set_up(self, car=None):
        """resets the game"""
        self._first_choice = None
        self._second_choice = None
        self._reveal = None
        self._doors = [0, 0, 0]
        if car is None:
            car = random.randint(0, 2)
        self._doors[car] = 1

    def first_pick(self, pick=None):
        """picks a first pick"""
        if pick is None:
            pick = random.randint(0, 2)
        self._first_choice = pick
        self._reveal = None
        self._second_choice = None

    def reveal(self):
        """Game show host reveals a goat"""
        self._second_choice = None
        if self._first_choice is None:
            self.first_pick()
        for i in range(len(self._doors)):
            if self._doors[i] is 0:
                if i != self._first_choice:
                    self._reveal = i

    def second_pick(self, switch=True):
        """user picks a new door"""
        if self._reveal is None:
            self.reveal()
        if switch is True:
            self._second_choice = 3 - (self._first_choice + self._reveal)
        else:
            self._second_choice = self._first_choice

    def is_win(self):
        """returns the win state"""
        if self._second_choice is None:
            self.second_pick()
        i = self._second_choice
        if self._doors[i] is 1:
            return True
        else:
            return False


def main(sims=3):
    for i in range(sims):
        monty_hall_sim(random_seed=1)


main(1)
