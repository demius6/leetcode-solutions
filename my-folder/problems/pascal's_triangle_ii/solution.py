class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        i = 1
        a = []
        while i <= (rowIndex + 1):
            list = [1 for i in range(i)]
            a.append(list)
            i += 1
        if len(a)>2:
            for i in range(2,rowIndex+1):
                for j in range(1,(len(a[i])-1)):
                    a[i][j] = a[i-1][j] + a[i-1][j-1]
        return a[rowIndex]
