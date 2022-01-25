"""
Given an m x n matrix, return all elements of the matrix in spiral order.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""
class Solution:
    def spiralOrder(self, matrix):
        left, right = 0, len(matrix[0])
        top , bottom = 0 ,len(matrix)
        list = []
        while left < right and top<bottom:
            for i in range(left,right):
                list.append(matrix[top][i])
            top +=1
            for j in range(top,bottom):
                list.append(matrix[j][right-1])
            right -=1
            if not (left< right and  top<bottom):
                break
            for k in range(right-1,left-1,-1):
                list.append(matrix[bottom-1][k])
            bottom -=1
            for l in range(bottom-1,top-1,-1):
                list.append(matrix[l][left])
            left +=1
        return list

cl = Solution()
ans = cl.spiralOrder([[[1,2,3],[4,5,6],[7,8,9]]])
print(ans)