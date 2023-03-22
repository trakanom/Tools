'''
Honestly an overcomplicated dice roll to end indecision.
'''
import random


def roll_dice(choicelist):
    """Simulate a dice roll to determine a winner from the given list."""
    counter = [0] * len(choicelist)
    winners = []

    for _ in range(len(choicelist) * 2 + 1):
        this_round = random.randint(0, len(choicelist) - 1)
        counter[this_round] += 1

    for i, val in enumerate(counter):
        if val == max(counter):
            winners.append(choicelist[i])

    if len(winners) > 1:
        output_string = ", ".join(winners[:-1]) + ", " + winners[-1]
        print(f"\033[1;32m{output_string} are tied for first. Re-rolling.\033[0m")
        roll_dice(winners)
    else:
        print(f"\033[1;32m* * * W I N N E R * * *\n{winners[0]} has the win!\033[0m")


def generate_dice_dict():
    """Generate a dictionary of dice from d3 to d100."""
    dice = {
        "coin": ["Heads", "Tails"],
    }
    for i in range(3, 101):
        dice["d" + str(i)] = list(range(1, i + 1))
    return dice


dice_dict = generate_dice_dict()
user_input = input("What do you want me to choose from? (Separate with commas): ")
choices = [choice.strip() for choice in user_input.split(',')]

if len(choices) == 1 and choices[0] in dice_dict.keys():
    choices = dice_dict[choices[0]]

if len(choices) < 1:
    choices = ["fill in the choices", "do homework", "sleep", "uhhhhhh"]

roll_dice(choices)
