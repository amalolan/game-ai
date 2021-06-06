# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:27:07 2017

@author: Malolan
"""
import sys
args = sys.argv
b = args[1]

i=0
domain = {}
class board(object):
    def __init__(self,sudokuGrid):
        """
        sudokuGrid is a string of all each cell
        """
        assert type(sudokuGrid) == str , 'Please input a string of the grid'
        self.gridstr = sudokuGrid
        self.grid = self.dictize(sudokuGrid)
        initializeDomain(self)
        
    def dictize(self,grid):
        """
        Creates a dictionary representation from a string
        """
        gridDict = {}
        d = {}
        sufList = ['A','B','C','D','E','F','G','H','I']
        for suffix in range(len(sufList)):
            gridDict[sufList[suffix]] =grid[suffix*9:(suffix+1)*9] 
            for i in range(9):
                d[sufList[suffix]+str(i+1)] = gridDict[sufList[suffix]][i]
        return d
        
    def update(self,cell,value,legal = False):
#        MAP = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9}
#        i = MAP[cell[0]]*int(cell[1])
        if not legal:
#            self.gridstr = self.gridstr[:i-1] +value + self.gridstr[i:]
            self.grid[cell] = value
        else:
            prevVal = self.getCellValue(cell)
            self.grid[cell] = value
            if not cellDiff(self,cell):
                self.grid[cell] = prevVal
                raise ValueError('This insertion is not legal.Undoing insertion')
            else:  
#                self.gridstr = self.gridstr[:i-1] +value + self.gridstr[i:]
                self.grid[cell] = value
                         
    def move(self,cell,value,legal = False):
#        MAP = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9}
#        i = MAP[cell[0]]*int(cell[1])
        if not legal:
            prevVal = self.getCellValue(cell)
#            return board(self.gridstr[:i-1] +value + self.gridstr[i:])
            self.grid[cell] = value
            new = board(self.make_str())
            self.grid[cell] = prevVal
            return new
        else:
            prevVal = self.getCellValue(cell)
            self.grid[cell] = value
            if not cellDiff(self,cell):
                self.grid[cell] = prevVal
                return False
            else:    
                new = board(self.make_str())
                self.grid[cell] = prevVal
                return new
            
                 
    def getCellValue(self,cell):
        return self.grid[cell]
    
    def getGrid(self,string = False):
        if not string:
            return self.grid.copy()
#        else:
#            return self.gridstr
    
    
    def getRow(self,cell,s=True):
        """
        Takes in a cell, ex: A1
        If s == True,Returns a string of that row including the cell
        Else returns the dict kkeys of the whole row
        """
        if s:
            g = self.grid
            string = ''
            for G in g.keys():
                if G[0] == cell[0]:
                    string += g[G]
                    if G[1] == '9':
                        return string
        else:
            g = self.grid
            string = []
            for G in g.keys():
                if G[0] == cell[0]:
                    string.append(G)
                    if G[1] == '9':
                        return string            
                
    def getColumn(self,cell,s=True):
        """
        Takes in a cell, ex: A1
        If s == True,Returns a string of that column including the cell
        Else returns the dict keys of the whole column
        """    
        if s:
            g = self.grid
            string = ''
            for G in g.keys():
                if G[1] == cell[1]:
                    string+=g[G]
                    if G[0] == 'I':
                        return string
        else:
            g = self.grid
            string = []
            for G in g.keys():
                if G[1] == cell[1]:
                    string.append(G)
                    if G[0]=='I':
                        return string
    def getSquare(self,cell,s=True): 
        """
        Takes in a cell, ex: A1
        If s == True,Returns a string of that 3x3 square including the cell
        Else returns the dict keys of the whole square
        """     
        if s:
            MAP = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9}
            c = ''
            g = self.grid
            string = ''
            c += str(MAP[cell[0]]-1)
            c+=str(int(cell[1])-1)
            if int(c[0])//3 == 0:
                if int(c[1])//3 == 0:
                    string+=g['A1']+g['A2']+g['A3']+g['B1']+g['B2']+g['B3']
                    string+=g['C1']+g['C2']+g['C3']
                    return string
                elif int(c[1])//3 == 1:
                    string+=g['A4']+g['A5']+g['A6']+g['B4']+g['B5']+g['B6']
                    string+=g['C4']+g['C5']+g['C6']
                    return string
                elif int(c[1])//3 == 2:
                    string+=g['A7']+g['A8']+g['A9']+g['B7']+g['B8']+g['B9']
                    string+=g['C7']+g['C8']+g['C9']
                    return string
            elif int(c[0])//3 ==1:
                if int(c[1])//3 == 0:
                    string+=g['D1']+g['D2']+g['D3']+g['E1']+g['E2']+g['E3']
                    string+=g['F1']+g['F2']+g['F3']
                    return string
                elif int(c[1])//3 == 1:
                    string+=g['D4']+g['D5']+g['D6']+g['E4']+g['E5']+g['E6']
                    string+=g['F4']+g['F5']+g['F6']
                    return string
                elif int(c[1])//3 == 2:
                    string+=g['D7']+g['D8']+g['D9']+g['E7']+g['E8']+g['E9']
                    string+=g['F7']+g['F8']+g['F9']
                    return string
            elif int(c[0])//3 == 2:
                if int(c[1])//3 == 0:
                    string+=g['G1']+g['G2']+g['G3']+g['H1']+g['H2']+g['H3']
                    string+=g['I1']+g['I2']+g['I3']
                    return string
                elif int(c[1])//3 == 1:
                    string+=g['G4']+g['G5']+g['G6']+g['H4']+g['H5']+g['H6']
                    string+=g['I4']+g['I5']+g['I6']
                    return string
                elif int(c[1])//3 == 2:
                    string+=g['G7']+g['G8']+g['G9']+g['H7']+g['H8']+g['H9']
                    string+=g['I7']+g['I8']+g['I9']
                    return string
                
                
        else:
            MAP = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9}
            c = ''
            g = self.grid
            c += str(MAP[cell[0]]-1)
            c+=str(int(cell[1])-1)
            if int(c[0])//3 == 0:
                if int(c[1])//3 == 0:
                    string =  ['A1','A2','A3','B1','B2','B3',
                               'C1','C2','C3']
                    return string
                elif int(c[1])//3 == 1:
                    string =  ['A4','A5','A6','B4','B5','B6',
                               'C4','C5','C6']
                    return string
                elif int(c[1])//3 == 2:
                    string =  ['A7','A8','A9','B7','B8','B9',
                               'C7','C8','C9']
                    return string
            elif int(c[0])//3 ==1:
                if int(c[1])//3 == 0:
                    string =  ['D1','D2','D3','E1','E2','E3',
                               'F1','F2','F3']
                    return string
                elif int(c[1])//3 == 1:
                    string =  ['D4','D5','D6','E4','E5','E6',
                               'F4','F5','F6']
                    return string
                elif int(c[1])//3 == 2:
                    string =  ['D7','D8','D9','E7','E8','E9',
                               'F7','F8','F9']
                    return string
            elif int(c[0])//3 == 2:
                if int(c[1])//3 == 0:
                    string =  ['G1','G2','G3','H1','H2','H3',
                               'I1','I2','I3']
                    return string
                elif int(c[1])//3 == 1:
                    string =  ['G4','G5','G6','H4','H5','H6',
                               'I4','I5','I6']
                    return string
                elif int(c[1])//3 == 2:
                    string =  ['G7','G8','G9','H7','H8','H9',
                               'I7','I8','I9']
                    return string
                
    def getCellDomain(self,cell):
        global domain
        DOMAIN = domain[self.gridstr]
        if DOMAIN.get(cell) == None:
            if self.getCellValue(cell) == '0':
                Domain = ['1','2','3','4','5','6','7','8','9']
                returning = []
                for d in Domain:
                    try:
                        self.update(cell,d,True)
                        returning.append(d)
                        self.update(cell,'0')
                    except ValueError:
                        a=1
                        a+=1
                if len(returning) == 1:
                    self.update(cell,returning[0])
                DOMAIN[cell] = returning
                return returning
            else:
                DOMAIN[cell] = [self.getCellValue(cell)]
                return [self.getCellValue(cell)]
        else:
            return DOMAIN.get(cell)
    def Domain(self,cell):
        global domain
        
        try:
            D = domain[self.gridstr].get(cell)
        except KeyError:
            initializeDomain(self)
            D = domain[self.gridstr].get(cell)
        if len(D) == 1:
            self.update(cell,D[0])
        return D    
    def complete(self,legal=False):
        """
        Checks if the board is solved
        """
        self.make_str()
        if '0' not in self.gridstr:
            if legal:
                return allDiff(self)
            else:
                return True
        else:
            return False
        
    def neighbours(self,cell):
        """
        Returns all the unique neighbours
        """
        row = self.getRow(cell,False)
        column = self.getColumn(cell,False)
        square = self.getSquare(cell,False)
        neigh = set(row+column+square)
        neigh.discard(cell)
        return neigh
        
                
    def diff(self,c1,c2):
        """
        Checks if the two cells are different
        Returns True if different and False otherwise
        """
        if self.getCellValue(c1) == self.getCellValue(c2):
            return False
        else:
            return True
        
    def make_str(self):
        g=['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
        string = ''
        for G in g:
            string+=self.grid[G]
        self.gridstr = string
        return string    
    def __str__(self):
        g=self.grid
        string = ''
        for G in g.keys():
            if g[G] == '0':
                string+='-'    
            else:    
                string += g[G]
            string+=' '
            if G[1] == '9':
                string+= '\n' 
        return string
    
def cellDiff(grid,cell):
    """
    Takes in a board object and a cell
    Returns True if the cell satisfies all the rules of sudoku
    Returns False otherwise    
    """
    
    cv = grid.getCellValue(cell)
    if cv == '0':
        raise ValueError('You have given an empty cell')
    else:
        neigh = grid.neighbours(cell)
        total = ''
        for n in neigh:
            total += grid.getCellValue(n)
        if cv in total:
            return False
        else:
            return True
def allDiff(grid):
    """
    Takes in a whole board object
    Returns True if the whole board is legal
    False otherwise
    """
    g = grid.getGrid()
    for G in g:
        if g[G]!= '0':
            if not cellDiff(grid,G):
                return False
    return True        

def getArcs(grid):
    g = grid.getGrid()
    arcs = []
    for G in g:
        neigh = grid.neighbours(G)
        for n in neigh:
            arcs.append((G,n))
    return arcs        

def ac3(grid):
    queue = getArcs(grid)
    while len(queue) != 0:
        xi,xj = queue.pop() 
        if revise(grid,xi,xj):
            cd = grid.Domain(xi)
            if len(cd) ==0:
                return False
            neigh = grid.neighbours(xi)
            neigh.discard(xj)
            for xk in neigh:
                queue.append((xk,xi))
    return True            
                
            
def revise(grid,xi,xj):
    di = grid.Domain(xi) 
    dj = grid.Domain(xj)
    revised = False
    for d in di:
        flag = True
        for D in dj:
            if d != D:
                flag = False
        if flag:        
            di.remove(d)
            revised = True
    return revised        
            
def initializeDomain(grid):
    global domain
    domain[grid.make_str()] = {}
    for g in grid.getGrid():
        grid.getCellDomain(g)

def solve(grid):
    return bts(grid)        
        

def bts(csp):
    squares= csp.getGrid().keys()
    if csp.complete():
        return csp.make_str()
    n,var = getmin(csp,squares)
    if var == False:
        return csp.make_str()
    for value in orderdomain(var,csp):
        newcsp = csp.move(var,value)
        if newcsp!= False:            
            if inferences(newcsp,var,value)== True:
                global domain
                domain = {}
                N = board(newcsp.make_str())
                result = bts(N)
                if result != False:
                    return result
    return False           
                
                
def orderdomain(var,csp):
    return csp.Domain(var)

def inferences(csp,var,value):
    return ac3(csp)


def getmin(csp,squares):
    """
    """
    lis = []
#    values = csp.domain
    for s in squares:
        sv = csp.Domain(s)
        if len(sv) > 1:
            lis.append((len(sv),s))
    try:
        return min(lis)
    except ValueError:
        return False,False

o = open('output1.txt','w+')
o.close()
import time
problems = []
f = open('sudokus_start.txt','r')
j = f.read()
J=j.split('\n')
problems = J.copy()   
start = time.time()       
for b in J:
              
                       
     
    B1 = board(b)    
    print(b)
        #print(ac3(B1))
        #print(B1.make_str())
    
    if ac3(B1):
        if B1.complete():
            o = open('output1.txt','a+')
            o.write('\n'+B1.make_str())
            o.close()
        else:
#            print(B1.make_str())
            B2 = board(B1.make_str())
            domain.pop(b)
            solution = solve(B2)
            print(solution)
            o = open('output1.txt','a+')
            o.write('\n'+solution)
            o.close()
    else:
        print('failure')      
        
end = time.time()
print(end-start)        