class Solution:
	def pushZerosToEnd(self,arr):
	    i=0
	    for num in arr:
	        if num!=0:
	            arr[i]=num
	            i+=1
	    while i<len(arr):
	        arr[i]=0
	        i+=1
	  
