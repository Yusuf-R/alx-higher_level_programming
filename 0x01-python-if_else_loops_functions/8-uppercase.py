def upper_case(str):
    for x in range(0, len(str)):
        if (ord(str[x]) >= 97) and (ord(str[x]) <= 122):
            lower = True
        else:
            lower = False
        print("{}".format((chr(ord(str[x]) - 32)) if lower else
              str[x]), end="")
   print("")
