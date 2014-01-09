'''
Created on 2013-12-23

@author: Administrator
'''
def addcol(insert_tableau,o_DDS):
    list_a = []
    for i in xrange(1,o_DDS+1):
        list_a.append(i)
    insert_tableau.insert(1,list_a)
    print insert_tableau
    return insert_tableau