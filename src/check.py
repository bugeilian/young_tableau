'''
Created on 2013-12-26

@author: Administrator
'''


def check(matrix_tem):
    a,b= matrix_tem.shape
    num = 0
    for i in xrange(0,a):
        for j in xrange (i+1,a):
            for k in xrange(0,b):
                if matrix_tem[i][k] == 1 and matrix_tem[j][k] == 1:
                    num+= 1
                if num > 1:
                    return False
    return True
