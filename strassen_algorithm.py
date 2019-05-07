import numpy as np
import timeit

# naive ijk matrix multiplication algorithm
def mat_mul(m1, m2):
    n = len(m1)
    M = np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                M[i,j] += m1[i,k] * m2[k,j]
    
    return M

def strassen(m1,m2):
    n = len(m1)
    # calcualte index of middle point
    mid = int(n/2)
    
    # initialize output matrix
    M = np.zeros((n,n)) 
    
    # set leaf_size here
    leaf_size = 32
    
    if n <= leaf_size:
        return mat_mul(m1,m2)
    
    a11 = m1[0:mid, 0:mid]
    a12 = m1[0:mid; mid:n]
    a21 = m1[mid:n, 0:mid]
    a22 = m1[mid:n, mid:n]
    
    b11 = m2[0:mid, 0:mid]
    b12 = m2[0:mid, mid:n]
    b21 = m2[mid:n, 0:mid]
    b22 = m2[mid:n, mid:n]
    
    s1 = b12 - b22
    s2 = a11 + a12
    s3 = a21 + a22
    s4 = b21 - b11
    s5 = a11 + a22
    s6 = b11 + b22
    s7 = a12 - a22
    s8 = b21 + b22
    s9 = a11 - a21
    s10 = b11 + b12
    
    p1 = a11 * s1
    p2 = s3 * b22
    p3 = s3 * b11
    p4 = a22 * s4
    p5 = s5 * s6
    p6 = s7 * s8
    p7 = s9 * s10
    
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p5 + p1 - p3 - p7
    
    M[0:mid, 0:mid] = c11
    M[0:mid, mid:] = c12
    M[mid:, 0:mid] = c21
    M[mid:, mid:] = c22
    
    return M

def __main__():
    # give length of matrix's row/column as input
    n = int(input("Give size of row/column: "))
    
    # generate two matrices to be multiplied
    A = np.random.rand(n,n)
    B = np.random.rand(n,n)
    
    # run naive algorithm and measure its running time
    start = timeit.default_timer()
    M1 = mat_mul(A,B)
    end = timeit.default_timer()
    t1 = end - start
    print("running time of niave matrix multiplication algorithm: %f (sec)" % t1)
    
    # run strassen's algorithm and measure its running time
    start = timeit.default_timer()
    M2 = strassen(A,B)
    end = timeit.default_timer()
    t2 = end - start
    print("running time of strassen's algorithm: %f (sec)" % t2)