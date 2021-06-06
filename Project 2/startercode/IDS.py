# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 16:42:46 2017

@author: Malolan
"""
from BaseAI_3 import BaseAI
import time
import random

depthLimit = 3
actionDic = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT",
    '0': "UP",
    '1': "DOWN",
    '2': "LEFT",
    '3': "RIGHT"
    
}
#prune = 0
#pruneLog = []


class PlayerAI(BaseAI):
    
    def __init__(self):
        self.over = False
        self.limit = 0.097
        self.depthLimit = 0
        self.mL = []
        
    def emergency(self):
        self.Alarm(time.clock())
        if self.over:
            raise KeyError
        
    def Alarm(self, currTime):
            if currTime - self.prevTime > self.limit:
                self.over = True   
   
                
    def getMove(self, grid):
        """
        Returns the move made by the PlayerAI
        0 - Up , 1- Down, 2- Left, 3- Right
        """
#        global prune
#        prune = 0
        def Terminal(stateTup):
            """
            Checks if the node is a terminal node
            Returns eval(state) if it is terminal
            """
#            global depthLimit
            maxDepth = self.depthLimit
            if stateTup[1] == maxDepth:
                return Eval(stateTup[0])
            elif len(stateTup[0].getAvailableMoves()) == 0:
                return Eval(stateTup[0])
                    
        def Eval(state):
            """
            This is the eval function which combines many heuristics and assigns
            weights to each of them
            Returns a single value
            """
#            H12 = h12(state)
#            H3 = h3(state)
            H1 = htest2(state)
#            w1 = 4
#            w2 = 1/64
#            Dict = {0:20,1:15,2:10,3:7,4:0,5:0}
            return (H1)# -(H12[1]*w2)-(Dict[H3])
 
            
        def htest1(state):
            grid = state.map
            return (4 * grid[0][0]) + (2 * grid[0][1]) + (2 * grid[1][0]) + grid[0][2]+ grid[1][1] + grid[2][0]
            
        def htest2(state):
            score1 = 0
            score2 = 0
            r = 0.5
            Path1 = [[3,0],[3,1],[3,2],[3,3],[2,3],[2,2],[2,1],[2,0],
                    [1,0],[1,1],[1,2],[1,3],[0,3],[0,2],[0,1],[0,0]][::-1]
            Path2 = [[3,0],[2,0],[1,0],[0,0],[0,1],[1,1],[2,1],[3,1],
                     [3,2],[2,2],[1,2],[0,2],[0,3],[1,3],[2,3],[3,3]]      
            for n in range(16):
                if n%3 == 0:
                    self.emergency()
                cell1 = state.getCellValue(Path1[n])
                cell2 = state.getCellValue(Path2[n])
                score1 += (cell1) * (r**n)
                score2 += (cell2) * (r**n)
            return max(score1,score2)  
        def neighbours(pos):
            """
            Returns all the neighbours of a position on the board
            Returns a list of the direction of a neighbouring cell and
            the neighbouring cell
            """
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
        def h12(state):
            """
            Returns a tuple of h1 and h2 vals
            """
            Value = 0
            Board = {}
            for a in range(4):
                for b in range(4):
                    Val = state.getCellValue([a,b])
                    Board[(a,b)] = Val 
            D = {'13':0,'12':0,'03':0,'02':0}
            for direction in D:
                val = 0
                for i in range(4):
                    for j in range(4):
                        for x in neighbours([i,j]):
                            P = Board[(i,j)]
                            X = Board[x[1]]
                            if x[0] == int(direction[0]) or x[0] == int(direction[1]):
                                if X < P:
                                    if X != 0 or P != 0:
                                        val +=1   
                            if P!= 0 or X!= 0 and direction == '13':
                                Value += abs(P-X)    
                D[direction] = val            
                            
            return D[max(D,key = D.get)] , Value           
        def h3(state):
            """
            Free Spaces Heuristic
            """
            val = 0
            cells = state.getAvailableCells()
            if len(cells) < 5:
                val += len(cells)
            return val    
            
        def Maximize(stateTup,A,B):
            """
            Returns a tuple of state,eval(state)
            Takes in a stateTup(tuple of grid + depth of the grid), alpha, 
            and beta
            """
            self.emergency()
            t = Terminal(stateTup)
            if t != None:
                return (None, t)
            
            maxChild , maxUtility = None,-999999999
            state = stateTup[0]
            g = state.clone()
            children = []
            for M in range(4):
                if g.move(M):
                    children.append(g)
                g = state.clone()
            for child in children:
                childTup = (child,stateTup[1]+1)
                utility = Minimize(childTup,A,B)[1]
                if utility > maxUtility:
                    maxChild , maxUtility = child , utility
                if maxUtility >= B:
#                    global prune
#                    prune +=1
                    break
                if maxUtility > A:
                    A = maxUtility
                    
            return (maxChild,maxUtility)
            
            
        def Minimize(stateTup,A,B):
            """
            Returns a tuple of state,eval(state)
            Takes in a stateTup(tuple of grid + depth of the grid), alpha, 
            and beta
            """
            self.emergency()
            t = Terminal(stateTup)
            if t != None:
                return (None, t)
            
            minChild , minUtility = None,999999999
            state = stateTup[0]
            children = []
            cells= state.getAvailableCells()
            tiles = [2,4]
            for i in cells:
                for j in tiles:
                    g = state.clone()
                    g.insertTile(i,j)
                    children.append(g)
            for child in children:
                childTup = (child,stateTup[1]+1)
                utility = Maximize(childTup,A,B)[1]
                if utility < minUtility:
                    minChild , minUtility = child , utility
                if minUtility <= A:
#                    global prune
#                    prune +=1
                    break
                if minUtility < B:
                    B = minUtility
                    
            return (minChild,minUtility)
            
        
            
        def decision(grid):
            """
            Decision function which returns the move which led to the state
            """
            child = Maximize((grid,0),-999999999,999999999)[0]
            Child = child.map
            g = grid.clone()
            for M in range(4):
                if g.move(M):
                    if g.map == Child:
    #                    global prune
    #                    global pruneLog
    #                    pruneLog.append(prune)
    #                    print(prune)
    #                    print(sum(pruneLog)/len(pruneLog))
                        return M
                    g = grid.clone()    
                    
        self.prevTime = time.clock()
        self.depthLimit = 1
        self.mL = []
        self.over = False
        while self.over == False:
            self.depthLimit +=1
            try :
                self.mL.append(decision(grid))

            except KeyError:
                return self.mL[-1]
            except IndexError:
                return random.randint(0,3)
            self.Alarm(time.clock())
        return self.mL[-1]    
            
                        
                            
            