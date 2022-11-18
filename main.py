from formulas import *

availableFormulas = ["+", "--", "/", "*", "%", "^", "power", "pow", "root", "-"]


# Leave the - on purpose at the end for situations with negative numbers like (-1 + 2) or (-1 - -2)
# sum | division | multiplication | percent| power | root | subtraction

# in the parse we convert the word for a unique formula: like pow and power to ^ or -- to +
def parseInput(userInput):
    userInput = userInput.replace(" ", "")
    userInput = userInput.replace(",", ".")
    for formula in availableFormulas:
        if formula in userInput.lower():
            realFormula = formula
            if formula == "--":
                userInput = userInput.replace("--", "+")
                realFormula = "+"
            if formula == "power" or formula == "pow":
                userInput = userInput.replace("power", "^")
                userInput = userInput.replace("pow", "^")
                realFormula = "^"
            solve(userInput, realFormula)
            break


def solve(userInput, formula):
    # special case is:
    # change for this situation -1 -1
    especialCase = False
    if formula == '-' and userInput[0] == '-':
        especialCase = True
        values = userInput.split(formula, 2)
    else:
        values = userInput.split(formula, 1)
    if formula == "root":
        if values[0].lower() == "square":
            values[0] = "2"
        if values[0].lower() == "cubic":
            values[0] = "3"
    # Convert the strings to numbers
    try:
        if especialCase:
            number1 = float(values[1]) * -1
            number2 = float(values[2])
        else:
            number1 = float(values[0])
            number2 = float(values[1])
        match formula:
            case "+":
                print(sumNum(number1, number2))
            case "/":
                print(division(number1, number2))
            case "*":
                print(multy(number1, number2))
            case "%":
                print(percent(number1, number2))
            case "^":
                print(pow(number1, number2))
            case "root":
                if number2 < 0:
                    print(str(root(number1, number2)) + "i")
                else:
                    print(root(number1, number2))
            case "-":
                print(sub(number1, number2))
            case _:
                print("There is been an unknown error, please contact us, to give us more information. Try, again")
    except:
        print("An error occur,probably because of a spelling mistake during the input or there was an attempt "
              "of doing multiple operations\nPlease contact us if its not the case, to give us more information")


def helper():
    print("This is a simple calculator")
    print("It can only make the operation between two numbers\n")
    print("Instructions:")
    print("Sum - number + number")
    print("Subtraction - number - number")
    print("Division - number / number")
    print("Multiplication - number * number")
    print("Power - number ^ number or number pow number or number power number")
    print("Root - number root number \n\tsquare root number \n\tcubic root number")
    print("percent - number%number, like 25% of 100")
    input("Press enter to continue")


if __name__ == '__main__':
    print("--------------------Welcome, to the python calculator--------------------")
    print("Write info or help for more info")
    print("Write quit or exit to exit")
    while True:
        userInput = input("Write quit to leave or enter the calculation you want to execute \n")
        if 'info' == userInput.lower() or 'help' == userInput.lower():
            helper()
        if 'quit' == userInput.lower() or 'exit' == userInput.lower():
            break
        parseInput(userInput)
    print("Bye, bye")
