def floorSqrt(n):
   # write your code logic here .
   ans = 0
   start = 0
   end = n
   while start <= end:
      mid = (start + end)//2
      if mid*mid <= n:
         ans = mid
         start = mid+1
      else:
         end = mid-1
   return ans



n= int(input())
print(floorSqrt(n))