n = int(input())
List=[]
if n>=2 and n<=10:
  for i in range(n):

    List.append(int(input()))

sets=set(List)
sets.remove(max(sets))

print(max(sets))