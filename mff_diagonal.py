# -*- coding: utf-8 -*-
import numpy
from random_MFF import random_MFF

MFF = random_MFF(3,4)
print MFF, "\n"

# Stevilo funkcijskih zahtev in delovnih principov:
fz = MFF.shape[0]/4
dp = MFF.shape[1]/4


# Razcleni matriko MFF na posamezne funkcijske zahteve / delovne principe
def razcleni_vrstice(matrika):
    seznam = []
    for i in range(matrika.shape[0]/4):
        funkcija_i = matrika.take(range(4*i, 4*i+4),axis=0) #VZAME 4ZAPOREDNE VRSTICE - ENO FUNKCIJSKO ZAHTEVO
        seznam.append(funkcija_i)   # doda posamezne funkcijske zahteve seznamu
    return seznam

def razcleni_stolpce(matrika):
    seznam = []
    for i in range(dp):
        dp_i = matrika.take(range(4*i, 4*i+4),axis=1) #VZAME 4ZAPOREDNE STOLPCE - EN DELOVNI PRINCIP
        seznam.append(dp_i)   #doda posamezne delovne principe seznamu 
    return seznam

FZ = razcleni_vrstice(MFF) # Funkcijske zahteve bodo v seznamu FZ od indeksa 0 naprej (FZ(0), FZ(1)...)
DP = razcleni_stolpce(MFF) # Delovni principi bodo v seznamu DP od indeksa 0 naprej

# Ce posamezne funkcijske zahteve razclenimo po stolpcih dobimo seznam vseh celic 4x4
celice = []
for i in FZ:
    celice.append(razcleni_stolpce(i))
    # celice so zdaj shranjene v 2D seznamu "celice" - naprimer prva je na mestu celice[0][0],
    # zadnja na mestu celice[fz-1][dp-1] - ker se indeksi zacnejo z 0

for i in range(fz):
    for j in range(dp):
        print celice[i][j],"\n"
