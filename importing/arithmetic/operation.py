import arithmetic.basic as ops


class Operation:
    def __init__(self, operation, x, y):
        self.setOperation(operation)
        self.setX(x)
        self.setY(y)

    def setOperation(self, operation):
        if (operation != "+" and operation != "-" and operation != "*" and operation != "/"):
            raise Exception(
                "The operation [{}] is invalid! Please, select one of the supported operations [+, -, *, /]".format(operation))

        self.operation = operation

    def setX(self, x):
        self.guardIsValidInteger(x)
        self.x = int(x)

    def setY(self, y):
        self.guardIsValidInteger(y)
        self.y = int(y)

    def guardIsValidInteger(self, value):
        try:
            int(value)
        except ValueError:
            raise Exception(
                "Given operators [{}] and is not a integer! Please, provide a valid integer input for both operators!".format(value))

    def asString(self):
        return ("({} {} {})".format(self.operation, self.x, self.y))

    def calculate(self):
        result = 0

        if self.operation == "+":
            result = ops.sum(self.x, self.y)
        elif self.operation == "-":
            result = ops.sub(self.x, self.y)
        elif self.operation == "*":
            result = ops.prod(self.x, self.y)
        elif self.operation == "/":
            result = ops.div(self.x, self.y)
        else:
            raise Exception(
                "Unsupported operation [{}]. There may be a application logic error!".format(self.operation))

        return result
