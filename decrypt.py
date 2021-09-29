def decryption(private,list):
    d, n = private
    x = ''
    for i in list:
        if (i == 400):
            x += ' '
        else:
            m = (int(i) ** d) % n
            m += 65
            c = chr(m)
            x += c

    return x