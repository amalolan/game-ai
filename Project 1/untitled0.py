#import sys
#from collections import deque
#import time
#import random
#import queue
#import heapq
#import itertools
#
#sys.setrecursionlimit(2900)
#args = sys.argv
#B=list(args[2])  
#a=''    
#for i in B:
#    a+=i
#
#depthDict={}
#Len=0
#
#class ParentBoard(object):
#    def __init__(self,board,n):
#        self.board = board
#        self.n=n
#    
#    def getBoard(self):
#        return self.board
#    
#    def getn(self):
#        return self.n
#        
#    
#    
#    def isLegal(self,move):
#        
#        n=self.n
#        b=self.board.split(',')
#        if move == 'U':
#            if b.index('0')< n:
#                return False
#            else:
#                return True
#        elif move == 'D':
#            if b.index('0') >= n**2 - n:
#                return False
#            else:
#                return True
#        elif move == 'L':
#            if b.index('0') % n == 0:
#                return False
#            else:
#                return True
#        elif move =='R':
#            if b.index('0') % n == n-1:
#                return False
#            else :
#                return True
#    
#    def Move(self,move):
#        """
#        Returns a moved board
#        """
#        n=self.n
#        b=self.board.split(',')
#        i = b.index('0')  
#        if move == 'U':
#            I=i-n
#        elif move ==  'D':
#            I=i+n
#        elif move == 'L':
#            I=i-1
#        elif move == 'R':
#            I=i+1           
#        moving = b[I] 
#        b[I] = '0'
#        b[i] = moving
#        Board=''
#        for j in b:
#            Board+=j
#            Board+=','
#        Board=Board[:-1]    
#        return Board    
#            
#        return Board    
#    def isGoal(self,goal):
#        if self.board == goal:
#            return True
#        else:
#            return False
#            
#    def legalMoves(self):
#        m=[]
#        if self.isLegal('U'):
#            m.append('U')
#        if self.isLegal('D'):
#            m.append('D')
#        if self.isLegal('L'):
#            m.append('L')
#        if self.isLegal('R'):
#            m.append('R')
#        return m 
#    
#    def dist(self,i,b):
#        """
#        takes in a cell on the board and finds the manhattan distance of the 
#        object to the goal.
#        """
#        ind = b.index(i)
#        n=self.n
#        goal=[]
#        for j in range(self.getn()**2):
#            goal.append(str(j))
#        Ind =goal.index(i)
#        return abs((Ind%n)-(ind%n)) + abs((Ind//n) - (ind//n))       
#        
#        
#    def getVal(self):
#        val=0
#        b= self.board.split(',')
#        for i in b:
#            if i != '0':
#                val+=self.dist(i,b)
#        return val    
#            
#            
#    def parents(self,l=set([])):
#        return l
#        
#    def path(self,p=''):
#        return p
#    def depth(self):
#        global depthDict
#        depthDict[self.getBoard()]=0
#        return 0
#        
#        
#class ChildBoard(ParentBoard):
#     def __init__(self,board,parent,move,n):
#         self.board = board
#         self.parent = parent
#         self.move = move  
#         self.n=n
#         
#        
#     def parents(self,l=set([])):
#         l.add(self.parent.getBoard())
#         return self.parent.parents(l)
#        
#     def depth(self):         
#         global depthDict
#         D=depthDict.get(self.parent.getBoard())
#         if D != None:
#             depthDict[self.getBoard()] = D+1
#             return D+1
#         else:
#             return self.parent.depth()
#             
#     def path(self,p=''):
#         
#         p+=self.move         
#         return self.parent.path(p)
#
#def ast(board):
#    """
#    Takes in a parent board(ONLY!!)
#    Uses A* search to return a list of values in order
#    """  
#    assert type(board) == ParentBoard , 'Please provide a Parent Board.'
#    global depthDict
#    depthDict[board.getBoard()] = 0
#    counter = itertools.count()
#    start = time.time()
#    frontier = {}
#    frontier[board.getBoard()]=[board.getVal(),0,next(counter),board]
#    fe=set([])
#    fringeLen = set([])
#    goal=''
#    nodes=0
#    for i in range(board.getn()**2):
#        goal+=str(i)
#        goal+=','
#    goal = goal[:-1]   
#    
#    while len(frontier) != 0:
#        fringeLen.add(len(frontier))
#        state = frontier.pop(min(frontier,key=frontier.get))[-1]
#        fe.add(state.getBoard())
#        if state.isGoal(goal):
#            fringe = len(frontier)
#            path=state.path()
#            depth = state.depth()
#            end = time.time()
#            time1 = end-start
#            ram = 0.7593999
#            returning = [path[::-1],nodes,depth,0,max(fringeLen),fringe,
#                         round(time1,8),ram] 
#            print(returning)             
#            return returning
#        nodes+=1
#        legal = state.legalMoves()
#        for m in legal:
#            new = state.Move(m)
#            if new not in fe:
#                New =ChildBoard(new,state,m,state.getn())
#                DEPTH = New.depth()
#                fe.add(new)
#                if m == 'U':
#                    mV=0.1
#                elif m =='D':
#                    mV=0.2
#                elif m=='L':
#                    mV=0.3
#                elif m=='R':
#                    mV=0.4
#                frontier[new] = [New.getVal()+DEPTH+mV,next(counter),New]
#            elif new in frontier:
#                New =ChildBoard(new,state,m,state.getn())
#                DEPTH = New.depth()
#                val=New.getVal()+DEPTH
#                if m == 'U':
#                    mV=0.1
#                elif m =='D':
#                    mV=0.2
#                elif m=='L':
#                    mV=0.3
#                elif m=='R':
#                    mV=0.4
#                val ==mV    
#                if int(frontier[new][0])>int(val):
#                    frontier[new]=[val,next(counter),New]
#
#                
#                    
#                    
#            
#                
#                
#            
#        
#        
#        
#        
#def bfs(board):
#    """
#    Takes in a parent board(ONLY!!)
#    Uses breadth-first search to return a list of values in order
#    """
#    assert type(board) == ParentBoard , 'Please provide a Parent Board.'
#    global depthDict
#    depthDict[board.getBoard()] = 0
#    start = time.time()     
#    frontier = deque([board])
#    fe=set([])
#    fringeLen = set([])
#    nodes=0
#    goal=''
#    for i in range(board.getn()**2):
#        goal+=str(i)
#        goal+=','
#    goal = goal[:-1]    
#        
#    while len(frontier) != 0:
#        fringeLen.add(len(frontier))
#        state = frontier.popleft()            
#        fe.add(state.getBoard())
#        if state.isGoal(goal):
#            fringe=len(frontier)
#            path=state.path()
#            depth = state.depth()
#            end = time.time()
#            time1 = end-start
#            ram = 0.7593999
#            return[path[::-1],nodes,depth,0,max(fringeLen),fringe,round(time1,8),ram]
#        nodes+=1
#        legal = state.legalMoves()
#        for m in legal:
#            new = state.Move(m)
#            if new not in fe:
#                New =ChildBoard(new,state,m,state.getn())
#                New.depth()
#                frontier.append(New)
#                fe.add(new)
#           
#
#                
#def dfs(board):
#    """
#    Takes in a parent board(ONLY!!)
#    Uses depth-first search to return a list of values in order
#    """        
#    assert type(board) == ParentBoard , 'Please provide a Parent Board.'
#    global depthDict
#    depthDict[board.getBoard()] = 0
#    start = time.time()     
#    frontier = [board]
#    fe=set([])
#    fringeLen = set([])
#    nodes=0
#    goal=''
#    for i in range(board.getn()**2):
#        goal+=str(i)
#        goal+=','
#    goal=goal[:-1]    
#    while len(frontier) != 0:
#        fringeLen.add(len(frontier))
#        state = frontier.pop()            
#        fe.add(state.getBoard())
#        if state.isGoal(goal):
#            fringe=len(frontier)
#            path=state.path()
#            depth = state.depth()
#            end = time.time()
#            time1 = end-start
#            ram = 0.7593999
#            returning = [path[::-1],nodes,depth,0,max(fringeLen),fringe,
#                         round(time1,8),ram]          
#            return returning
#        nodes+=1
#        legal = state.legalMoves()[::-1]
#        for m in legal:
#            new = state.Move(m)
#            if new not in fe:
#                New =ChildBoard(new,state,m,state.getn())
#                New.depth()
#                frontier.append(New)
#                fe.add(new)  
#         
#def output(l):
#    """
#    Takes in a list of the format:path,nodes,depth,maxDepth,max(fringeLen),
#    fringe,time1,ram
#    Edits output.txt
#    """        
#    f= open("output.txt","w+")
#    Path=l[0]
##    global A
##    if testBoard(A,Path).getBoard() == '0,1,2,3,4,5,6,7,8':
##        print(True)
##    else:
##        print(False)
#    path=[]
#    for i in Path:
#        if i == 'U':
#            path.append('Up')
#        elif i =='D':
#            path.append('Down')
#        elif i =='L':
#            path.append('Left')
#        elif i=='R':
#            path.append('Right')
#    d = max(depthDict.values())        
#    f.write("path_to_goal: " + str(path) + '\n' )      
#    f.write("cost_of_path: "+str(len(path))+ '\n')
#    f.write("nodes_expanded: "+str(l[1])+ '\n')
#    f.write("fringe_size: "+str(l[5])+ '\n')
#    f.write("max_fringe_size: "+str(l[4])+ '\n')
#    f.write("search_depth: "+str(l[2])+ '\n')
#    f.write("max_search_depth: "+str(d)+ '\n')
#    f.write("running_time: "+str(l[6])+ '\n')
#    f.write("max_ram_usage: "+str(l[7])+ '\n')        
#    f.close() 
#    
#
#def testBoard(b,moves):
#    if len(moves) == 1:
#        return ChildBoard(b.Move(moves[0][0]),b,moves[0][0],b.getn())
#    else:    
#        return testBoard(ChildBoard(b.Move(moves[0][0]),b,moves[0][0],b.getn()),
#                         moves[1:])
#                         
#
#
#
#
#n=int(len(a.split(','))**(1/2))
#def ranBoard(n):
#    a=''
#    b=[]
#    for x in range(n**2):
#        b.append(str(x))
#    for i in range(len(b[:])):
#        j=random.randint(0,len(b)-1)
#        k=b.pop(j)
#        a+=k
#        a+=','
#    return a[:-1]    
#    
#    
#    
#
##a=randBoard(3)
#A = ParentBoard(a,n)
#
#
#
#            
#if args[1] == 'bfs':
#    output(bfs(A))
#elif args[1] == 'dfs':
#    output(dfs(A))
#elif args[1] == 'ast':
#    output(ast(A))                        
##                        
#                       



import sys
from collections import deque
import time
import random
import heapq
import itertools

sys.setrecursionlimit(2900)
args = sys.argv
B=list(args[2])  
a=''    
for i in B:
    a+=i
kewl=0
depthDict={}
Len=0
valDict={}

class ParentBoard(object):
    def __init__(self,board,n):
        self.board = board
        self.n=n
    
    def getBoard(self):
        return self.board
    
    def getn(self):
        return self.n
        
    
    
    def isLegal(self,move):
        
        n=self.n
        b=self.board.split(',')
        if move == 'U':
            if b.index('0')< n:
                return False
            else:
                return True
        elif move == 'D':
            if b.index('0') >= n**2 - n:
                return False
            else:
                return True
        elif move == 'L':
            if b.index('0') % n == 0:
                return False
            else:
                return True
        elif move =='R':
            if b.index('0') % n == n-1:
                return False
            else :
                return True
    
    def Move(self,move):
        """
        Returns a moved board
        """
        n=self.n
        b=self.board.split(',')
        i = b.index('0')  
        if move == 'U':
            I=i-n
        elif move ==  'D':
            I=i+n
        elif move == 'L':
            I=i-1
        elif move == 'R':
            I=i+1           
        moving = b[I] 
        b[I] = '0'
        b[i] = moving
        Board=''
        for j in b:
            Board+=j
            Board+=','
        Board=Board[:-1]    
        return Board    
            
        return Board    
    def isGoal(self,goal):
        if self.board == goal:
            return True
        else:
            return False
            
    def legalMoves(self):
        m=[]
        if self.isLegal('U'):
            m.append('U')
        if self.isLegal('D'):
            m.append('D')
        if self.isLegal('L'):
            m.append('L')
        if self.isLegal('R'):
            m.append('R')
        return m 
    
    def dist(self,i,b):
        """
        takes in a cell on the board and finds the manhattan distance of the 
        object to the goal.
        """
        ind = b.index(i)
        n=self.n
        goal=[]
        for j in range(self.getn()**2):
            goal.append(str(j))
        Ind =goal.index(i)
        return abs((Ind%n)-(ind%n)) + abs((Ind//n) - (ind//n))        
        
        
    def getVal(self):
        global valDict
        if valDict.get(self.board) != None:
            return valDict.get(self.board)
        val=0
        b= self.board.split(',')
        for i in b:
            if i != '0':
                val+=self.dist(i,b)
        valDict[self.board] = val      
        return val    
            
            
    def parents(self,l=set([])):
        return l
        
    def path(self,p=''):
        return p
        
    def depth(self):
        global depthDict
        depthDict[self.getBoard()]=0
        return 0
    
    def getMoveVal(self):
        return 0
        
        
class ChildBoard(ParentBoard):
     def __init__(self,board,parent,move,n):
         self.board = board
         self.parent = parent
         self.move = move  
         self.n=n
     def getMoveVal(self):
         m=self.move
         if m == 'U':
             moveVal=1
         elif m =='D':
             moveVal=2
         elif m=='L':
             moveVal=3
         elif m=='R':
             moveVal=4
         return moveVal
        
     def parents(self,l=set([])):
         l.add(self.parent.getBoard())
         return self.parent.parents(l)
        
     def depth(self):         
         global depthDict
         D=depthDict.get(self.parent.getBoard())
         if D != None:
             depthDict[self.getBoard()] = D+1
             return D+1
         else:
             return self.parent.depth()
             
     def path(self,p=''):
         
         p+=self.move         
         return self.parent.path(p)
         
         
def ida(board):
    """
    Takes in a parent board(ONLY!!)
    Uses Iterative Deepening-A* search to return a list of values in order
    """
    def remove_Board(b,val,Check = True):
        if Check == True:
            entry = frontierboards.get(b.getBoard())
            if int(entry[0]) <= int(val):
                return False    
            entry = frontierboards.pop(b.getBoard())
            entry[-1]='REMOVED'
            return True
        else:
            try:
                entry = exploredboards.get(b.getBoard())
                if int(entry[0]) <= int(val):
                    return False 
                return True
            except TypeError:
                return True
        
        
    def add_Board(b,val,moveval,check=True):
        if check == True:  
            val +=(moveval)/100
            if frontierboards.get(b.getBoard()) != None:
                c=remove_Board(b,val)
                if c == False:
                    return None
                
                    
            count = next(counter)    
            entry = [val,count,b]
            frontierboards[b.getBoard()] = entry
            frontier.append(entry)
        else:
            if frontierboards.get(b.getBoard()) != None:
                add_Board(b,val,moveval)
            else:
                val += (moveval)/100
                c=remove_Board(b,val,False)
                if c == False:
                    return None
            count = next(counter)    
            entry = [val,count,b]
            exploredboards[b.getBoard()] = entry
            e.add(b.getBoard())
    
    def pop_Board():
        
        while True:
            b = frontier.pop()[-1]
            if b != 'REMOVED':
                del frontierboards[b.getBoard()]
                return b   
             
                
       
    def LenCheck(frontier):
        return len(frontierboards)
        
    assert type(board) == ParentBoard , 'Please provide a Parent Board.'
    global depthDict
    counter = itertools.count()
    start = time.time()
    a=board.getVal()-1
    fringeLen = set([])
    goal=''
    nodes=0
    
    for i in range(board.getn()**2):
        goal+=str(i)
        goal+=','
    goal = goal[:-1]    
      
    frontier = []
    frontierboards={}       
    while True:
        e=set([])
        exploredboards={}
        add_Board(board,board.getVal(),0)
        LMNO=LenCheck(frontier)    
        a+=1
        depthDict={}
        depthDict[board.getBoard()] = 0
        while LMNO != 0:
            
            LMNO = LenCheck(frontier)
            if LMNO == 0:
                break
            fringeLen.add(LMNO)
            state = pop_Board()
            add_Board(state,state.getVal()+state.depth(),state.getMoveVal(),False)
            if state.isGoal(goal):
                LMNO -=1
                fringe=LMNO
                path=state.path()
                depth = state.depth()
                end = time.time()
                time1 = end-start
                ram = 0.7593999
                returning = [path[::-1],nodes,depth,0,max(fringeLen),fringe,
                             round(time1,8),ram]          
                return returning
                
            nodes+=1
            legal = state.legalMoves()[::-1]
            for m in legal:    
                new = state.Move(m)   
                New =ChildBoard(new,state,m,state.getn())
                DEPTH1 = New.depth()
                val = New.getVal()+DEPTH1
                moveVal = New.getMoveVal()
                if int(val) <= int(a):
                    if new in e:
                        add_Board(New,val,moveVal,False)
                    else:
                        add_Board(New,val,moveVal)
                              
             
    




     
def ast(board):
    """
    Takes in a parent board(ONLY!!)
    Uses A* search to return a list of values in order
    """  
    
    
    def remove_Board(b,val):
        entry = frontierboards[b.getBoard()]
        if int(entry[0]) <= int(val):
            return False    
        entry = frontierboards.pop(b.getBoard())
        entry[-1]='REMOVED'
        return True
        
        
    def add_Board(b,val,moveval):
        val +=(moveval/100)
        if b.getBoard() in frontierboards:
            c=remove_Board(b,val)
            if c == False:
                return None
            
                
        count = next(counter)    
        entry = [val,count,b]
        frontierboards[b.getBoard()] = entry
        heapq.heappush(frontier,entry)
    
    def pop_Board():
        while True:
            b = heapq.heappop(frontier)[-1]
            if b != 'REMOVED':
                del frontierboards[b.getBoard()]
                return b    
       
    def LenCheck(frontier):
        return len(frontierboards)
        
    assert type(board) == ParentBoard , 'Please provide a Parent Board.'
    counter = itertools.count()
    global depthDict
    depthDict[board.getBoard()] = 0
    start = time.time()
    frontier = []
    frontierboards={}    
    add_Board(board,board.getVal(),0)
    e=set([])
    fringeLen = set([])
    goal=''
    nodes=0
    for i in range(board.getn()**2):
        goal+=str(i)
        goal+=','
    goal = goal[:-1]    
    LMNO=LenCheck(frontier)

    while LMNO != 0:
        LMNO = LenCheck(frontier)
        fringeLen.add(LMNO)
        state = pop_Board()        
        e.add(state.getBoard())
        if state.isGoal(goal):
            LMNO -=1
            fringe=LMNO
            path=state.path()
            depth = state.depth()
            end = time.time()
            time1 = end-start
            ram = 0.7593999
            returning = [path[::-1],nodes,depth,0,max(fringeLen),fringe,
                         round(time1,8),ram]            
            return returning
        nodes+=1
        legal = state.legalMoves()
        for m in legal:
            new = state.Move(m)            
            if new not in e:
                New =ChildBoard(new,state,m,state.getn())
                DEPTH1 = New.depth()
                moveVal=New.getMoveVal()
                add_Board(New,New.getVal()+DEPTH1,moveVal)
                
                
            
        
def bfs(board):
    """
    Takes in a parent board(ONLY!!)
    Uses breadth-first search to return a list of values in order
    """
    assert type(board) == ParentBoard , 'Please provide a Parent Board.'
    global depthDict
    depthDict[board.getBoard()] = 0
    start = time.time()     
    frontier = deque([board])
    fe=set([])
    fringeLen = set([])
    nodes=0
    goal=''
    for i in range(board.getn()**2):
        goal+=str(i)
        goal+=','
    goal = goal[:-1]    
        
    while len(frontier) != 0:
        fringeLen.add(len(frontier))
        state = frontier.popleft()            
        fe.add(state.getBoard())
        if state.isGoal(goal):
            fringe=len(frontier)
            path=state.path()
            depth = state.depth()
            end = time.time()
            time1 = end-start
            ram = 0.7593999
            return[path[::-1],nodes,depth,0,max(fringeLen),fringe,round(time1,8),ram]
        nodes+=1
        legal = state.legalMoves()
        for m in legal:
            new = state.Move(m)
            if new not in fe:
                New =ChildBoard(new,state,m,state.getn())
                New.depth()
                frontier.append(New)
                fe.add(new)
           

                
def dfs(board):
    """
    Takes in a parent board(ONLY!!)
    Uses depth-first search to return a list of values in order
    """        
    assert type(board) == ParentBoard , 'Please provide a Parent Board.'
    global depthDict
    depthDict[board.getBoard()] = 0
    start = time.time()     
    frontier = [board]
    fe=set([])
    fringeLen = set([])
    nodes=0
    goal=''
    for i in range(board.getn()**2):
        goal+=str(i)
        goal+=','
    goal=goal[:-1]    
    while len(frontier) != 0:
        fringeLen.add(len(frontier))
        state = frontier.pop()            
        fe.add(state.getBoard())
        if state.isGoal(goal):
            fringe=len(frontier)
            path=state.path()
            depth = state.depth()
            end = time.time()
            time1 = end-start
            ram = 0.7593999
            return[path[::-1],nodes,depth,0,max(fringeLen),fringe,round(time1,8),ram]
        nodes+=1
        legal = state.legalMoves()[::-1]
        for m in legal:
            new = state.Move(m)
            if new not in fe:
                New =ChildBoard(new,state,m,state.getn())
                New.depth()
                frontier.append(New)
                fe.add(new)  
         

def output(l):
    """
    Takes in a list of the format:path,nodes,depth,maxDepth,max(fringeLen),
    fringe,time1,ram
    Edits output.txt
    """        
    f= open("output.txt","w+")
    Path=l[0]
#    global A
#    if testBoard(A,Path).getBoard() == '0,1,2,3,4,5,6,7,8':
#        print(True)
#    else:
#        print(False)
    path=[]
    for i in Path:
        if i == 'U':
            path.append('Up')
        elif i =='D':
            path.append('Down')
        elif i =='L':
            path.append('Left')
        elif i=='R':
            path.append('Right')
    d = max(depthDict.values())        
    f.write("path_to_goal: " + str(path) + '\n' )      
    f.write("cost_of_path: "+str(len(path))+ '\n')
    f.write("nodes_expanded: "+str(l[1])+ '\n')
    f.write("fringe_size: "+str(l[5])+ '\n')
    f.write("max_fringe_size: "+str(l[4])+ '\n')
    f.write("search_depth: "+str(l[2])+ '\n')
    f.write("max_search_depth: "+str(d)+ '\n')
    f.write("running_time: "+str(l[6])+ '\n')
    f.write("max_ram_usage: "+str(l[7])+ '\n')        
    f.close() 
    

def testBoard(b,moves):
    if len(moves) == 1:
        return ChildBoard(b.Move(moves[0][0]),b,moves[0][0],b.getn())
    else:    
        return testBoard(ChildBoard(b.Move(moves[0][0]),b,moves[0][0],b.getn()),
                         moves[1:])
                         




n=int(len(a.split(','))**(1/2))
def ranBoard(n):
    a=''
    b=[]
    for x in range(n**2):
        b.append(str(x))
    for i in range(len(b[:])):
        j=random.randint(0,len(b)-1)
        k=b.pop(j)
        a+=k
        a+=','
    return a[:-1]    
    
    
    

#a=randBoard(3)
A = ParentBoard(a,n)



            
if args[1] == 'bfs':
    output(bfs(A))
elif args[1] == 'dfs':
    output(dfs(A))
elif args[1] == 'ast':
    output(ast(A))                        
elif args[1] == 'ida':
    output(ida(A))                        
                       