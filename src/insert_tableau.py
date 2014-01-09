'''
Created on 2013-12-21

@author: Administrator
'''
import copy
def insert_creat(young_digram,o_DDS,p):
    insert_tableau = [ [ [1,p-1],[1] ] ]
    while insert_tableau[0][0][0]<=o_DDS:
        #print insert_tableau
        for i in xrange( 1,len( insert_tableau[0] ) ):
            temp = copy.deepcopy( insert_tableau[0] )
            if i == 1 and len( temp[i] )< young_digram[0]:
                temp[i].append( temp[0][0] )
                temp[0][1]-=1
                if temp[0][1] == 0:
                    temp[0][0]+=1
                    #temp[0][1] = p-1
                    temp[0][1] = p
                insert_tableau.append(temp)
                continue
            elif len(temp[i]) < young_digram[i-1] and len( temp[i] ) <len( temp[i-1]) and i != 1:
                temp[i].append( temp[0][0] )
                temp[0][1]-=1
                if temp[0][1] == 0:
                    temp[0][0]+= 1
                    #temp[0][1] = p-1
                    temp[0][1] = p
                insert_tableau.append(temp)
                continue
        if len( insert_tableau[0] ) <=len( young_digram ):
            temp = copy.deepcopy( insert_tableau[0] )
            temp.append( [ temp[0][0] ] )
            temp[0][1]-=1
            if temp[0][1] == 0:
                temp[0][0]+= 1
                #temp[0][1] = p-1
                temp[0][1] = p
            insert_tableau.append(temp)
        insert_tableau.pop(0)
    #print insert_tableau
    return insert_tableau
    