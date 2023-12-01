import re
import sys


def main():
    print(count(input("Input: ")))


def count(s):
    find_um = re.findall(r"\b\W*um\W", s, re.IGNORECASE) 
    return len(find_um)


...


if __name__ == "__main__":
    main()