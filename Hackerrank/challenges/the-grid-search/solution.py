#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gridSearch function below.
def gridSearch(G, P):
    r = len(P)
    c = len(P[0])
    
    def checkMatch(i, j):
        for n, row in enumerate(G[i:i+r]):
            if row[j:j+c] != P[n]:
                return False
        return True
    
    for i in range(len(G) - (r-1)):
        for j in range(len(G[0]) - (c-1)):
            if checkMatch(i, j):
                return 'YES'
    return 'NO'

if __name__ == '__main__':
    actual_results = []
    with open('input05.txt', 'r') as f:
        lines = f.readlines()

    t = int(lines.pop(0))

    for t_itr in range(t):
        RC = lines.pop(0).split()
        R = int(RC[0])
        C = int(RC[1])
        G = []
        for _ in range(R):
            G.append(lines.pop(0).strip())
        rc = lines.pop(0).split()
        r = int(rc[0])
        c = int(rc[1])
        P = []
        for _ in range(r):
            P.append(lines.pop(0).strip())
        actual_results.append(gridSearch(G, P))

    with open('output05.txt', 'r') as f:
        expected_results = [line.rstrip() for line in f]
    if actual_results == expected_results:
        print('PASS')
    else:
        print('FAIL')
        print('Actual: %s' % actual_results)
        print('Expected: %s' % expected_results)
