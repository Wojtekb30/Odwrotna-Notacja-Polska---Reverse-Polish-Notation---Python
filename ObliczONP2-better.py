def Licz(stos, dlugosc):
    while True:
        a=2
        b=0
        print(stos)
        while a<=dlugosc-1:
            if stos[a]=='+' or stos[a]=='-' or stos[a]=='*' or stos[a]=='/':
                if stos[a]=='+':
                    b=int(stos[a-2])+int(stos[a-1])
                elif stos[a]=='-':
                    b=int(stos[a-2])-int(stos[a-1])
                elif stos[a]=='*':
                    b=int(stos[a-2])*int(stos[a-1])
                elif stos[a]=='/':
                    b=int(stos[a-2])//int(stos[a-1])
                stos[a-2]=str(b)
                stos[a-1]='r'
                stos[a]='r'
                break
            a=a+1
        a=1
        c=0
        blokada = 0
        print(stos)
        while a<=dlugosc-1:
            if stos[a]=='r':
                c=c+1
                blokada = blokada+1
            else:
                stos[a-c]=stos[a]
                if a!=c and blokada>0:
                    stos[a] = 'r'
                #print(stos)
            a=a+1
        a = 0
        licznik = 0
        while a<=dlugosc-1:
            if stos[a]=='r':
                licznik = licznik + 1
            if licznik == dlugosc - 1:
                return stos[0]
            a=a+1


rownanie = str(input("Wpisz dzialanie w ONP: "))
stos = rownanie.split(' ')
dlugosc = len(stos)
print(Licz(stos, dlugosc))