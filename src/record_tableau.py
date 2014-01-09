'''
Created on 2013-12-22

@author: Administrator
'''
import copy
from shapeturnover import *
def record_creat(young_digram,n_DDS,d_DDS,o_DDS):
    insert_l = [ [1] ]
    young_digram_over=shape_turnover(young_digram,o_DDS)
    print young_digram_over
    #num = o_DDS
    surp = d_DDS-1
    p = 1
    '''
    for i in xrange(1,num ):
        insert_l.append([p])
        surp-= 1
        if surp == 0 and i != num-1:
            surp = d_DDS-1
            p+= 1
    '''
    insert_l.insert(0,[1,d_DDS-1])
    insert_tableau = []
    insert_tableau.insert( 0,copy.deepcopy(insert_l) )

    while insert_tableau[0][0][0]<=n_DDS:
        print('complete')
        for i in xrange( 1,len( insert_tableau[0]) ):
            print i
            if i == 1 and len( insert_tableau[0][i] )< young_digram_over[0]:
                temp = copy.deepcopy( insert_tableau[0] )
                temp[i].append( temp[0][0] )
                temp[0][1]-=1
                if temp[0][1] == 0:
                    temp[0][0]+=1
                    #if temp[0][0] < p:
                        #temp[0][1]=1
                    if temp[0][0] == p:
                        temp[0][1] = surp+1
                    else:
                        temp[0][1] = d_DDS
                insert_tableau.append(temp)
                print("complete")
                continue
            
            
            elif len( insert_tableau[0][i] ) <len( insert_tableau[0][i-1]) and i !=1 and len(insert_tableau[0][i]) < young_digram_over[i-1]:
                temp = copy.deepcopy( insert_tableau[0] )
                temp[i].append( temp[0][0] )
                temp[0][1]-=1
                if temp[0][1] == 0:
                    temp[0][0]+= 1
                    #if temp[0][0] < p:
                        #temp[0][1]=1
                    if temp[0][0] == p:
                        temp[0][1] = surp+1
                    else:
                        temp[0][1] = d_DDS
                insert_tableau.append(temp)
                continue
        if len(insert_tableau[0]) <=len(young_digram_over)+1:
            temp = copy.deepcopy( insert_tableau[0] )
            temp.append( [temp[0][0]] )
            temp[0][1]-=1
            if temp[0][1] == 0:
                temp[0][0]+= 1
                #if temp[0][0] < p:
                    #temp[0][1]=1
                if temp[0][0] == p:
                    temp[0][1] = surp+1
                else:
                    temp[0][1] = d_DDS
            insert_tableau.append(temp)
        insert_tableau.pop(0)
        print(insert_tableau)
        #print(insert_tableau)
    return insert_tableau