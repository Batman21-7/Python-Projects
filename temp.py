n = int(input())
arr = [int(x) for x in input().split()]
sum = 0
if n%2==1:
    n+=1
n = n//2
arr.sort(reverse=True)
for i in range(n):
    if arr[i]>0:
        sum += arr[i]
    else:
        break
print(sum)
