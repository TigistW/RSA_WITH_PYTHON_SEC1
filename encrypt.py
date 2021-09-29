def encryption(public, message):
    e,n = public
    x = []
    for i in message:
        print(x)
        if (i.isupper()):
            m = ord(i) - 65
            c = (m ** e) % n
            x.append(c)
        elif (i.islower()):
            m = ord(i) - 97
            c = (m ** e) % n
            x.append(c)
        elif (i.isspace()):
            spc=400
            x.append(spc)
        else:
            m = ord(i)
            c = (m ** e) % n
            x.append(c)
    return x


