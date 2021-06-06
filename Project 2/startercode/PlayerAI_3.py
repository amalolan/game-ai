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
        self.limit = 0.095
        self.depthLimit = depthLimit
        self.mL = []
        self.dict = {}
        self.h = {}
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
            state = stateTup[0]
            maxDepth = self.depthLimit
            if stateTup[1] == maxDepth:
                val = self.h.get(str(state.map))
                if val == None:
                    Val = Eval(state)
                    self.h[str(state.map)] = Val
                    return Val
                else:
                    return val
            elif len(stateTup[0].getAvailableMoves()) == 0:
                val = self.h.get(str(state.map))
                if val == None:
                    Val = Eval(state)
                    self.h[str(state.map)] = Val
                    return Val
                else:
                    return val

        def Eval(state):
            """
            This is the eval function which combines many heuristics and assigns
            weights to each of them
            Returns a single value
            """

            H1 = htest2(state)
            return H1


        def htest2(state):
            score1 = 0
            score2 = 0
            r = 0.5
            Path1 = [[3,0],[3,1],[3,2],[3,3],[2,3],[2,2],[2,1],[2,0],
                    [1,0],[1,1],[1,2],[1,3],[0,3],[0,2],[0,1],[0,0]]
            Path2 = [[3,0],[2,0],[1,0],[0,0],[0,1],[1,1],[2,1],[3,1],
                     [3,2],[2,2],[1,2],[0,2],[0,3],[1,3],[2,3],[3,3]]
            for n in range(16):
                if n%3 == 0:
                    self.emergency()
                cell1 = state.getCellValue(Path1[n])
                cell2 = state.getCellValue(Path2[n])
                score1 += (cell1) * (r**n)
                score2 += (cell2) * (r**n)
            MAX = state.getMaxTile()
            if state.getCellValue(Path1[0]) != MAX:
                score1 = (score1)/MAX
                score2 = (score2)/MAX

            return max(score1,score2)


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
            Map =  self.dict.get(str(state.map))
            if Map == None:
                children = []
                for M in range(4):
                    g = state.clone()
                    if g.move(M):
                        children.append(g)
                self.dict[str(state.map)] = children
            else:
                children = Map
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
            Map= self.dict.get(str(state.map))
            if Map == None:
                cells= state.getAvailableCells()
                children = []
                tiles = [2,4]
                for i in cells:
                    for j in tiles:
                        g = state.clone()
                        g.insertTile(i,j)
                        children.append(g)
                self.dict[str(state.map)] = children
            else:
                children = Map
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

        self.dict = {}
        self.h = {}
        self.prevTime = time.clock()
        self.depthLimit = 1
        self.mL = []
        self.over = False
        while self.over == False:
            self.depthLimit +=1
            try :
                self.mL.append(decision(grid))

            except KeyError:
                print(self.depthLimit)
                return self.mL[-1]
            except IndexError:
                return random.randint(0,3)
            self.Alarm(time.clock())
        return self.mL[-1]



