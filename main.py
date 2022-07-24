from ft_math import *
import sys

def calcul(data):
    equation = ft_math()
    data = equation.extract_equation(data)
    print("this is ",data[1],len(data[1]))










if __name__ == "__main__":
    if len(sys.argv) == 2:
        data_argv = sys.argv[1]
        size = len(data_argv.split("="))
        if size == 2:
            calcul(data_argv)
        else:
            print("rror, multiple '=' found in the expression please check the expression and retry\n")

    else:
        print("Erreur")
