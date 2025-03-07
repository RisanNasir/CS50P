def calculate(exp):
    explist = exp.split()
    x = float(explist[0])
    y = float(explist[2])
    op = explist[1]
    ##print(x,op,y)
    match op:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            return x / y

def main():
    exp = input("Expression: ")
    result = calculate(exp)
    print(result)


main()
