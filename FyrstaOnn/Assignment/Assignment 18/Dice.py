# The implementation of Dice goes here
import random

class Dice:
    def __init__(self, sides, num=0):
        self.sides = sides
        self.num = int(num)
    
    def __str__(self):
        return str(self.num)

    def roll (self):
        self.num = random.randint(1, self.sides)

    def __add__ (self, other):
        sum_dice = self.num + other.num
        sides_sum = self.sides + other.sides
        return Dice(sides_sum, sum_dice)


def run_dice_experiment():
    dice1 = Dice(6)
    dice2 = Dice(6)
    for _ in range(0,10):
        dice1.roll()
        dice2.roll()
        sum_dice = dice1 + dice2
        print("dice1: {}, dice2: {}, sum dice: {}".format(str(dice1), str(dice2), str(sum_dice)))
        sum_dice.roll()
        print("sum dice: {}".format(str(sum_dice)))

# Main program starts here
seed_number = int(input("Enter a seed: "))
random.seed(seed_number)
run_dice_experiment()