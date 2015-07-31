# -*- coding: utf-8 -*-
import numpy as np

def random_MFF(FZ,DP):
    # Sestavi naključno MFF matriko, število funkcijskih zahtev FZ, delovnih principov DP
    diagonal = np.identity(4, dtype=float)

    while True:
        dp = 0
        while dp < DP:
            rand_z = np.random.rand(4)
            rand_0_1 = np.where(rand_z > 0.75, 1, 0)
            rand_0_2 = np.where(rand_z > 0.95, 2, 1)
            random = rand_0_1 * rand_0_2
            del_prin = random*diagonal
            if del_prin[0,0]:
                del_prin.put([(0,0)],1)
                
            for fz in range(FZ-1):
                rand_z = np.random.rand(4)
                rand_0_1 = np.where(rand_z > 0.75, 1, 0)
                rand_0_2 = np.where(rand_z > 0.95, 2, 1)
                random = rand_0_1 * rand_0_2
                celica = random*diagonal
                if celica[0,0]:
                    celica.put([(0,0)],1)
                del_prin = np.concatenate((del_prin,celica), axis=0)

            # Pregleda, ce je v del_prin vsaj ena vrednost razlicna od 0
            # - torej ce vsak delovni princip izpolnjuje vsaj eno funkcijo 
            while True:              
                if np.count_nonzero(del_prin) == 0:
                    break
                else:
                    dp += 1
                    # Ce je to prvi od delovnih principov z njim začne matriko, ce ne
                    # doda trenutni del_prin k obstojeci matriki
                    if dp == 1:
                        matrika = del_prin
                    else:
                        matrika = np.concatenate((matrika,del_prin), axis=1)
                    break

        # Preveri, ce je pri vsaki funkcijski zahtevi vsaj ena vrednost
        # razlicna od 0 - ce so vse funkcijske zahteve izpolnjene
        for i in range(FZ):
            funkcija_i = matrika.take(range(4*i, 4*i+4),axis=0) #VZAME 4ZAPOREDNE VRSTICE - ENO FUNKCIJSKO ZAHTEVO
            if np.count_nonzero(funkcija_i) == 0:
                break
        else:
            break

    return matrika

if __name__ == '__main__':
    print (random_MFF(3,3))
