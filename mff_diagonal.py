# -*- coding: utf-8 -*-
import numpy
from math import *
from random_MFF import random_MFF

def uredi_MFF(MFF):
    """Funkcija, ki uredi podano matriko MFF.
    INPUT:
        MFF == uporabnikova matrika funkcij in funkcionalnosti
    OUTPUT:
        MFF_sorted == urejena matrika MFF
    """
    
    # Stevilo funkcijskih zahtev in delovnih principov:
    fz = MFF.shape[0]/4
    dp = MFF.shape[1]/4

    # Razcleni matriko MFF na posamezne funkcijske zahteve / delovne principe
    def razcleni_vrstice(matrika, visina):
        seznam = []
        for i in range(int(matrika.shape[0]/visina)):    #visina pove, koliko vrstic je visok en zeljen radelek (ena fz)
            funkcija_i = matrika.take(range(visina*i, visina*i+visina),axis=0) #VZAME 4ZAPOREDNE VRSTICE - ENO FUNKCIJSKO ZAHTEVO
            seznam.append(funkcija_i)   # doda posamezne funkcijske zahteve seznamu
        return seznam

    def razcleni_stolpce(matrika, sirina):
        seznam = []
        for i in range(int(dp)):
            dp_i = matrika.take(range(sirina*i, sirina*i+sirina),axis=1) #VZAME 4ZAPOREDNE STOLPCE - EN DELOVNI PRINCIP
            seznam.append(dp_i)   #doda posamezne delovne principe seznamu 
        return seznam

    FZ = razcleni_vrstice(MFF,4) # Funkcijske zahteve bodo v seznamu FZ od indeksa 0 naprej (FZ(0), FZ(1)...)
    DP = razcleni_stolpce(MFF,4) # Delovni principi bodo v seznamu DP od indeksa 0 naprej

    # Ce posamezne funkcijske zahteve razclenimo po stolpcih dobimo seznam vseh celic 4x4
    def razcleni_celice(matrika, size):     #size je velikost celice (4x4 celica -> size = 4)
        tabela = []
        for i in razcleni_vrstice(matrika, size):
            tabela.append(razcleni_stolpce(i, size))
        return tabela

    celice = razcleni_celice(MFF,4)
    # celice so zdaj shranjene v 2D seznamu "celice" - naprimer prva je na mestu celice[0][0],
    # zadnja na mestu celice[fz-1][dp-1] - ker se indeksi zacnejo z 0

    # Vsako polje 4x4 nadomestimo z utežno vrednostjo glede na vsebino,
    # shranimo v ustrezno polje v mariki fz x dp

    def CellToC(seznam_celic,i,j):   #funkcija ki pretvori celico 4x4 v vrednost C
        c = numpy.zeros(4)
        for k in range(4):
                c.put(k, seznam_celic[i][j][k,k])
        w = [100., 400., 800., 1300.]
        if not c.any(): 
            C = 0
        else:
            C = (w[0]*c[0]+w[1]*c[1]+w[2]*c[2]+w[3]*c[3])/(sqrt(c[0])+sqrt(c[1])+sqrt(c[2])+sqrt(c[3]))
        return C

    MFF_C = numpy.zeros((fz,dp),dtype=float)
    for i in range(int(fz)):
        for j in range(int(dp)):
            MFF_C.put(dp*i+j, CellToC(celice,i,j))

    # Aritmetična sredina vrednosti iz posamezne vrstice = vrednost vrstice
    # Aritmetična sredina vrednosti iz posameznega stolpca = vrednost stolpca
    vrednosti_FZ = MFF_C.sum(axis=1)/(MFF_C != 0).sum(axis=1)
    vrednosti_DP = MFF_C.sum(axis=0)/(MFF_C != 0).sum(axis=0)

    FZ_sort_i = numpy.argsort(vrednosti_FZ) # indeksi funkcijskih zahtev, urejeni po veilkosti utežne vrednosti
    DP_sort_j = numpy.argsort(vrednosti_DP) # indeksi delovnih principov, -||-

    FZ_sorted_array = numpy.array(FZ)[FZ_sort_i] # matrika funkcijskih zahtev, urejena po velikosti utežne funkcije

    # Iz te matrike spet tvorimo celoten MFF, ga razdelimo po stolpcih na DP in
    # stolpce uredimo glede na urejene indekse DP_sort_j
    MFF_FZ_sorted = numpy.concatenate((FZ_sorted_array), axis=0)
    DP_sorted_array = numpy.array(razcleni_stolpce(MFF_FZ_sorted,4))[DP_sort_j] # urejena matrika DP

    # Dobljen seznam urejenih DP združimo nazaj v urejeno matriko MFF
    MFF_sorted = numpy.concatenate((DP_sorted_array), axis=1)
    return MFF_sorted

if __name__ == '__main__':
    from mff_vnos import matrika_MFF
    #MFF = matrika_MFF()
    MFF = random_MFF(3,4, 0.3, 0.05)
    urejena_MFF = uredi_MFF(MFF)
    print ("Izvorna matrika MFF:\n\n",MFF,"\n\n")
    print ("Urejena matrika MFF:\n\n",urejena_MFF,"\n")
