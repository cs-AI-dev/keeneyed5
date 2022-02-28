import blessed
import internalUtilities as utils
import datetime

term = blessed.Terminal()

xindex = 4

def resetCLI():
    global xindex

    print(term.center("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"))
    print(term.center("┃ KEENEYED-5 ARTIFICIAL GENERAL INTELLIGENCE SYSTEM ┃"))
    print(term.center("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"))
    print("━┳" + utils.listtostring(["━" for x in range(term.width - 4)]) + "┳━")
    [print(" ┃" + utils.listtostring([" " for x in range(term.width - 4)]) + "┃ ") for x in range(term.height - 8)]
    print(" ┣" + utils.listtostring(["━" for x in range(term.width - 4)]) + "┫ ")
    print(" ┃" + utils.listtostring([" " for x in range(term.width - 4)]) + "┃ ")
    print(" ┗" + utils.listtostring(["━" for x in range(term.width - 4)]) + "┛ ")
    xindex = 4

def display(txt):
    global xindex

    with term.location(3, term.height - 3):
        print(term.white_on_black(utils.listtostring([" " for x in range(term.width - 20)])))
    with term.location(3, xindex):
        print(term.white_on_black(txt))
    xindex += 1
    if xindex >= term.height - 9:
        resetCLI()
        xindex = 4

    with open(__file__[:-23] + "/executionTranscripts/current.ke5", "a") as f:
        dt = datetime.date.today().strftime("%m/%d/%y")
        f.write(f"\n[{dt} @ {datetime.datetime.now().time()}] {txt}")

def getUserInput(prompt):
    with term.location(3, term.height - 3):
        print("                                               ")
    with term.location(3, term.height - 3):
        out = input(prompt + " ")
    display("[USER] " + prompt + " " + out)
    return out
