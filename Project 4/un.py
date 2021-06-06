# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 10:59:58 2017

@author: Malolan
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:27:07 2017

@author: Malolan
"""



class cspd(object):
    """
    Uses domain to function
    """    
    def __init__(self,string):
        
        self.squares = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
        self.units = eval(open('stuff.txt','r').read())
        self.neigh = eval(open('stuff1.txt','r').read())
        self.domain = self.domainize(string)
    def domainize(self,s):
        def values(grid):
            C = [c for c in grid if c in D or c in '0.']
            return dict(zip(self.squares, C))
        dom = {}
        D = '123456789'
        for i in self.squares :
            dom[i] = D
        d = values(s)
        for i in self.squares:
            if d[i] != '0':
                dom[i] = d[i]       
        return dom      
    def make_str(self,domain):
        string = ''
        for d in self.squares:
            dm = domain[d]
            if len(dm) == 1:
                string+=dm
            else:
                string += '0'
        return string        
    def __str__(self):
        string = self.make_str(self.domain)
        returning = ''
        for s in range(len(string)):
            if s%9 == 0:
                if s != 0:
                    returning+= '\n'
            if string[s] == '0':
                returning += '-'
            else:
                returning += string[s]
            returning += ' '
            
        return returning        
            
    def move(self,cell,value):
        dmn = self.domain.copy()
        dmn[cell] = value
        new = cspd(self.make_str(dmn))
        if not cellDiff(new,cell):
            return False
        else:
            return new

def cellDiff(grid,cell):
    total = ''
    for n in grid.neigh[cell]:
        dn = grid.domain[n]
        if len(dn) == 1:
            total += dn
        else:
            total+='0'
    if grid.domain[cell] in total:
        return False
    else:
        return True        
def getArcs(grid):
    arcs = []
    for G in grid.squares:
        neigh = grid.neigh[G]
        for n in neigh:
            arcs.append((G,n))
    return arcs        
    
def ac3(grid):
    queue = Arcs[:]
    while len(queue) != 0:
        xi,xj = queue.pop() 
        if revise(grid,xi,xj):
            cd = grid.domain[xi]
            if len(cd) ==0:
                return False
            neigh = grid.neigh[xi]
            for xk in neigh:
                if xk != xj:
                    queue.append((xk,xi))
    return True            
                
def remove(string,i):
    return string[:i]+string[i+1:]

def revise(grid,xi,xj):
    di = grid.domain[xi]
    dj = grid.domain[xj]
    revised = False
    for d in range(len(di)):
        flag = True
        for D in dj:
            if di[d] != D:
                flag = False
        if flag:        
            grid.domain[xi] = remove(di,d)
            revised = True
    return revised        
            

def solve(grid):
    return bts(grid)        
        

def bts(csp):
    domain = csp.domain
    squares= csp.squares
    if all(len(domain[s]) == 1 for s in squares): 
        return csp
    n,var = getmin(domain,squares)
    
    for value in domain[var]:
        newcsp = csp.move(var,str(value))
        if newcsp!= False:            
            if inferences(newcsp,var,value)== True:
                result = bts(newcsp)
                if result != False:
                    return result
    return False   
                

def inferences(csp,var,value):
    return ac3(csp)


def getmin(domain,squares):
    """
    """
    lis = []
    for s in squares:
        sv = domain[s]
        if len(sv) > 1:
            lis.append((len(sv),s))
    return min(lis)

import sys
args = sys.argv
b = args[1]  
B1 = cspd(b)
Arcs = []         
Arcs = getArcs(B1) 
         
def main(b):     
    B1 = cspd(b)     
    print(b)
    o = open('output.txt','w+')
    o.close()
    if ac3(B1):
        if all(len(B1.domain[s]) == 1 for s in B1.squares):
            solution = B1.make_str(B1.domain)
            print(solution)
            o = open('output.txt','w+')
            o.write(solution)
            o.close()
        else:
            s = solve(B1)
            try:
                solution = s.make_str(s.domain)
                print(solution)
                o = open('output.txt','w+')
                o.write(solution)
                o.close() 
                print()
            except AttributeError:
                print('Failed')
                
              
    else:
            print('failure')    
J = ['000000000302540000050301070000000004409006005023054790000000050700810000080060009',
'500400070600090520003025400000000067000014800800600000005200000300007000790350000',
'000000000047056000908400061000070090409000100000009080000000007000284600302690005',
'000000000000530041600412005900000160040600002005200000000103200000005089070080006',
'090060000004000006003000942000200000086000200007081694700008000009510000050000073',
'000070360301000000042000008003006400004800002000003100005080007200760000000300856',
'000102900103097000009000070034060800000004500500021030000400000950000000000015307',
'800000090075209080040500100003080600000300070280005000000004000010027030060900020',
'000002008401006007002107903007000000065040009004000560000001000008000006910080070',
'006029000400006002090000600200005104000000080850010263000092040510000000000400800',
'000000000010720000700014826000000000006000900041906030050001000020097680000580009',
'005100026230009000000000000000900800590083000006500107060000001004000008853001600',
'680400000000710009013000000800000300000804090462009000000900037020007108000000026',
'000900007020007061300810002000078009007300020100040000000000050005000003010052078',
'000000060000130907900200031002000000004501703010006004046000020000010000200605008',
'000000000000002891080030507000000000047001085006427003000000000030005070719000204',
'010050000362010005070206400000005070005090600900000000700001008000374900601000000',
'000001086076300502000009300007000060900000800054000207008035900030900000000407000',
'307009000000003060006400001003100094025040803060300002000000006000200900580000040',
'021000050000000708000400020000600035060000000083020600059002086030001000006904200']     
for j in J: 
    main(j)            