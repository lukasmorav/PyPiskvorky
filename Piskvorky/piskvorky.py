import pygame, sys
import numpy as np

pygame.init()

#Konstanty
VYSKA = 600
SIRKA = 600
VELIKOST_POLICKA = 200
SIRKA_CARY = 15

BG_BARVA = (28, 170, 156)
BARVA_CARY = (23, 145, 135)

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
    

#Main loop
priprav_pole()
hrac = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mysX = event.pos[0]
            mysY = event.pos[1]

            radek = int(mysX // VELIKOST_POLICKA)
            sloupec = int(mysY // VELIKOST_POLICKA)

            if je_volne_policko(radek, sloupec):
                if hrac == 1:
                    oznac_policko(radek, sloupec, hrac)
                    hrac = 2
                elif hrac == 2:
                    oznac_policko(radek, sloupec, hrac)
                    hrac = 1



    pygame.display.update()