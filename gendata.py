from sympy import sympify

vars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', #'I', 
'J', 'K', 'L', 'M', #'N', 'O', 
'P', 'Q', 'R', #'S', 
'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'alpha', 'b', #'beta', 
'c', 'chi', 'd', 'delta', 'e',
'epsilon', 'eta', 'f', 'g', #'gamma',
'h', 'i', 'iota', 'j', 'k', 'kappa', 'l', 'lamda',
'm', 'mu', 'n', 'nu', 'o', 'omega', 'omicron',
'p', 'phi', 'pi', 'psi', 'q', 'r', 'rho', 's', 'sigma',
't', 'tau', 'theta', 'u', 'upsilon',
'v', 'w', 'x', 'xi', 'y', 'z', #'zeta'
] + list(map(str, range(11)))

#vars = [getattr(l, x) for x in vars]+ list(map(sympify, (map(str, range(11)))))
vars = list(map(str, vars))

from itertools import combinations
import re

def formatting(string):
    return string.replace(',', ' ,').replace('(','( ').replace(')',' )').replace('\'','')

def strsimp(mvf, j, xl, wl):
    return ([xl.lower() + " " + wl.lower() + ', '.join(j), mvf + " " + formatting(str(j))])

def pstrsimp(mvf, j, xl, wl):
    retval = strsimp(mvf, j, xl, wl)
    print(' => '.join(retval))
    #try:   # For Checking if sympify works ?
    #    sympify(retval[-1])
    #except:
    #    input()
    return retval

standardUse = ["What be the", "Find the"] # followed by 'of'
trickyUse = []
dictOfFuncs = {
    #'sum': ["Sum", "Total", "Aggregate"],
    'Min': {
        'params': 'Multi',
        'useCase': 'Standard',
        'alternates': ["Minimum", "Min", "Smallest"]
        },
    'Max': {
        'params': 'Multi',
        'useCase': 'Standard',
        'alternates': ["Maximum", "Max", "Greatest", "Biggest"]
    }
    # et.al
}

for i in range(2, 4):
    for j in combinations(vars, i):
        for fn, k in dictOfFuncs.items():
            if k['useCase'] == 'Standard':
                use = standardUse
            elif k['useCase'] == 'Tricky':
                use = trickyUse
            for xl in use:
                for wl in k['alternates']:
                    (pstrsimp(fn, j, xl, wl + " of "))
