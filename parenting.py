t=int(input())
#t=1
for k in range(t):
    jobs=""
    tasks=[]
    C=0
    J=0
    n=int(input())
    for i in range(n):
        start,end=[int(x) for x in (input().split())]
        tasks.append([start,i,0])
        tasks.append([end,i,1])
    tasks=sorted(tasks,key=lambda x:x[0])
    active=[]
    #print(tasks)
    time=0
    for x in range(len(tasks)):
        task=tasks[x]
        if(task[2]==0):
            if(C==0):
                time=task[0]
                C=1
                jobs=jobs+"C"
                active.append(["C",task[1]])
                tasks[x].append("C")
                #print("ACTIVE LIST:",active)
            elif(J==0):
                time=task[0]
                J=1
                jobs=jobs+"J"
                active.append(["J",task[1]])
                tasks[x].append("J")
                #print("ACTIVE LIST:",active)
            else:
                jobs="IMPOSSIBLE"
                #print(jobs)
                break
        else:
            for element in active:
                if(element[1]==task[1]):
                    if(element[0]=="C"):
                        C=0
                    else:
                        J=0
                    active.remove(element)
                 #   print("Removed:",active)
    tasks=sorted(tasks,key=lambda x:x[1])
    print("Case #",k+1,end=':')
    if(jobs=="IMPOSSIBLE"):
        print(jobs,end='')
    else:
        print(tasks)
        for a in range(0,len(tasks),2):
            print(tasks[a][3],end='')
    #print("Case #",k,":",jobs)
    #jobs=''
    print()
