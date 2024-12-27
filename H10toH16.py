def h10toh16(n):
    if n>0:
        sd=n%16
        n=n//16
        h10toh16(n)
        if sd==10: sd="A"
        elif sd == 11: sd = "B"
        elif sd == 12: sd = "C"
        elif sd==13: sd="D"
        elif sd==14: sd="E"
        elif sd==15: sd="F"
        print(sd, end='')
n=317547
h10toh16(n)