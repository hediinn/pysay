import sys, argparse


END_OF_LINE_CHAR = ",,-,,.."

LINE_LENGTH = 68


def cat():
    print("                              //" + END_OF_LINE_CHAR)
    print('    _._     _,-\'""`-._       //' + END_OF_LINE_CHAR)
    print("   (,-.`._,'(       |\\`-/|  //" + END_OF_LINE_CHAR)
    print("       `-.-' \\ )-`( , o o) // " + END_OF_LINE_CHAR)
    print("          `-    \\`_`\"'-     " + END_OF_LINE_CHAR)


def cow():
    print("       \\   ^__^                 " + END_OF_LINE_CHAR)
    print("        \\  (oo)\\_______        " + END_OF_LINE_CHAR)
    print("           (__)\\       )\\/\\   " + END_OF_LINE_CHAR)
    print("               ||----w |         " + END_OF_LINE_CHAR)
    print("               ||     ||         " + END_OF_LINE_CHAR)


def snake():
    print("       \\      __" + END_OF_LINE_CHAR)
    print("        \\    {0O}" + END_OF_LINE_CHAR)
    print("             \\__/" + END_OF_LINE_CHAR)
    print("             /^/" + END_OF_LINE_CHAR)
    print("            ( (             " + END_OF_LINE_CHAR)  # -Peter Bier-")
    print("            \\_\\_____" + END_OF_LINE_CHAR)
    print("            (_______)" + END_OF_LINE_CHAR)
    print("           (_________()Oo" + END_OF_LINE_CHAR)


def dolphin():
    print("                \\   " + END_OF_LINE_CHAR)
    print("             ,   \\     " + END_OF_LINE_CHAR)
    print("           __)\\___      " + END_OF_LINE_CHAR)
    print("       _.-'      .`-. " + END_OF_LINE_CHAR)
    print("     .'/~~```\"~z/~'\"`" + END_OF_LINE_CHAR)
    print("     ^^" + END_OF_LINE_CHAR)


def myArgsParse(b_type):
    if b_type == "dolphin" or b_type == "evie":
        dolphin()
    elif b_type == "snake" or b_type == "python":
        snake()
    elif b_type == "cat":
        cat()
    else:
        cow()


def splitter_of_line(string: str):
    string_b = string.strip()
    if len(string_b) > LINE_LENGTH:
        t_string = string_b.find(" ", LINE_LENGTH - 8)
        return string_b + str(string_b.count('\t')) + " 33"
    else:
        return string_b + str(string_b.count('\t')) + " 1"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type")
    args = parser.parse_args()
    line = list(sys.stdin)

    if (len(line[0])) >= LINE_LENGTH + 2:
        LINE_LENGTH = len(line[0]) - 1
    if len(line) == 1 and len(line[0]) < LINE_LENGTH:
        a = line[0]
        a = a[0:-1]
        print(" " + f"_" * LINE_LENGTH + " ")
        print("<" + f"{a:^{LINE_LENGTH}}" + ">")
        print(" " + "-" * LINE_LENGTH + " ")
    elif len(line) == 0:
        pass

    else:
        print("┌" + "─" * LINE_LENGTH + "┐", end="\n")
        startchar = "│"
        endchar = "│"
        new_line = line[-20:]
        new_line = list(map(lambda x: splitter_of_line(x),new_line))
        for b in new_line:
            a = b.strip()
            if str(a)[-8:-1] == (END_OF_LINE_CHAR):
                pass
            if len(a) < 3:
                temp_string = f"{startchar}{str(a)+'  ':^{LINE_LENGTH}}{endchar}"
                print(temp_string, end="\n")
            else:
                temp_string = f"{startchar}{str(a):^{LINE_LENGTH}}{endchar}"
                print(temp_string)
        print("└" + "─" * LINE_LENGTH + "┘")
    a_type = args.type
    myArgsParse(a_type)


