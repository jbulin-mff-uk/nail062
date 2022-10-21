# generate a CNF for the boardomino problem
# n x n board, positions (0,0),...,(n-1,n-1), assume n >=4
# propositional variables:
# * h_{ij} : is there a horizontal tile whose upper left corner is in the field (i,j)? 
#            for (i,j)!=(0,0) and (i,j)!=(n-1,n-2) and j!=n-1)
# * v_{ij} : is there a vertical tile whose upper left corner is in the field (i,j)? 
#            for (i,j)!=(0,0) and (i,j)!=(n-2,n-1) and i!=n-1
# the variables are represented by consecutive integers 1, 2, ... 2*n*n-2*n-4

import itertools
import sys


def v(h,i,j,n):
    # return the number corresponding to the variable h_{ij} if h==True and v_{ij} if h==False
    # n is the size of the board
    if h:
        #return f"h{i}{j}"        
        return i*(n-1)+j
    else:
        #return f"v{i}{j}"         
        return n*n-n-2 + i*n+j


def exactly_one_true(vars):
    # outputs clauses saying that exactly one of the variables is true
    # at least one true
    print(" ".join(map(str,vars))+" 0")
    # no two can be true at the same time
    for pair in itertools.combinations(vars, 2):
        print(f"-{pair[0]} -{pair[1]} 0")


def generate_cnf_formula(n):
    # print the header
    print(f"p cnf {2*(n*(n-1)-2)} {2*2 + 4*(2+(n-3)*4) +(n-2)*(n-2)*7}")

    # upper right and lower left corner:
    exactly_one_true([v(True,0,n-2,n), v(False,0,n-1,n)])
    exactly_one_true([v(True,n-1,0,n), v(False,n-2,0,n)])

    # in the first row
    for j in range(1,n-1):
        if j==1:
            exactly_one_true([v(True,0,1,n), v(False,0,1,n)])    
        else:
            exactly_one_true([v(True,0,j-1,n), v(True,0,j,n), v(False,0,j,n)])

    # in the last row
    for j in range(1,n-1):
        if j==n-2:
            exactly_one_true([v(True,n-1,n-3,n), v(False,n-2,n-2,n)])        
        else:
            exactly_one_true([v(True,n-1,j-1,n), v(True,n-1,j,n), v(False,n-2,j,n)])

    # in the first column
    for i in range(1,n-1):
        if i==1:
            exactly_one_true([v(True,1,0,n), v(False,1,0,n)])
        else:
            exactly_one_true([v(True,i,0,n), v(False,i-1,0,n), v(False,i,0,n)])

    # in the last column
    for i in range(1,n-1):
        if i==n-2:
            exactly_one_true([v(True,n-2,n-2,n), v(False,n-3,n-1,n)])        
        else:
            exactly_one_true([v(True,i,n-2,n), v(False,i-1,n-1,n), v(False,i,n-1,n)])

    # elsewhere
    for i in range(1,n-1):
        for j in range(1,n-1):
            exactly_one_true([v(True,i,j-1,n), v(True,i,j,n), v(False,i-1,j,n), v(False,i,j,n)])


def show_variable_numbers(n):
    # for debugging
    print("Variable numbering:")
    for i in range(n):
        for j in range(n):
            if j!=n-1 and (i!=0 or j!=0) and (i!=n-1 or j!=n-2):
                print(f"{i} {j} h => {v(True,i,j)}")
    for i in range(n):
        for j in range(n):
            if i!=n-1 and (i!=0 or j!=0) and (i!=n-2 or j!=n-1):
                print(f"{i} {j} v => {v(False,i,j)}")


if __name__ == "__main__":
     generate_cnf_formula(int(sys.argv[1]))

        