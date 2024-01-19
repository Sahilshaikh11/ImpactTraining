#!/usr/bin/env python
# coding: utf-8

# In[4]:


def stringcompare(str1,str2,i,j):
    while(i>=0 and j>=0):
        count1=0
        while (i>0 and (count1>0 or str1[i]=='#')):
            if (str1[i]=='#'):
                count1+=1
            else:
                count1-=1
            i-=1
        count2=0
        while (j>0 and (count2>0 or str2[j]=='#')):
            if (str2[j]=='#'):
                count2+=1
            else:
                count2-=1
            j-=1
        if (i>=0 and j>=0):
            if(str1[i]!=str2[j]):
                return False
            else:
                i-=1
                j-=1
        else:
            if (i<0 or j<0):
                return False
    return True
        
    
str1=input()
str2=input()
n1=len(str1)
n2=len(str2)
i=n1-1
j=n2-1
print(stringcompare(str1,str2,i,j))


# In[17]:


def merge(arr,l,m,h):
    n1=m-l+1
    n2=h-m
    arr1=[]
    arr2=[]
    for i in range(l,m+1):
        arr1.append(arr[i])
    for i in range(m+1,h+1):
        arr2.append(arr[i])
    i=0
    j=0
    k=l
    while (i<n1 and j<n2):
        if arr1[i]<arr2[j]:
            arr[k]=arr1[i]
            i+=1
        else:
            arr[k]=arr2[j]
            j+=1
        k+=1

    while i<n1:
        arr[k]=arr1[i]
        i+=1
        k+=1
    while j<n2:
        arr[k]=arr2[j]
        j+=1
        k+=1


def mergesort(arr,l,h):
    if l>=h:
        return 
    m=l+(h-l)//2
    mergesort(arr,l,m)
    mergesort(arr,m+1,h)
    merge(arr,l,m,h)
    
    












def insertionSort(arr,n):
    for i in range(1,n):
        key=arr[i] #5
        j=i-1   #0
        while j>=0 and key<arr[j]:#  False
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
        
    
# 4 - 23  6 1 2 2 3 566    



def selectionSort(arr,n):
    for i in range(n):
        min_i=i
        for j in range(i+1,n):
            if arr[j]<arr[min_i]:
                min_i=j
        if min_i==i:
            pass
        else:
            arr[i],arr[min_i]=arr[min_i],arr[i]
        
        
        
    
arr=list(map(int,input().split()))
n=len(arr)
mergesort(arr,0,n-1)
arr


# In[16]:


5//2


# In[2]:


# moving zeroes

arr=list(map(int,input().split()))
i=0
j=0
while j<len(arr):
    if arr[j]!=0:
        arr[i]=arr[j]
        i+=1
        j+=1
    else:
        j+=1
print(arr)
while i<len(arr):
    arr[i]=0
    i+=1
arr


# In[ ]:


# maximum summation subarray
#kadane algorithm
# maximum product subarray
import sys
arr=list(map(int,input().split()))
n=len(arr)
maxx=-sys.maxsize-1
for  i in range(n):
    summ=arr[i]













# In[2]:


import sys
print(sys.maxsize)


# In[12]:


def palindrome(strr):
    i=0
    j=len(strr)-1
    while i<j:
        while  not((strr[i]>='a '  and  strr[i]<='z') or (strr[i]>='0' and strr[i]<='9')):
            i+=1
        while  not((strr[j]>='a '  and  strr[j]<='z') or (strr[j]>='0' and strr[j]<='9')):
            j-=1
        if strr[i] != strr[j]:
            return False
        else:
            i+=1
            j-=1
    return True
    


strr=input()
palindrome(strr)


# In[18]:


strr="atul0"
print(strr[2]<='z')
sett={2,3,4,45}
#sett.pop()
sett.remove(3)
#sett.pop()
sett.remove(2)


# In[19]:


dictt={'a':"atul", 'b':"bharat", 'c':"cherry"}
dictt.pop('a')
dictt.pop('b')
dictt.remove()


# In[20]:


class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

        
    
hash_ar=[]
arr= 


# In[23]:


# issubsequence
def issubsequence(strr,s2,i,j,n):
    while j<n:
        if str1[j]==s2[i]:
            i+=1
        j+=1
        
        if i==len(s2):
            return True
    return False
str1=input()
s2= input()
i=0 # pointer for str1
j=0 # pointer for s2
n=len(str1)
issubsequence(str1,s2,i,j,n)


# In[40]:


class Node: 
    def __init__(self, key, value): 
        self.key = key 
        self.value = value 
        self.next = None
  
  
class HashTable: 
    def __init__(self, capacity): 
        self.capacity = capacity 
        self.size = 0
        self.table = [None] * capacity 
  
    def _hash(self, key): 
        return hash(key) % self.capacity 
  
    def insert(self, key, value): 
        index = self._hash(key) 
  
        if self.table[index] is None: 
            self.table[index] = Node(key, value) 
            self.size += 1
        else: 
            current = self.table[index] 
            while current: 
                if current.key == key: 
                    current.value = value 
                    return
                current = current.next
            new_node = Node(key, value) 
            new_node.next = self.table[index] 
            self.table[index] = new_node 
            self.size += 1
  
    def search(self, key): 
        index = self._hash(key) 
  
        current = self.table[index] 
        while current:
            print(current.value)
            if current.key == key: 
                return current.value 
            current = current.next
  
        raise KeyError(key) 
  
    def remove(self, key): 
        index = self._hash(key) 
  
        previous = None
        current = self.table[index] 
  
        while current: 
            if current.key == key: 
                if previous: 
                    previous.next = current.next
                else: 
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current 
            current = current.next
  
        raise KeyError(key) 
  
    def __len__(self): 
        return self.size
    def printt(self,key):
        index=self._hash(key)
        current=self.table[index]
        while current:
            print(current.key ,':',current.value,end="-> ")
            current=current.next
  
    def __contains__(self, key): 
        try: 
            self.search(key) 
            return True
        except KeyError: 
            return False
if __name__ == '__main__': 
    ht = HashTable(5)
    ht.insert("apple", 3) 
    ht.insert("banana", 2) 
    ht.insert("cherry", 5) 
     
  
    
    ht.insert("banana", "parul")
    ht.insert(9,"assss")
    ht.insert(4, "as") 
    ht.printt("banana")


# In[43]:


print(help(hash))


# In[48]:



'''Given a number N, find its square root. 
You need to find and print only the integral part of square root of N.
For eg. if number given is 18, answer is 4.'''
def sqrt(n,low,high):
    while low<=high:
        mid=low+(high-low)//2
        if mid*mid==n:
            ans =mid
            return ans
        elif mid*mid >n:
            high=mid-1
        else:
            low=mid+1
            ans=mid
    
    i=0.1
    while i<1:
        
        value =ans+i
        i+=0.1
        if value*value>=n:
            return value
    
n=eval(input())
low=1
high=n//2
sqrt(n,low,high)


# In[9]:


# to find the first and last occurrence and an element in an sorted array

"linear search"

arr=list(map(int,input().split()))
key=eval(input())
first=-1
last=-1
'''
for i in range(len(arr)):
    if arr[i]==key and first==-1:
        first=i
        last=i
    elif arr[i]==key:
        last=i
print(first , last)
'''


# binary search
def firstoccurrence(arr,si,ei,first):
    while si<=ei:
        mid=si +(ei-si)//2
        if arr[mid]==key:
            first=mid
            ei=mid-1
        elif arr[mid]<key:
            si=mid+1
        else:
            ei=mid-1
    return first
def lastoccurrence(arr,si,ei,last):
    while si<=ei:
        mid=si +(ei-si)//2
        if arr[mid]==key:
            last=mid
            si=mid+1
        elif arr[mid]<key:
            si=mid+1
        else:
            ei=mid-1
    return last

si=0
ei=len(arr)-1
print(firstoccurrence(arr,si,ei,first))
print(lastoccurrence(arr,si,ei,last))
        
    
'''
We find the index of the middle element of ARR as mid = si + (ei - si) /2 .
If (ARR[mid] == K)
first = mid
end=mid-1
We update the end index, ei = mid - 1.
Else If (ARR[mid] < K)
We update the start index, si = mid + 1. 
Else
We update the end index, ei = mid - 1.
 
The modified binary search to find the last occurrence of ‘K’ :
We find the index of the middle element of ARR as mid = si + (ei - si) / 2
If (ARR[mid] == K)
last = mid
start=mid+1
We update the start index, si = mid + 1.
Else If (ARR[mid] < K)
We update the start index, si = mid + 1.
Else If (ARR[mid] > K)
We update the end index, ei = mid - 1.
   
Time Complexity
O(log(N)), where N is the length of the given array/list ARR. 
'''


# In[17]:


# find the duplicates in an array
'''
Time complexity: O(N) 
Space complexity: O(1)
Where N is the length of the array.
'''
def duplicates(arr,n):
    for i in range(n):
        index=arr[i]%n
        arr[index]+=n
        if arr[i]/n>=2:
              return i
                 
    for i in range(n):
              if arr[i]/n>=2:
                  return i
arr= list(map(int,input().split()))
n=len(arr)
print(duplicates(arr,n))








'''


def findDuplicate(arr, n):
    
    
    for i in range(n):
        index = abs(arr[i]) - 1
        arr[index] *= -1
        if arr[index] > 0:
            return abs(arr[i])
            
            
    return -1
 '''           


# In[20]:


''' Given an array of length N. Peak element is defined as the element
greater than both of its neighbors. Formally, if ‘arr[i]’ is the peak element,
‘arr[i – 1]’ < ‘arr[i]’ and ‘arr[i + 1]’ < ‘arr[i]’. Find the index(0-based) of
a peak element in the array.
If there are multiple peak numbers, return the index of any peak number.'''
def peakelement(arr,n):
    if arr[0]>arr[1]:
        return 0
    if arr[n-1]>arr[n-2]:
        return n-1
    low=1
    high=n-2
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid]>arr[mid-1]:
            low=mid+1
            
        else:
            high=mid-1
    return -1
    
arr=[11,2,3,5,2,6,9,5]
print(peakelement(arr,len(arr)))









'''If n == 1: This means the array size is 1. If the array contains only one element,
we will return that index i.e. 0.
If arr[0] > arr[1]: This means the very first element of the array is the peak element. 
So, we will return the index 0.


If arr[n-1] > arr[n-2]: This means the last element of the array is the peak element. 
So, we will return the index n-1.

Place the 2 pointers i.e. low and high:

Initially, we will place the pointers excluding index 0 and n-1 like this: 
low will point to index 1, and high will point to index n-2 i.e. the second last index.

Calculate the ‘mid’: 
Now, inside a loop, we will calculate the value of ‘mid’ using the following formula:
mid = (low+high) // 2 ( ‘//’ refers to integer division)

Check if arr[mid] is the peak element:
If arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
If this condition is true for arr[mid], we can conclude arr[mid] is the peak element.
We will return the index ‘mid’.
If arr[mid] > arr[mid-1]: This means we are in the left half and we should eliminate it 
as our peak element appears on the right. So, we will do this:
low = mid+1.
Otherwise, we are in the right half and we should eliminate it as our peak element appears on the left. 
So, we will do this: high = mid-1. This case also handles the case for the index ‘mid’ being a common point
of a decreasing and increasing sequence. It will consider the left peak and eliminate the right peak.'''



# In[ ]:


# Aggressive cows


'''You are given an array 'arr' consisting of 'n' integers which denote the position
of a stall.
You are also given an integer 'k' which denotes the number of aggressive cows.
You are given the task of assigning stalls to 'k' cows such that the minimum distance 
between any two of them is the maximum possible.

Print the maximum possible minimum distance.

Example:
Input: 'n' = 3, 'k' = 2 and 'arr' = {1, 2, 3}

Output: 2

Explanation: The maximum possible minimum distance will be 2 when 2 cows are placed 
at positions {1, 3}.
Here distance between cows is 2.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
6 4
0 3 4 7 10 9

Sample Output 1 :
3

Explanation to Sample Input 1 :
The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed
at positions {0, 3, 7, 10}. Here distance between cows are 3, 4 and 3 respectively.'''


# In[ ]:


'''You are given an unsorted array containing ‘N’ integers. You need to find ‘K’ largest elements 
from the given array. Also, you need to return the elements in non-decreasing order.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 100
1 <= N <= 10^4  
1<= K <= N  
-10^9 <= ARR[i] <= 10^9

Where ‘T’ is the number of test cases, ‘N’ is the size of the array, ‘K’ is the number of elements
you need to return as an answer and ARR[i] is the size of the array of elements.

Time Limit: 1 sec
Sample Input 1:
2
4 2
3 4 2 1
5 1
2 2 3 3 1
Sample Output 1:
3 4
3
Explanation for sample input 1:
Test case 1:
If we sort the array then it will look like: [1, 2, 3, 4]. The 2 largest elements will be [3, 4].

Test case 2:
If we sort the array then it will look like: [1, 2, 2, 3, 3]. Then the largest element will be [3].
Sample Input 2:
2
5 5
0 10 1 2 2
6 2
-2 12 -1 1 20 1 
Sample Output 2:
0 1 2 2 10
12 20
'''


# In[ ]:





# In[11]:



graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['A', 'C', 'E'],
    'E': ['D'],
}

def bfs(node):
    visited = [False] * (len(graph))
    queue = []

    visited.append(node)#A
    queue.append(node)

    while queue:
        v = queue.pop(0)
        print(v, end=" ")

        # Get all adjacent nodes of the removed node v from the graph hash table.
        # If an adjacent node has not been visited yet,
        # then mark it as visited and add it to the queue.
        for neigh in graph[v]:
            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)



bfs('A')


# In[ ]:


'''Every time we reach a new node, we will take the following steps:

We add the node to the top of the stack.
Marked it as visited.
We check if this node has any adjacent nodes:
If it has adjacent nodes, then we ensure that they have not been visited already, 
and then visited it.
We removed it from the stack if it had no adjacent nodes.
With every node added to the stack, we repeat the above steps or recursively 
visit each node until we reach the dead end.


0: [2]
1: [2, 3]
2: [0, 1, 4]
3: [1, 4]
4: [2, 3]
'''
def dfs(node, graph, visited, component):
    component.append(node) 
    visited[node] = True  

    # Traverse to each adjacent node of a node
    for child in graph[node]:
        if not visited[child]:  # Check whether the node is visited or not
            dfs(child, graph, visited, component)  # Call the dfs recursively


graph = {
        0: [2],
        1: [2, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3]
    }
node = 0
visited = [False]*len(graph)  
component = []
dfs(node, graph, visited, component) 
print(f"Following is the Depth-first search: {component}") 

    

