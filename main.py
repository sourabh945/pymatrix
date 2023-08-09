import inspect

__author__="sourabh945"
__version__="0.0.1"
__email__="sheokand.anil.sourabh@gmail.com"

class Matrix:
    def __init__(self,elements:list) -> None:
        self.element = elements
        self.nrow = elements.__len__()
        self.ncol = elements[0].__len__()
        if Matrix.is_valid(self) is True:
            self.order = f"{self.nrow}X{self.ncol}"
            if self.nrow == self.ncol:
                self.det = Matrix.determinet(self)
                if self.det != 0:
                    self.inv = Matrix.inverse(self)

    class Error(Exception):
        def __init__(self,message) -> None:
            super().__init__()
            print("Error ::: " )
            error = inspect.stack()
            print(f"file= {error[-1][1]} \n line= {error[-1][2]} \n    >>> {error[-1][-2][0]}")
            print(message)
            exit()


    def is_valid(self:object) -> bool:
        for i in self.element:
            if self.ncol != i.__len__():
                Matrix.Error(" Invalid Matrix :: all rows have not same number of columns")
        return True
    

    def minor(self, row, column) -> list:
        if row >= self.nrow or column >= self.ncol:
            return Exception("Indexing Error")
        result = []
        for i in range(self.nrow):
            if i != row:
                b_col = []
                for j in range(self.ncol):
                    if j != column:
                        b_col.append(self.element[i][j])
                result.append(b_col)
        return result 
    
    def all_minor(self):
        result = []
        for i in range(self.nrow):
            for j in range(self.ncol):
                result.append(Matrix.minor(self,i,j))
        return result
    
    def transpose(self):
        result=[]
        for i in range(self.ncol):
            mid_col = []
            for j in range(self.nrow):
                mid_col.append(0)
            result.append(mid_col)
        print(mid_col)    
        for i in range(self.nrow):
            for j in range(self.ncol):
                result[j][i] = self.element[i][j]
        return result

    def deter(matrix:list):
        if matrix.__len__() == 1:
            return matrix[0][0]
        def minor(matrix,row,col):
            result = []
            for i in range(matrix.__len__()):
                if i != row:
                    mid_col = []
                    for j in range(matrix.__len__()):
                        if j != col:
                            mid_col.append(matrix[i][j])
                    result.append(mid_col)
            return result
        if matrix.__len__() == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        else:
            det = 0
            for i in range(matrix.__len__()):
                det = det + ((-1)**(i))*Matrix.deter(minor(matrix,1,i))
        return det

    def determinet(self):
        return Matrix.deter(self.element)

    def inverse(self):
        if self.nrow == 2:
            result = [[0,0],[0,0]]
            for i in range(self.nrow):
                for j in range(self.nrow):
                    if i == j:
                        result[i][i] = self.element[i][i]/self.det
                    else:
                        result[i][j] = -1*self.element[j][i]/self.det
            return result
        if self.nrow == 1:
            return [[1/self.det]]
        mine = []
        minors = Matrix.all_minor(self)
        a = 0
        for i in minors:
            mine.append(((-1)**a)*(Matrix.deter(i)))
            a = a+1
        result = []
        for i in range(self.nrow):
            mid_col = []
            count = True
            for j in range(self.nrow):
                mid_col.append(float(mine[i+j*self.nrow]/(self.det)))
            result.append(mid_col)
        return result
 ha
