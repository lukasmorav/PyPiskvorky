def pridejStudenta():
    jmeno = ''
    while jmeno == '':
        jmeno = input("Zadej jmeno studenta: ")
    studenti.append(jmeno)

    znamkyH = []
    if predmety.count() != 0:
        for predmet in predmety:
            while True:
                znamka = input("Zadej znamku z předmětu %s: " %predmet)
                if ['1','2','3','4','5'].__contains__(znamka):
                    break
            znamkyH.append(int(znamka))
    znamky.append(znamkyH)

def pridejPredmet():
    predmet = ''
    while predmet == '':
        predmet = input("Zadej zkratku předmětu: ")
    predmety.append(predmet)


studenti=[]
predmety=[]
znamky=[]

while True:
    vstup = input("Co chcete udělat? (Student/Předmět/Tabulka) ")

    if vstup.lower() == 'k':
        break
    elif vstup.lower() == 's':
        pridejStudenta()
    elif vstup.lower() == 'p':
        pridejPredmet()
    