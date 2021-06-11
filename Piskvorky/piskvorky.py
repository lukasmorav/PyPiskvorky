import pygame, sys
import numpy as np

pygame.init()

#Konstanty
VYSKA = 600
SIRKA = 600
VELIKOST_POLICKA = 200
SIRKA_CARY = 15
KOLECKO_R = 60
KOLECKO_T = 15
KRIZEK_T = 25
MEZERA = 55

BG_BARVA = (28, 170, 156)
BARVA_CARY = (23, 145, 135)
BARVA_KOLECKA = (239, 231, 200)
BARVA_KRIZKU = (66, 66, 66)

#Hlavni okenko
screen = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption('PISKVORKY')
screen.fill(BG_BARVA)

pole = np.zeros( (3, 3) )

#Funkce
def priprav_pole():
    #horizontální čáry
    pygame.draw.line(screen, BARVA_CARY, (0, VELIKOST_POLICKA), (SIRKA, VELIKOST_POLICKA), SIRKA_CARY)
    pygame.draw.line(screen, BARVA_CARY, (SIRKA, 2 * VELIKOST_POLICKA), (0, 2 * VELIKOST_POLICKA), SIRKA_CARY)
    #vertikalní čáry
    pygame.draw.line(screen, BARVA_CARY, (VELIKOST_POLICKA, 0), (VELIKOST_POLICKA, VYSKA), SIRKA_CARY)
    pygame.draw.line(screen, BARVA_CARY, (2 * VELIKOST_POLICKA, 0), (2 * VELIKOST_POLICKA, VYSKA), SIRKA_CARY)

def update_pole ():
    for radek in range(3):
        for sloupec in range(3):
            if pole[radek][sloupec] == 1:
                pygame.draw.circle( screen, BARVA_KOLECKA, (int(sloupec * VELIKOST_POLICKA + VELIKOST_POLICKA//2), int(radek * VELIKOST_POLICKA + VELIKOST_POLICKA//2)), KOLECKO_R, KOLECKO_T)
            elif pole[radek][sloupec] == 2:
                pygame.draw.line( screen, BARVA_KRIZKU, (sloupec * VELIKOST_POLICKA + MEZERA, (radek + 1) * VELIKOST_POLICKA - MEZERA), ((sloupec + 1) * VELIKOST_POLICKA - MEZERA, radek * VELIKOST_POLICKA + MEZERA), KRIZEK_T)
                pygame.draw.line( screen, BARVA_KRIZKU, (sloupec * VELIKOST_POLICKA + MEZERA, radek * VELIKOST_POLICKA + MEZERA), ((sloupec + 1) * VELIKOST_POLICKA - MEZERA, (radek + 1) * VELIKOST_POLICKA - MEZERA), KRIZEK_T)

def zkontroluj_vyhru(hrac):
    for radek in range(3):
        if pole[radek][0] == hrac and pole[radek][1] == hrac and pole[radek][2] == hrac:
            draw_vyhra_vodorovna(radek, hrac)
            return True

    for sloupec in range(3):
        if pole[0][sloupec] == hrac and pole[1][sloupec] == hrac and pole[2][sloupec] == hrac:
            draw_vyhra_svisla(sloupec, hrac)
            return True
    
    if pole[0][0] == hrac and pole[1][1] == hrac and pole[2][2] == hrac:
        draw_uhlopricka_L(hrac)
        return True

    if pole[2][0] == hrac and pole[1][1] == hrac and pole[0][2] == hrac:
        draw_uhlopricka_P(hrac)
        return True

    return False

def oznac_policko(radek, sloupec, hrac):
    pole[radek][sloupec] = hrac

def je_volne_policko(radek, sloupec):
    return pole[radek][sloupec] == 0

def je_pole_zaplnene():
    for radek in range(3):
        for sloupec in range(3):
            if pole[radek][sloupec] == 0:
                return False
    return True

def draw_vyhra_vodorovna(radek, hrac):
    if hrac == 1:
        barva = BARVA_KOLECKA
    else:
        barva = BARVA_KRIZKU
    
    radekY = radek * VELIKOST_POLICKA + VELIKOST_POLICKA//2

    pygame.draw.line(screen, barva, (15, radekY), (SIRKA - 15, radekY), SIRKA_CARY)

def draw_vyhra_svisla(sloupec, hrac):
    if hrac == 1:
        barva = BARVA_KOLECKA
    else:
        barva = BARVA_KRIZKU

    sloupecX = sloupec * VELIKOST_POLICKA + VELIKOST_POLICKA//2
    pygame.draw.line(screen, barva, (sloupecX, 15), (sloupecX, VYSKA - 15), SIRKA_CARY)

def draw_uhlopricka_L(hrac):
    if hrac == 1:
        barva = BARVA_KOLECKA
    else:
        barva =  BARVA_KRIZKU
    
    pygame.draw.line(screen, barva, (15,15), (SIRKA - 15, VYSKA - 15), SIRKA_CARY)

def draw_uhlopricka_P(hrac):
    if hrac == 1:
        barva = BARVA_KOLECKA
    else:
        barva =  BARVA_KRIZKU
    
    pygame.draw.line(screen, barva, (15, VYSKA - 15), (SIRKA - 15, 15), SIRKA_CARY)

#Main loop
priprav_pole()
hrac = 1
vyhra = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not vyhra:
            mysX = event.pos[0]
            mysY = event.pos[1]

            sloupec = int(mysX // VELIKOST_POLICKA)
            radek = int(mysY // VELIKOST_POLICKA)

            if je_volne_policko(radek, sloupec):
                oznac_policko(radek, sloupec, hrac)
                if zkontroluj_vyhru(hrac):
                    vyhra = True
                


                
                hrac = hrac % 2 + 1

              


    update_pole()
    pygame.display.update()