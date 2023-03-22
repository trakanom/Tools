from random import randint as roll
import sys
def Dice_Roll(dicepicker):
    die = dicepicker.split("+")
    results = 0
    for i,dice in enumerate(die):
        dice = dice.split("d")
        rolls = int(dice[0])
        num = int(dice[1])
        thisroll = []
        for n in range(rolls):
            thisroll.append(roll(1,num))
        # results.append(thisroll+[f"Result={sum(thisroll)}"])
        results=thisroll
    # return f"{results}\nTotal sum: {sum(sums)}"
    return results
def FlagParser(die):
    
    is_wild=False
    top_count=0
    result=None
    for dice in die:
        if dice[0].isnumeric():
            result = Dice_Roll(dice)
        if dice.lower()=="wild":
            is_wild=True
        if dice.lower().startswith("top"):
            top_count=int(dice[3:].strip())
            # print(top_count)
    if result is not None:
        if top_count>0:
            new_result=sorted(result,reverse=True)
            # print("sorted",result)
            tops=new_result[:top_count]
            # print("trimmed",result)
            print(f"{die[0]} results:\t{result}, top rolls={tops}, Sum={sum(tops)}")
        else:
            print(f"{die[0]} results:\t{result}, Sum={sum(result)}")
        return result
    else:
        print("Error, no dice rolls to do.")
            



def Parser(command=None):
    # try:
    if command is None:
        print("Error: No command given. Type 'help' for help.")
    elif command.lower()=='help':
        print("Use this program to roll dice in many different ways. The proper syntax of such is as follows.\n\t'NdX':\tRoll an 'X' sided dice 'N' times. Join with '+'(Ex:'2d20+1d6' to roll 2 d20s and 1 d6)\n\t'Special Commands':\tThese commands are in beta. Use at your own peril. Join with ',' following the dice you want to use this on.\n\t\t(Ex:'6d10,top10+1d6' would take the top 3 numbers from the '6d10' rolls then perform an additonal '1d6' roll.\n\t'topY':\tTake the top 'Y' of the joined dice rolls. ('6d10,top3' will return the 3 highest rolls in that set)\n\t'wild':\tDoes some stuff. I don't know yet. Something about rolling a 1 or a 6? Who knows.\n\t'sum':\tUsed by default, only use this if you don't care about knowing the particulars of your roll.")
    elif command.lower()=="exit":
        global exit
        exit = True
        print("Good-bye.")
    else:
        die = command.split("+")
        for dice in die:
            dice=dice.split(",")
            FlagParser(dice)
            # These_Rolls = Dice_Roll(dicepicker=command)
        #             ThisWild = True if 'wild' in flags else False
        # if 'top' in flags:
        #     print("we found the top!")
    # except:
    #     print("Error: No command given. Type 'help' for help.")

if __name__ == '__main__':
    # print(Dice_Roll("4d20"))
    # print(Dice_Roll(sys.argv[1]))
    exit=False
    while not exit:
        Parser(input())




"""
if command is None:
    Error: No command given. Type 'help' for help.
if command is 'help':
    Use this program to roll dice in many different ways. The proper syntax of such is as follows.\n
    \t'NdX':\tRoll an 'X' sided dice 'N' times. ('2d20' to roll 2 d20s)\n
    \t\t'+':\tJoin additional rolls and types. ('2d20+1d6' to roll 2 d20s then 1d6')\n
    \t'Special Commands':\tThese commands are in beta. Use at your own peril.\n
    \t\t',':\tJoin these commands together for additional fun!\n
    \t'topY':\tTake the top 'Y' of the joined dice rolls. ('6d10,top3' will return the 3 highest rolls in that set)\n
    \t'wild':\tDoes some stuff. I don't know yet. Something about rolling a 1 or a 6? Who knows.\n
    \t'sum':\tUsed by default, only use this if you don't care about knowing the particulars of your roll.
if command is 'exit':
    end program


"""
