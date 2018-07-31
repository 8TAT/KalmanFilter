import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        if self.h == 1:
            return self[0][0]
        
        if self.h == 2:
            
            ad = self[0][0]*self[1][1]
            bc = self[0][1]*self[1][0]
            result = (ad) - (bc)

        return result

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        tr = 0
        for i in range(self.h):
            tr+= self[i][i]
        return tr
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        if self.determinant() == 0:
            return 0  

        det = self.determinant()

        result = zeroes(self.h,self.w)
#copying self values into result matrix
        for i in range(self.h):
            for j in range(self.w):
                result[i][j] = self[i][j]

        if self.h == 2:
            temp = result[0][0]
            result[0][0] = result[1][1]
            result[1][1] = temp

            result[0][1] *=-1
            result[1][0] *=-1

        for i in range(result.h):
            for j in range(result.w):
                result[i][j] *= 1/det 
        
        return result

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        result = zeroes(self.w, self.h)
        
        for i in range(self.h):
            for j in range(self.w):
                result[j][i] = self[i][j]
        return result

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same")
            
        result = zeroes(self.h, self.w)
        
        for i in range(result.h):
            for j in range(result.w):
                result[i][j] = self[i][j] + other[i][j]
        return result 

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #Take a matrix, and return the negative of that matrix
        negative = zeroes(self.h, self.w) #create a matrix of zeroes with H and W of the self matrix
        #for i in range(len(negative.g)):
        for i in range(negative.h): #iterate through rows of self
            for j in range(negative.w):#iterate through the columns of the rows of self
                negative[i][j]= self[i][j]*-1 # mult -1 by the value of the self matrix at the position [i][j] and store it in the negative                                               matrix at the position [i][j].
        return negative # return the negative matrix

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        # 
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
            
        result = zeroes(self.h, self.w)
        
        for i in range(result.h):
            for j in range(result.w):
                result[i][j] = self[i][j] - other[i][j]
        return result 

    def __mul__(self, other): 
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        # 
        if self.w != other.h:
             raise(ValueError, "Cannot multiply the two matrices. Incorrect dimensions.")
            
        result = zeroes(self.h, other.w)
        for i in range(self.h):
            for j in range(other.w):
                for k in range (self.w):
                    result[i][j] +=  self[i][k]*other[k][j]
                    print (result)
        return result

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            result = zeroes(self.h, self.w)
            for i in range(result.h):
                for j in range(result.w):
                    result[i][j] =  self[i][j]*other
        return result
            