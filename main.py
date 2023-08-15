import sys,argparse


END_OF_LINE_CHAR = ",,-,,.."

def cat():
    print("                              //"+END_OF_LINE_CHAR)
    print("    _._     _,-\'\"\"`-._       //"+END_OF_LINE_CHAR)
    print("   (,-.`._,\'(       |\\`-/|  //"+END_OF_LINE_CHAR)
    print("       `-.-\' \\ )-`( , o o) // "+END_OF_LINE_CHAR)
    print("          `-    \\`_`\"\'-     "+END_OF_LINE_CHAR)

def cow():
    print("       \\   ^__^                 "+END_OF_LINE_CHAR)
    print("        \\  (oo)\\_______        "+END_OF_LINE_CHAR)
    print("           (__)\\       )\\/\\   "+END_OF_LINE_CHAR)
    print("               ||----w |         "+END_OF_LINE_CHAR)
    print("               ||     ||         "+END_OF_LINE_CHAR)

def snake():
    print("       \\      __"+END_OF_LINE_CHAR)
    print("        \\    {0O}"+END_OF_LINE_CHAR)
    print("             \\__/"+END_OF_LINE_CHAR)
    print("             /^/"+END_OF_LINE_CHAR)
    print("            ( (             "+END_OF_LINE_CHAR)# -Peter Bier-")
    print("            \\_\\_____"+END_OF_LINE_CHAR)
    print("            (_______)"+END_OF_LINE_CHAR)
    print("           (_________()Oo"+END_OF_LINE_CHAR)

def dolphin():
    print("                \\   "+END_OF_LINE_CHAR)
    print("             ,   \\     "+END_OF_LINE_CHAR)
    print("           __)\\___      "+END_OF_LINE_CHAR)
    print("       _.-'      .`-. "+END_OF_LINE_CHAR)
    print("     .'/~~```\"~z/~'\"`"+END_OF_LINE_CHAR)
    print("     ^^"+END_OF_LINE_CHAR)


def myArgsParse(b_type):
    if (b_type == "dolphin" or b_type == "evie"):
        dolphin()
    elif (b_type == "snake" or b_type == "python"):
        snake()
    elif (b_type == "cat"):
        cat()
    else:
        cow()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type')
    args = parser.parse_args()
    LINE_LENGTH = 78
    line = list(sys.stdin)
    
    if (len(line[0])) >= 78:
        LINE_LENGTH = len(line[0])-1
    if len(line)== 1:
        a = line[0]
        a = a[0:-1]
        print(" "+f"_"*LINE_LENGTH+" ")
        print("<" + f"{a:^{LINE_LENGTH}}"+">")
        print(" "+ "-"*LINE_LENGTH +" ")
    elif len(line) == 0:
        pass

    else:
        print("┌"+ "─"*LINE_LENGTH + "┐")
        startchar = "│"
        endchar = "│"
        for a in line:
            if str(a)[-8:-1] == (END_OF_LINE_CHAR):
                pass
            else:
                print(startchar + f"{str(a)[0:-1]:^{LINE_LENGTH}}"+endchar)
        print("└" + "─"*LINE_LENGTH +"┘")
    a_type = args.type
    myArgsParse(a_type)
