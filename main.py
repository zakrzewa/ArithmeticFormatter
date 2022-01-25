import re

print("Our Magical Calculator")
print("Print quit to exit")

previous = 0
run = True

def do_math():
    global run
    global previous
    equatation = ""

    if previous == 0:
        equatation = input("Provide your equatation: ")
    else:
        equatation = input(str(previous))

    if (equatation == 'quit'):
        run = False
    else:
        equatation = re.sub('[a-zAZ.,:()+" "]', '', equatation)

        if previous == 0:
            previous = eval(equatation)
        else:
             previous = eval(str(previous) + equatation)

while run:
    do_math()

