#!/usr/bin/env python

from RPN import RPN

def main():
    line = raw_input("Please enter your expression, or q to exit:\n> ")
    while line.lower() != 'q':
        RPN(line).calculate()
        line = raw_input("Please enter your expression, or q to exit:\n> ")
    print("Goodbye!")


if __name__ == '__main__':
    main()
