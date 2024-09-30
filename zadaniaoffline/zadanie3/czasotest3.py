# testy kodu
import random
import math


def dominates(point1, point2):
    if point1[0] > point2[0] and point1[1] > point2[1]:
        return 1
    return 0


def points_dominated(P, point):
    dominated = 0
    for i in range(0, len(P)):
        if dominates(point, P[i]):
            dominated += 1
    return dominated


def gen_example(n, size):
    P = [()]*n
    #print(P)
    for i in range(0, n):
        P[i] = (random.randint(0, size), random.randint(0, size))
    return P


def solve_example(P):
    l = len(P)
    max_d = 0
    P.sort()
    c_p = P[l - 1]
    max_d = points_dominated(P, P[l - 1])
    for i in range(l - 2, -1, -1):
        if not dominates(c_p, P[i]):
            dominated = 0
            for j in range(i, -1, -1):
                if dominates(P[i], P[j]):
                    dominated += 1
            if dominated > max_d:
                max_d = dominated
            c_p = P[i]
    return max_d


def probabilistic_solve(P):
    max_d = 0
    l = len(P)
    max_c = 0
    new_p = [0] * l
    for i in range(0, l):
        check = P[i][0] * P[i][1]
        if check > max_c:
            max_c = check
        new_p[i] = check

    log_l = math.log(l, 10)
    percentage = (l-log_l)/l
    #print(percentage)
    #max_c = percentage*max_c
    for i in range(0, l):
        if max_c <= new_p[i]:  # samo max_c tez dziala xddd
            dominated = 0
            for j in range(0, l):
                if dominates(P[i], P[j]):
                    dominated += 1
            if dominated > max_d:
                max_d = dominated

    return max_d


example = gen_example(10000, 10000)
#print(example)
print(solve_example(example))
print(probabilistic_solve(example))

ts = 0
for i in range(1, 101):
    example = gen_example(10, 100)
    good_solution = solve_example(example)
    probable_solution = probabilistic_solve(example)
    if good_solution == probable_solution:
        ts += 1
    print(f"Test {i}: RA: {good_solution}  PA: {probable_solution}")
print(f"Zgodnych odpowiedzi: {ts} na 100")

new_t = []
for i in range(0, 100):
    for j in range(0, 100):
        new_t.append(i*j)
new_t.sort()
print(new_t)

wt = 0
st = 20001
max_ab_r = 0
max_od_r = 0
for i in range(1, 101):
    for j in range(0, st):
        if random.randint(0, 1) % 2 == 0:
            wt += 1
    ab_r = abs(wt - st//2)
    od_r = ab_r/(st//2)
    if ab_r > max_ab_r:
        max_ab_r = ab_r
        max_od_r = od_r
    print(wt, abs(wt - st//2), abs(wt - st//2)/(st//2))
    wt = 0

print(max_ab_r, max_od_r*100)
