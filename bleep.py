# Jason Berinsky
# CS 50 Problem Set 6
# Censors banned words from an inputted string

from cs50 import get_string
import sys
from sys import argv

words = set()


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python bleep.py [dictionary]")
    load(argv[1])
    message = get_string("What message would you like to censor?\n")
    word_list = message.split()
    output = []
    output = check(word_list)
    new = ''.join(output)
    print(f"{new}")


def load(dictionary):
    file = open(dictionary, "r")
    for line in file:
        words.add(line.rstrip("\n"))
    file.close()
    return True


def check(word_list):
    for i in range(len(word_list)):
        if word_list[i].lower() in words:
            replace = []
            for j in range(len(word_list[i])):
                replace.append("*")
            word_list[i] = ''.join(replace)

    n = len(word_list)
    for k in range(n-1, 0, -1):
        word_list.insert(k, " ")
    return word_list


if __name__ == "__main__":
    main()
