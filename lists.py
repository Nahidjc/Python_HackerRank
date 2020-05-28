n=int(input())
List=[]
for i in range(0,n):
      m=input().split(' ')
      s=m[0]
      if s=='insert':
          List.insert(int(m[1]),int(m[2]))
      elif s=='print':
         print(List)
      elif s=='remove':
         List.remove(int(m[1]))
      elif s=='append':
         List.append(int(m[1]))
      elif s=='sort':
         List.sort()
      elif s=='pop':
         List.pop()
      elif s=='reverse':
         List.reverse()

