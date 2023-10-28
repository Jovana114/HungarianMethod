import numpy as np
from Simplex import Simplex

def main():

    #Example 1) - min
    function_koefs = np.array([2, -3])
    restriction_koefs = np.matrix([[1, 1], [1, -1]]) # <=
    free_koefs = np.array([[4], [6]])  
    
    Simplex(function_koefs, restriction_koefs, free_koefs)
    
    #Example 2) - max
    #function_koefs = np.array([-1, -1])
    #restriction_koefs = np.matrix([[-1, 0], [0, -1]]) # <=
    #free_koefs = np.array([[0], [0]])
    
    #Simplex(function_koefs, restriction_koefs, free_koefs, True)

if __name__ == '__main__':
	main()