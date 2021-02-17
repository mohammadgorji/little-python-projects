# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Stack class


class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, item):
        if len(self.stack) < self.size:
            self.stack.append(item)

    def pop(self):
        result = -1

        if self.stack != []:
            result = self.stack.pop()
        return result

    def isEmpty(self):
        return self.stack == []

    def topChar(self):
        result = -1

        if self.stack != []:
            result = self.stack[len(self.stack) - 1]

        return result
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# convert a string type number to an intiger one


def toInt(number):
    if type(number) == str:
        return ord(number)-48
    return number

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# check if char is an operand


def isOperand(char):
    return ord(char) >= 48 and ord(char) <= 57


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# check if char is an operator


def isOperator(char):
    return char in "+-*/"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# get priority for operator


def priority(char):
    if char in "+-":
        return 1
    else:
        return 2


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# return least priority for an operator in an expression


def lowestPriority(expression):
    lowest = 2
    countCondition = True

    for char in expression:
        if countCondition and isOperator(char):
            opPriority = priority(char)

            if opPriority < lowest:
                lowest = opPriority
        elif char == '(':
            countCondition = False
        elif char == ')':
            countCondition = True

    return lowest

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# postfix to infix


def toInfix(expression):
    result = ""

    stack = Stack(20)

    for char in expression:
        if isOperand(char):
            stack.push(char)
        else:
            exp2 = stack.pop()
            exp1 = stack.pop()
            operatorPriority = priority(char)
            lpExp2 = lowestPriority(exp2)
            lpExp1 = lowestPriority(exp1)

            if lpExp2 < operatorPriority:
                exp2 = '(' + exp2 + ')'

            if lpExp1 < operatorPriority:
                exp1 = '(' + exp1 + ')'

            newExpression = exp1 + char + exp2
            stack.push(newExpression)

    result = stack.pop()

    return result

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# infix to postfix


def toPostfix(expression):
    result = ""

    stack = Stack(20)

    for char in expression:
        if isOperand(char):
            result += char
        elif isOperator(char):
            while True:
                topChar = stack.topChar()

                if stack.isEmpty() or topChar == '(':
                    stack.push(char)
                    break
                else:
                    charPriority = priority(char)
                    topCharPriority = priority(topChar)

                    if charPriority > topCharPriority:
                        stack.push(char)
                        break
                    else:
                        result += stack.pop()

        elif char == '(':
            stack.push(char)
        elif char == ')':
            cpop = stack.pop()
            while cpop != '(':
                result += cpop
                cpop = stack.pop()

    while not stack.isEmpty():
        cpop = stack.pop()
        result += cpop

    return result

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# evalute the result base on postfix expression


def evalute(expression):
    stack = Stack(20)

    for char in expression:
        if char in "+-*/":
            operand2 = toInt(stack.pop())
            operand1 = toInt(stack.pop())
            if char == "+":
                result = operand1 + operand2
            elif char == "-":
                result = operand1 - operand2
            elif char == "*":
                result = operand1 * operand2
            else:
                result = operand1 / operand2
            stack.push(result)
        else:
            stack.push(toInt(char))
    return stack.pop()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# main menu
menu = True
while menu:
    print("~~~~~~~~~~~~~~~~~~menu~~~~~~~~~~~~~~~~~~")
    choice = input(
        "1)Infix to Postfix\n2)Postfix to Infix\n3)Exit\nPlease choose:")
    choice = int(choice)
    print("\n")

    if choice == 1:
        exp = input("Enter your expression:")
        print()
        postfix = toPostfix(exp)
        result = evalute(postfix)
        print('Infix:', exp, '\nPostfix:', postfix, '\nresult:', result)
        print("\n")

    elif choice == 2:
        exp = input("Enter your expression:")
        print()
        infix = toInfix(exp)
        result = evalute(exp)
        print('Postfix:', exp, '\nInfix:', infix, '\nresult:', result)
        print("\n")

    elif choice == 3:
        print("Thank You!\nSee you later...\n")
        menu = False

    else:
        print("Please enter a valid number!\n")
