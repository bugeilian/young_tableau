'''
Created on 2013-12-23

@author: Administrator
'''
import numpy
def young2matrix(insert_tableau,record_tableau,o_DDS,d_DDS,n_DDS,young_digram):
    
    num = n_DDS*d_DDS
    record_tableau[0][0] = n_DDS
    record_tableau[0][1] = d_DDS
    biword = []
    while num != 0:
        for i in xrange(len( record_tableau )-1,0,-1):
            if record_tableau[i][ len( record_tableau[i])-1 ] == record_tableau[0][0]:
                num-= 1
                position = len( record_tableau[i]) 
                a = record_tableau[i].pop()
                if len( record_tableau[i] ) == 0:
                    record_tableau.pop()
                record_tableau[0][1]-= 1
                if record_tableau[0][1] == 0:
                    record_tableau[0][1] = d_DDS
                    record_tableau[0][0]-= 1
                    
                b=insert_tableau[ position ].pop()
                while position !=1:
                    if b >=insert_tableau[ position-1 ][len(insert_tableau[position-1])-1]:
                        c = insert_tableau[ position-1 ][len(insert_tableau[position-1])-1]
                        insert_tableau[ position-1 ][len(insert_tableau[position-1])-1] =b
                        b = c
                    else:
                        for j in xrange(0,len( insert_tableau[position-1] ) ):
                            if insert_tableau[position-1][j] == b:
                                break
                            elif insert_tableau[position-1][j] > b:
                                c=insert_tableau[position-1][j-1]
                                insert_tableau[position-1][j-1] = b 
                                b = c
                                break
                    position-=1
                list_tem = [a,b]
                biword.insert(0,list_tem)
                #print record_tableau
                #print insert_tableau
                break
    #print biword
    matrix_a = numpy.zeros((n_DDS,o_DDS),dtype=int)
    for i in xrange(0,len( biword ) ):
        matrix_a[ biword[i][0]-1 ][biword[i][1]-1 ] = 1
    #print matrix_a
    return matrix_a