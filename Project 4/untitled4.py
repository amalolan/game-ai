o = open('output1.txt','w+')
o.close()
import time
import un
problems = []
f = open('output.txt','r')
j = f.read()
J=j.split('\n')
problems =[]
problems.append(J.copy())  
start = time.time()   
problems = problems[0]    
for b in problems:
    print(b)
    un.main(b)
end = time.time()
print(end-start)    
