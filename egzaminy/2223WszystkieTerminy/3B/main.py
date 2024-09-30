"""
Tutaj lekka listość, bo 2 pkt za n^2 xddddd jeszcze 1 za poprawnosci i testy wow
nawet nic nie tlumacze bo nie ma co
"""
from egz3btesty import runtests

def uncool( P ):
    n = len(P)
    for i in range(0, n):
        for j in range(i+1, n):
            a, b = P[i]
            x, y = P[j]
            if a < x < b < y or x < a < y < b:
                return (i,j)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True)

#solution 2 nlogn

def uncool2( P ):
    n = len(P)
    #sortuje przedzialy wzgledem punktu startowego
