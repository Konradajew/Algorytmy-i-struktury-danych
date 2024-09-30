"""
Konrad Sz

Na prostą logikę jeżeli weźmiemu ilosc okregow na fundusze prosty dynamik i pomnozymy razy liczbe
wyborow to wszystko jest cycus glancus pizdeczka i to działa
Ten pomysl wielokrotnie wystepuje w tych wszystkich dynamikach bo sa w huj proste
zlozonosc nnmp to natomiast sortowanie topologiczne z jakimis ograniczeniami (mamy acykliczny graf skierowany)
"""


from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None
""" koncepcja bez dokladnej implementacji
def wybory(T):
    e1 = T[0]
    funds = e1.fundusze
    n = len(T)
    F = [[0 for _ in range(funds)] for _ in range(n)]
    F[0][0] = 0
    for i in range(0, n):
        for j in range(0, funds):
            F[i][j] = max(F[i-1][j], F[i-1][j-koszt]+wyborcy)

    return 0"""

def wybory(T):
    votes = 0
    for w in T:
        n = 1
        funds = w.fundusze
        T = []
        while w.next:
            T.append((w.wyborcy, w.koszt))
            n += 1
            w = w.next
        T.append((w.wyborcy, w.koszt))
        #print(n, funds, T)
        F = [[0 for _ in range(funds+1)] for _ in range(n)]
        F[0][T[0][1]] = T[0][0]
        for i in range(0, n):
            wyborcy = T[i][0]
            koszt = T[i][1]
            for j in range(0, funds+1):  #trzeba od zera, aby w kazdej lini przepisalo minimalna liczbe wydatkow bo to cos zmienia czesto
                F[i][j] = max(F[i][j], F[i-1][j])
                if j - koszt > -1:
                    F[i][j] = max(F[i-1][j-koszt]+wyborcy, F[i][j], wyborcy)
        votes += max(F[n-1])
        #for r in F:
        #    print(r)
        #print()

    return votes

runtests(wybory, all_tests = True)