"""" For Github Upload Test from main pc"""

"""" Author Calum Farrar """


def print_greeting():
    print('Hello Github')


print_greeting()


print("Here is some shitty date input system")


def date_input(YYYY, MM, DD):
    if YYYY < 1 or YYYY > 9999:
        print("Invalid Year")
    elif MM < 1 or MM > 12:
        print("Invalid Month")
    elif DD < 1 or DD > 31:
        print("Invalid Day")
    elif DD > 30 and MM == [2, 4, 6, 9, 11]:
        print("Invalid Day")
    elif DD > 28 and MM == 2:
        print("Invalid Day")
    else:
        print(YYYY, MM, DD)


date_input(1996, 6, 14)
