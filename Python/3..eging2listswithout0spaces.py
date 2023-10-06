class Solution(object):
  def merge(self,num1,m,num2,n):
    res=[0]*(m+n)
    i,j,k=0,0,0
    while i<m and j<n:
      if num1[i]<num2[j]:
        res[k]=num1[i]
        i+=1
      else:
        res[k]=num2[j]
        j+=1
      k+=1
    while i<m:
      res[k]=num1[j]
      i+=1
      k+=1
    while j<n:
      res[k]=num2[j]
      j+=1
      k+=1
    return res
a=Solution()
a.merge([1,2,3],3,[4,5,7],3)
print(res)
