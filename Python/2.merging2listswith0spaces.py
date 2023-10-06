class Solution:
  def mergearray(self,num1,m,num2,n):
    for j in range(n):
      num1[m+j]=num2[j]
    num1.sort()
    print(num1)
a=Solution()
a.mergearray([1,2,3,0,0,0],3,[4,5,6],3)


'''
op
[1,2,3,4,5,6]
'''
