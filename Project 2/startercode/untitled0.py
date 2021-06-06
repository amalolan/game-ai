# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:45:00 2017

@author: Malolan
"""
from Grid_3 import Grid
def neighbours(pos):
    if pos == [0,0]:
        return [[1,(1,0)],[3,(0,1)]]
    elif pos == [0,3]:
        return [[1,(1,3)],[2,(0,2)]]
    elif pos == [3,0]:
        return [[0,(2,0)],[3,(3,1)]]
    elif pos == [3,3]:
        return [[0,(2,3)],[2,(3,2)]]
    elif pos == [0,2] or pos == [0,1]:
        a = pos[1] - 1
        b = pos[1] + 1
        c = pos[1]
        return [[2,(0,a)],[3,(0,b)],[1,(1,c)]]
    elif pos == [1,0] or pos == [2,0]:
        a = pos[0] - 1
        b = pos[0] + 1
        c = pos[0]
        return [[0,(a,0)],[1,(b,0)],[3,(c,1)]]
    elif pos == [3,2] or pos == [3,1]:
        a = pos[1] - 1
        b = pos[1] + 1
        c = pos[1]
        return [[2,(3,a)],[3,(3,b)],[0,(2,c)]]
    elif pos == [1,3] or pos == [2,3]:
        a = pos[0] - 1
        b = pos[0] + 1
        c = pos[0]
        return [[0,(a,3)],[1,(b,3)],[2,(c,2)]]
    else :
        a = pos[0] - 1
        b = pos[0] + 1
        c = pos[0]
        A = pos[1] - 1
        B = pos[1] + 1
        C = pos[1]
        return [[0,(a,C)],[1,(b,C)],[2,(c,A)],[3,(c,B)]]
def h1(state):
    """
    This is the monotonicity heuristic
    """
    val = 0
    Board = {}
    for a in range(4):
        for b in range(4):
            Val = state.getCellValue([a,b])
            Board[(a,b)] = Val 
    Max = max(Board,key = Board.get)
    direction = ''
    if Max[0] <= 1:
        direction += '1'
    else :
        direction += '0'
    if Max[1] <= 1: 
        direction += '3'
    else:
        direction += '2'
            
    for i in range(4):
        for j in range(4):
            for x in neighbours([i,j]):
                P = Board[(i,j)]
                X = Board[x[1]]
                if x[0] == int(direction[0]) or x[0] == int(direction[1]):
                    if X < P:
                        if X != 0 or P != 0:
                            val += 1    
    return val   

def h2(state):
        """
        This is the smoothness heuristic
        """
        val = 0
        Board = {}
        for a in range(4):
            for b in range(4):
                Val = state.getCellValue([a,b])
                Board[(a,b)] = Val 
        for i in range(4):
            for j in range(4):
                for x in neighbours([i,j]):
                    P = Board[(i,j)]
                    X = Board[x[1]]
                    if P!= 0 or X!= 0:
                        val += abs(P-X)
        return val
def h12(state):
        """
        Returns a tuple of h1 and h2 vals
        """
        val = 0
        Value = 0
        Board = {}
        for a in range(4):
            for b in range(4):
                Val = state.getCellValue([a,b])
                Board[(a,b)] = Val 
        Max = max(Board,key = Board.get)
        direction = ''
        if Max[0] <= 1:
            direction += '1'
        else :
            direction += '0'
        if Max[1] <= 1: 
            direction += '3'
        else:
            direction += '2'
                
        for i in range(4):
            for j in range(4):
                for x in neighbours([i,j]):
                    P = Board[(i,j)]
                    X = Board[x[1]]
                    if x[0] == int(direction[0]) or x[0] == int(direction[1]):
                        if X < P:
                            if X != 0 or P != 0:
                                val +=1   
                    if P!= 0 or X!= 0:
                        Value += abs(P-X)           
        return val , Value                   


g = Grid()
g.map[0][0] = 1024
g.map[1][0] = 512
g.map[2][0] = 256
g.map[0][1] = 512
g.map[1][1] = 512
g.map[2][1] = 128
g.map[0][2] = 256
g.map[0][3] = 128

 
for J in (g.getAvailableMoves()):
    g = Grid()
    g.map[0][0] = 1024
    g.map[1][0] = 512
    g.map[2][0] = 256
    g.map[0][1] = 512
    g.map[1][1] = 512
    g.map[2][1] = 128
    g.map[0][2] = 256
    g.map[0][3] = 128
    g.move(J)
    for i in g.map:
        print(i) 
    print(h1(g) - h2(g) , h1(g) , h2(g) , h12(g))     


