import re
import os


def get_oui_file():
    os.system("curl -o oui.txt \"http://standards-oui.ieee.org/oui/oui.txt\"")

def main():
    get_oui_file()
    file = open("oui.txt", "r", encoding="utf8")
    lines = file.readlines()
    file.close()

    new_file = open("../oui_vendors.txt", "w", encoding="utf8")
    for line in lines:
        if (re.search("(base 16)", line)):
            new_file.write(line)
    new_file.close()

if __name__ == "__main__":
    main()
