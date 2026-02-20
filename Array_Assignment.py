"""
Array Problems Assignment
Name: Saloni Khare
Enrollment No: 0103AL231177
Total Problems: 33
Language: Python
"""

#1. Reverse an Array
arr=[1,3,3,7,5,7,9]
def rev(arr):
  n=len(arr)
  for i in range(n//2):
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
  return arr
print("Reverse is: ",rev(arr))

#2. Find the Maximum & Minimum Element
print("Max element is: ",max(arr))
print("Min element is: ",min(arr))

#4. Find the Second Largest Element
m=max(arr)
n=len(arr)
sm=float('-inf')
for i in range(n):
  if arr[i]==m:
    continue
  if arr[i]>sm:
    sm=arr[i]
print(sm if sm != float('-inf') else None)

#5. Count Frequency of Elements
arr=[1,2,8,3,5,2,3]
def count_frequency(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq
print("Frequency is: ",count_frequency(arr))

#6. Check if Array is Sorted
def is_sorted(arr):
    for i in range(len(arr)-1):
      if arr[i]>arr[i+1]:
          return False
    return True
print("Array is sorted: ",is_sorted(arr))
    
#7. Rotate Array by k Positions: Rotate the array to the right by k positions.
def rotate_array(arr, k):
    n = len(arr)
    k %= n
    
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)
    return arr
print("Array is: ",rotate_array(arr,3))

#8. Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.
def find_pair(arr, t):
    s = set()
    for num in arr:
        if t- num in s:
            return (num, t - num)
        s.add(num)
    return None
print("Nos are:",find_pair(arr,8))

#9. Remove Duplicates from Array: Remove duplicates from the array while maintaining order.
a=set()
r=[]
for i in arr:
  if i not in a:
    a.add(i)
    r.append(i)
print("Array became: ",r)

#10. Merge Two Sorted Arrays
a=[1,3,5,7]
b=[2,4,6,8,9]
x,y=0,0
n,m=len(a),len(b)
res=[]
while x<n and y<m:
  if a[x]<=b[y]:
    res.append(a[x])
    x+=1
  else:
    res.append(b[y])
    y+=1
res.extend(a[x:])
res.extend(b[y:])
print("Resultant array is: ",res)

#11. Remove given Element from Array
def remove_element(arr, target):
    j = 0
    for i in range(len(arr)):
        if arr[i] != target:
            arr[j] = arr[i]
            j += 1
    return arr[:j]
target=3
print(remove_element(arr, target))

#12. Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.
def missingNo(n):
  no=len(n)
  s=sum(n)
  s1=(no*(no+1))/2
  return int(s1-s)
n=[1,2,4,5,6]
print("Missing no is:",missingNo(n))

#13. Find Duplicates in an Array
def dupli(arr):
  f={}
  for i in arr:
    f[i]=f.get(i,0)+1
  ans=[]
  for k,v in f.items():
    if v>1:
      ans.append(k)
  return ans
print("Duplicates are:",dupli(arr))

#14. Find Intersection of Two Arrays: Find the common elements between two arrays.
a=[1,2,4,6]
b=[4,5,6,7,2]
def inter(a,b):
  sb=set(a)
  x=[]
  for i in b:
    if i in sb:
      x.append(i)
  return x
print("Intersection is:",inter(a,b))

#15. Find Union of Two Arrays
a=[1,2,4,6]
b=[4,5,6,7,2]
def uni(a,b):
  x=a+b
  return list(set(x))
print("Union is:",uni(a,b))

#16. Check if Two Arrays Are Equal: if two arrays contain the same elements
a=[1,2,4,6,5,7]
b=[4,5,6,7,2,1]
def checkEqual(a, b):
    n, m = len(a), len(b)
    if n != m:
        return False
    mp = {}
    for num in a:
        mp[num] = mp.get(num, 0) + 1
    for num in b:
        if num not in mp:
            return False
        if mp[num] == 0:
            return False
        mp[num] -= 1
    return True
print("Is 2 arrays equal",checkEqual(a,b))

#17. Find the Leader Elements: An element is a leader if it is greater than all elements to its right.
arr=[1,5,2,4,3]
def leader(arr):
  a=[]
  m=arr[-1]
  a.append(m)
  for i in range(len(arr)-2,-1,-1):
    if arr[i]>m:
      m=arr[i]
      a.append(m)
  return a[::-1]
print("Leader elements are:",leader(arr))

#18. Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements.
arr=[1,0,3,0,4,0,5]
def zeros(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1
    return arr
print("Array is",zeros(arr))

#19. Find Subarray with Given Sum.
def suba(nu, t):
    s = 0
    curr = 0
    for e in range(len(nu)):
        curr += nu[e]
        while curr > t and s < e:
            curr -= nu[s]
            s += 1
        if curr == t:
            return [s, e]
    return []
t=21
nu=[15, 2, 4, 8, 9, 5, 10, 23]
print(suba(nu,t))

#20. Rotate Array to the Left by k Positions
def rotate_array(arr, k):
    k%=len(arr)
    return arr[k:]+arr[0:k]
print("Array is: ",rotate_array(nu,3))

#21. Find the Kth Smallest Elements
import heapq
def sheap(arr,k):
  heapq.heapify(arr)
  for i in range(k-1):
    heapq.heappop(arr)
  return heapq.heappop(arr)
print("Kth smallest element is",sheap(nu,4))

#22. Find All Subarrays
arr=[1,2,3]
def subarrays(arr):
    subarr= []
    n = len(arr)
    for start in range(n):
        for end in range(start+1, n+1):
            subarr.append(arr[start:end])
    return subarr

print("Subarrays are",subarrays(arr))
#23. Maximum Sum Subarray (Kadane's Algorithm)
def maxsub(arr):
  currsum=arr[0]
  maxsum=arr[0]
  for i in arr[1:]:
    currsum=max(i,currsum+i)
    maxsum=max(maxsum,currsum)
  return maxsum
arr = [2, 3, -8, 7, -1, 2, 3]
print("Max subarray sum is:",maxsub(arr))

#24. Rearrange Array Alternately: Rearrange an array such that elements alternate between the largest and smallest.
def rearrange(arr):
  ans=[]
  arr.sort()
  i,j=0,len(arr)-1
  while i<=j:
    if i!=j:
      ans.append(arr[j])
      ans.append(arr[i])
    else:
      ans.append(arr[i])
    i+=1
    j-=1
  return ans
print("Alternated array is",rearrange(arr))

#25. Find Majority Element: Find the element that appears more than n/2 times.
arr=[1,2,3,2,2,2]
def maj(arr):
  f={}
  for i in arr:
    f[i]=f.get(i,0)+1
  x=len(arr)/2
  for k,v in f.items():
    if v>x:
      return k
print("Majority element is",maj(arr))
      
#26. Find Peak Element: A peak element is greater than its neighbors. Find one such element.
def peak(arr):
  if arr[0]>arr[1]:
    return arr[0]
  for i in range(1,len(arr)-1):
    if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
      return arr[i]
  if arr[-1]>arr[-2]:
    return arr[-1]
  return None
arr = [1, 3, 2, 5, 4, 6]
print("Peak element is",peak(arr))

#27. Find the First Missing Positive: Find the smallest positive integer missing in the array.
def fP(nums):
  n = len(nums)
  for i in range(n):
    while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
      nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
  for i in range(n):
    if nums[i] != i + 1:
      return i + 1
  return n + 1
nums=[-1,3,4,1]
print("First positive no is",fP(nums))

#28. Sort an Array of 0s, 1s, and 2s: Sort an array consisting of only 0s, 1s, and 2s.
def dnf(arr):
  n=len(arr)
  l,m,h=0,0,n-1
  while m<=h:
    if arr[m]==0:
      arr[l],arr[m]=arr[m],arr[l]
      l+=1
      m+=1
    elif arr[m]==1:
      m+=1
    else:
      arr[m],arr[h]=arr[h],arr[m]
      h-=1
  return arr
arr=[0,1,0,2,0,2]
print("Sorted array is",dnf(arr))

#29. Find the Longest Consecutive Sequence: Find the length of the longest consecutive sequence of integers.
def longestC(nums):
  s = set(nums)
  m = 0
  for num in s:
    if num - 1 not in s:
      length = 1
      while num + length in s:
        length += 1
      m = max(m, length)
  return m
arr=[45,23,25,24,22]
print("Length of longest consecutive sequence is",longestC(arr))

"""30. Product of Array Except Self
Given an array, return a new array where each element is the product of all elements except itself.
Do not use division.
Input: [1,2,3,4]
Output: [24,12,8,6]"""
def prodArr(nums):
  n=len(nums)
  pProd,sProd=[1]*n,[1]*n
  ans=[0]*n
  for i in range(1,n):
    pProd[i]=nums[i-1]*pProd[i-1]
  for j in range(n-2,-1,-1):
    sProd[j]=nums[j+1]*sProd[j+1]
  for i in range(n):
    ans[i]=pProd[i]*sProd[i]
  return ans
nums=[1,2,3,4]
print("Product of array is",prodArr(nums))
#31. Find Equilibrium Index: Find an index such that sum of elements on left = sum on right.
def addArr(nums):
  tsum=sum(nums)
  lsum=0
  for i,j in enumerate(nums):
    if lsum==tsum-lsum-j:
      return i
    lsum+=j
  return -1
nums=[1,2,1,3,4]
print("Equllibrium index is",addArr(nums))

#32. Find Maximum Product Pair: Find two elements whose product is maximum.
def maxprod(arr):
  m1=float('-inf')
  m2=float('-inf')
  mi1=float('inf')
  mi2=float('inf')
  for i in arr:
    if i>m1:
      m2=m1
      m1=i
    elif i>m2:
      m2=i
    if i<mi1:
      mi2=mi1
      mi1=i
    elif i<mi2:
      mi2=i
  return max(m1*m2,mi1*mi2)
print("Max product is",maxprod(nums))
  
#33. Find Maximum Difference (j > i)
def maxDiff(arr):
    if not arr:
        return 0
    miv=arr[0]
    madiff= float('-inf')
    for j in range(1, len(arr)):
        madiff=max(madiff,arr[j]-miv)
        miv=min(miv,arr[j])
    return madiff
nums = [2, 3, 10, 6, 4, 8, 1]
print("Maximum difference is", maxDiff(nums))
