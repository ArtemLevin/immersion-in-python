import argparse


def summa(a, b):
    return a + b

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This function can be used to add up the numbers")
    parser.add_argument("a", metavar="a", type=int, default=0)
    parser.add_argument("b", metavar="b", type=int, default=0)
    args = parser.parse_args()
    print(summa(args.a, args.b))

