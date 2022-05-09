from re import L
import turtle

print("If you see this, please note that this calculator is very scuffed and a lot of thigns dont work (for example squaring is very broken half the time)")

screen = turtle.Screen()
numbers = []
old = 0
prevNum = 0
operation = ""
printer = ""
ugh = 0
ans = 0

screen.setup(700,1000)
screen.bgcolor("#000000")

screen.addshape("calculatorIcons/zero.gif")
screen.addshape("calculatorIcons/one.gif")
screen.addshape("calculatorIcons/two.gif")
screen.addshape("calculatorIcons/three.gif")
screen.addshape("calculatorIcons/four.gif")
screen.addshape("calculatorIcons/five.gif")
screen.addshape("calculatorIcons/six.gif")
screen.addshape("calculatorIcons/seven.gif")
screen.addshape("calculatorIcons/eight.gif")
screen.addshape("calculatorIcons/nine.gif")
screen.addshape("calculatorIcons/add.gif")
screen.addshape("calculatorIcons/subtract.gif")
screen.addshape("calculatorIcons/multiply.gif")
screen.addshape("calculatorIcons/divide.gif")
screen.addshape("calculatorIcons/squared.gif")
screen.addshape("calculatorIcons/decimal.gif")
screen.addshape("calculatorIcons/backspace.gif")
screen.addshape("calculatorIcons/negative.gif")
screen.addshape("calculatorIcons/clear.gif")
screen.addshape("calculatorIcons/equals.gif")

negative = turtle.Turtle()
negative.shape("calculatorIcons/negative.gif")
negative.penup()
negative.speed(0)
negative.goto(-260, -410)

zero = turtle.Turtle()
zero.shape("calculatorIcons/zero.gif")
zero.penup()
zero.speed(0)
zero.goto(-87, -410)

decimal = turtle.Turtle()
decimal.shape("calculatorIcons/decimal.gif")
decimal.penup()
decimal.speed(0)
decimal.goto(87, -410)

equals = turtle.Turtle()
equals.shape("calculatorIcons/equals.gif")
equals.penup()
equals.speed(0)
equals.goto(260, -410)

one = turtle.Turtle()
one.shape("calculatorIcons/one.gif")
one.penup()
one.speed(0)
one.goto(-260, -250)

two = turtle.Turtle()
two.shape("calculatorIcons/two.gif")
two.penup()
two.speed(0)
two.goto(-87, -250)

three = turtle.Turtle()
three.shape("calculatorIcons/three.gif")
three.penup()
three.speed(0)
three.goto(87, -250)

add = turtle.Turtle()
add.shape("calculatorIcons/add.gif")
add.penup()
add.speed(0)
add.goto(260, -250)

four = turtle.Turtle()
four.shape("calculatorIcons/four.gif")
four.penup()
four.speed(0)
four.goto(-260, -90)

five = turtle.Turtle()
five.shape("calculatorIcons/five.gif")
five.penup()
five.speed(0)
five.goto(-87, -90)

six = turtle.Turtle()
six.shape("calculatorIcons/six.gif")
six.penup()
six.speed(0)
six.goto(87, -90)

subtract = turtle.Turtle()
subtract.shape("calculatorIcons/subtract.gif")
subtract.penup()
subtract.speed(0)
subtract.goto(260, -90)

seven = turtle.Turtle()
seven.shape("calculatorIcons/seven.gif")
seven.penup()
seven.speed(0)
seven.goto(-260, 70)

eight = turtle.Turtle()
eight.shape("calculatorIcons/eight.gif")
eight.penup()
eight.speed(0)
eight.goto(-87, 70)

nine = turtle.Turtle()
nine.shape("calculatorIcons/nine.gif")
nine.penup()
nine.speed(0)
nine.goto(87, 70)

multiply = turtle.Turtle()
multiply.shape("calculatorIcons/multiply.gif")
multiply.penup()
multiply.speed(0)
multiply.goto(260, 70)

clear = turtle.Turtle()
clear.shape("calculatorIcons/clear.gif")
clear.penup()
clear.speed(0)
clear.goto(-260, 230)

squared = turtle.Turtle()
squared.shape("calculatorIcons/squared.gif")
squared.penup()
squared.speed(0)
squared.goto(-87, 230)

backspace = turtle.Turtle()
backspace.shape("calculatorIcons/backspace.gif")
backspace.penup()
backspace.speed(0)
backspace.goto(87, 230)

divide = turtle.Turtle()
divide.shape("calculatorIcons/divide.gif")
divide.penup()
divide.speed(0)
divide.goto(260, 230)

numberPrinter = turtle.Turtle()
numberPrinter.hideturtle()
numberPrinter.penup()
numberPrinter.speed(0)
numberPrinter.goto(300, 330)
numberPrinter.color("#FFFFFF")
numberPrinter.write(printer, align = "right", font = ["Arial", 100, "normal"])
# prevNum = float("".join([str(item) for item in numbers]))
def operationing():
    global prevNum, old, numbers, operation, ans
    if len(numbers) == 0:
        old = ans
    else:
        prevNum = float("".join([str(item) for item in numbers]))
    if operation == "+":
        old += prevNum
    elif operation == "-":
        old -= prevNum
    elif operation == "/":
        old /= prevNum
    elif operation == "*":
        old *= prevNum
def updateNum():
    global numbers, numberPrinter, printer, screen
    printer = "".join([str(item) for item in numbers])
    numberPrinter.clear()
    screen.update()
    numberPrinter.write(printer, align = "right", font = ["Arial", 100, "normal"])
    screen.update()
def bye(x, y):
    global screen
    screen.bye()
def clickZero(x, y):
    global numbers, updateNum
    numbers.append("0")
    updateNum()
def clickOne(x, y):
    global numbers, updateNum
    numbers.append("1")
    updateNum()
def clickTwo(x, y):
    global numbers, updateNum
    numbers.append("2")
    updateNum()
def clickThree(x, y):
    global numbers, updateNum
    numbers.append("3")
    updateNum()
def clickFour(x, y):
    global numbers, updateNum
    numbers.append("4")
    updateNum()
def clickFive(x, y):
    global numbers, updateNum
    numbers.append("5")
    updateNum()
def clickSix(x, y):
    global numbers, updateNum
    numbers.append("6")
    updateNum()
def clickSeven(x, y):
    global numbers, updateNum
    numbers.append("7")
    updateNum()
def clickEight(x, y):
    global numbers, updateNum
    numbers.append("8")
    updateNum()
def clickNine(x, y):
    global numbers, updateNum
    numbers.append("9")
    updateNum()
def clickDecimal(x, y):
    global numbers, updateNum
    numbers.append(".")
    updateNum()
def clickAdd(x, y):
    global numbers, updateNum, joinNumbers, operation, old, ugh
    ugh += 1
    if ugh != 1:
        operationing()
    else:
        if len(numbers) == 0:
            operationing()
        else:
            old = float("".join([str(item) for item in numbers]))
        ugh = 2
    numbers = []
    updateNum()
    operation = "+"
def clickSub(x, y):
    global numbers, updateNum, joinNumbers, operation, old, ugh
    ugh += 1
    if ugh != 1:
        operationing()
    else:
        if len(numbers) == 0:
            operationing()
        else:
            old = float("".join([str(item) for item in numbers]))
        ugh = 2
    numbers = []
    updateNum()
    operation = "-"
def clickMult(x, y):
    global numbers, updateNum, joinNumbers, operation, old, ugh
    ugh += 1
    if ugh != 1:
        operationing()
    else:
        if len(numbers) == 0:
            operationing()
        else:
            old = float("".join([str(item) for item in numbers]))
        ugh = 2
    numbers = []
    updateNum()
    operation = "*"
def clickDiv(x, y):
    global numbers, updateNum, joinNumbers, operation, old, ugh, prevNum
    ugh += 1
    if ugh != 1:
        operationing()
    else:
        if len(numbers) == 0:
            operationing()
        else:
            old = float("".join([str(item) for item in numbers]))
        ugh = 2
    numbers = []
    updateNum()
    operation = "/"
def clickClear(x, y):
    global old, ugh, prevNum, numbers, operation, updateNum
    old = 0
    ugh = 0
    prevNum = 0
    numbers = []
    operation = ""
    updateNum()
def clickSquare(x, y):
    global prevNum, numbers, old, clickEquals, ans
    if len(numbers) == 0:
        old = ans ** 2
    else:
        prevNum = float("".join([str(item) for item in numbers]))
        old = prevNum ** 2
    ans = old
    clickEquals(0, 0)
def clickEquals(x, y):
    global printer, numberPrinter, numbers, old, ugh, prevNum, operation, ans, operationing
    try:
        operationing()
    except:
        pass
    printer = old
    numberPrinter.clear()
    screen.update()
    numberPrinter.write(printer, align = "right", font = ["Arial", 100, "normal"])
    screen.update()
    ans = old
    old = 0
    ugh = 0
    prevNum = 0
    numbers = []
    operation = ""
    print(ans)
    print("^^ there is a limit to how many characters are shown on the screen so this is here to help you see the entire answer btw")
def clickBackspace(x, y):
    global numbers, updateNum
    try:
        numbers.pop()
    except:
        pass
    updateNum()


def azero():
    global clickZero
    clickZero(0, 0)
def aone():
    global clickOne
    clickOne(0, 0)
def atwo():
    global clickTwo
    clickTwo(0, 0)
def athree():
    global clickThree
    clickThree(0, 0)
def afour():
    global clickFour
    clickFour(0, 0)
def afive():
    global clickFive
    clickFive(0, 0)
def asix():
    global clickSix
    clickSix(0, 0)
def aseven():
    global clickSeven
    clickSeven(0, 0)
def aeight():
    global clickEight
    clickEight(0, 0)
def anine():
    global clickNine
    clickNine(0, 0)
def adecimal():
    global clickDecimal
    clickDecimal(0, 0)
def aplus():
    global clickAdd
    clickAdd(0, 0)
def aminus():
    global clickSub
    clickSub(0, 0)
def amultiply():
    global clickMult
    clickMult(0, 0)
def adivide():
    global clickDiv
    clickDiv(0, 0)
def aequals():
    global clickEquals
    clickEquals(0, 0)
def aclear():
    global clickClear
    clickClear(0, 0)
def aback():
    global clickBackspace
    clickBackspace(0, 0)
def abye():
    global bye
    bye(0, 0)

equals.onclick(clickEquals)
zero.onclick(clickZero)
one.onclick(clickOne)
two.onclick(clickTwo)
three.onclick(clickThree)
four.onclick(clickFour)
five.onclick(clickFive)
six.onclick(clickSix)
seven.onclick(clickSeven)
eight.onclick(clickEight)
nine.onclick(clickNine)
decimal.onclick(clickDecimal)
add.onclick(clickAdd)
subtract.onclick(clickSub)
multiply.onclick(clickMult)
divide.onclick(clickDiv)
clear.onclick(clickClear)
squared.onclick(clickSquare)
negative.onclick(bye)
backspace.onclick(clickBackspace)

screen.onkey(azero, "0")
screen.onkey(aone, "1")
screen.onkey(atwo, "2")
screen.onkey(athree, "3")
screen.onkey(afour, "4")
screen.onkey(afive, "5")
screen.onkey(asix, "6")
screen.onkey(aseven, "7")
screen.onkey(aeight, "8")
screen.onkey(anine, "9")
screen.onkey(aback, "BackSpace")
screen.onkey(aequals, "Return")
screen.onkey(aequals, "equal")
screen.onkey(adecimal, "period")
screen.onkey(aclear, "c")
screen.onkey(aplus, "plus")
screen.onkey(aminus, "minus")
screen.onkey(adivide, "slash")
screen.onkey(amultiply, "asterisk")
screen.onkey(abye, "space")
screen.listen()

updateNum()

screen.update()
screen.mainloop()
