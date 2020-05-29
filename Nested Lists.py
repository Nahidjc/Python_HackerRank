N=int(input())
Main=[]
for i in range(N):
    list=[]
    name = input()
    score = float(input())
    list.append(name)
    list.append(score)
    Main.append(list)
nl=[]
for i in range(N):
    nl.append(Main[i][1])
sor=[]
sor=sorted(nl)
slow=sor[0]
for i in range(N):
    if sor[i]>slow:
        ch=sor[i]
        break
pr=[]
for i in range(N):
    for j in range(2):
        if Main[i][1]==ch:
            pr.append(Main[i][0])
        break
pr.sort()
for i in range(len(pr)):
  print(pr[i])








