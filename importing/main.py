from arithmetic.operation import Operation
import sys


def main():
    guardIsValidInput(sys.argv)
    operation = buildOperation(sys.argv)
    print("{} = {}".format(operation.asString(), operation.calculate()))


def guardIsValidInput(args):
    if len(args) < 4:
        raise Exception(
            "Mandatory arguments not given! Please, inform a arithmetic operation and two operands!")


def buildOperation(args):
    return Operation(args[1], args[2], args[3])


if __name__ == "__main__":
    main()
