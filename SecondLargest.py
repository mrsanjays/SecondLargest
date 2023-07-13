
"""
You are given an integer array A.
You have to find the second largest element/value in the array or report that no such element exists.
"""
class Solution:
    def SecondLargest(self,array):
        if len(array)<=1:
            return -1
        # to find Second Largest we need to find  maximum of array along with second max
        maximum = float('-inf')
        SecondMax=float('-inf')
        for element in array:
            if element>maximum:
                SecondMax=maximum
                maximum=element
            if element>SecondMax and element< maximum:
                SecondMax = element
        return SecondMax if SecondMax != float('-inf') else -1


if __name__ == "__main__":
    ob = Solution()
    array=list(map(int,input().split()))
    print(ob.SecondLargest(array))
