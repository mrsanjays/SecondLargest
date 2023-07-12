
"""
You are given an integer array A.
You have to find the second largest element/value in the array or report that no such element exists.
"""
class Solution:
    def SecondLargest(self,array):
        if len(array)<=1:
            return -1
        # to find Second Largest we need to find unique elements and maximum of array
        maximum = float('-inf')
        uniqueElements = []
        for i in range(len(array)):
            if array[i] not in uniqueElements:
                uniqueElements.append(array[i])
            if array[i]>maximum:
                maximum=array[i]
        if len(uniqueElements)==1:
            return -1
        #find the Second maximum
        else:
            SecondMax=float('-inf')
            for element in uniqueElements:
                if element>SecondMax and element<maximum:
                    SecondMax=element
            return  SecondMax


if __name__ == "__main__":
    ob = Solution()
    array=list(map(int,input().split()))
    print(ob.SecondLargest(array))