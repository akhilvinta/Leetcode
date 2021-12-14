
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    print(str(i)  + "," + str(j))
                    for k in range(len(matrix[0])):
                        if k == j or matrix[i][k] == 0 or type(matrix[i][k]) == str:
                            continue
                        matrix[i][k] = str(matrix[i][k]) + 'a'
                    for k in range(len(matrix)):
                        if k == i or matrix[k][j] == 0 or type(matrix[k][j]) == str:
                            continue
                        matrix[k][j] = str(matrix[k][j]) + 'a'
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(type(matrix[i][j]) == str):
                    matrix[i][j] = 0

        return matrix
        