#TextEditingFunctions
def rls(text):
    #RemoveLeadingSpaces - homemade function from my "nohow" package
    letter = False
    i = 0
    while letter == False:
        if not text[i] == " ":
            letter = True
        else:
            i += 1
    chunk = text[0:i]
    rem = text[i:len(text)]
    return rem
def cfp(text):
    textr = rls(text)
    #ChopFormatPrint - homemade function from my "nohow" package
    if len(textr) > 78:
        i = 78
        space = False
        while space == False:
            if textr[i] == " ":
                space = True
            else:
                i -= 1
        chunk = textr[0:i]
        rem = textr[i+1:len(textr)]
        print(rls(chunk))
        cfp(rem)
    else:
        print(rls(textr))
