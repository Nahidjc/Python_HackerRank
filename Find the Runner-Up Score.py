n = int(input())
arr = map(int, input().split())[:n]
sets=set(arr)
sets.remove(max(sets))

print(max(sets))