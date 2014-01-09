'''
Created on 2013-12-20

@author: Administrator
'''
from mstring import *
from insert_tableau import insert_creat
from record_tableau import record_creat
from young2matrix import young2matrix
from addcol import addcol
from check import check
import copy
n_DDS=5
d_DDS=4
o_DDS=10
p_DDS=2
young_digram = []
num_count = 0
rec_num = 0
ins_num = 0

file = open(r"d:\partition20.txt",'r')
for line in file:
    if( len(line) <2 ):
        continue
    line=trim(line)
    print(line)
    datas=line.split('+')
    for i in xrange(0,len(datas)):
        young_digram.append( int(datas[i]) )
        
    insert_tableau = insert_creat(young_digram,o_DDS,p_DDS)
    ins_num += len(insert_tableau)
    #print(insert_tableau)
    print('complete')
    record_tableau = record_creat(young_digram,n_DDS,d_DDS,o_DDS)
    rec_num += len(insert_tableau)
    #print( record_tableau)
    print('complete')

    for i in xrange( 0,len( insert_tableau ) ):
        #insert_tableau[i] = addcol(insert_tableau[i],o_DDS)
        for j in xrange( 0,len( record_tableau ) ):
            #print i,j
            #insert_temp = copy.deepcopy( insert_tableau[i] )
            #record_temp = copy.deepcopy( record_tableau[j] )
            #matrix_tem = young2matrix(insert_temp,record_temp,o_DDS,d_DDS,n_DDS,young_digram)
            #print check(matrix_tem)
            num_count +=1
            #break
        #break
    young_digram = []
    #break
print ins_num
print rec_num
print num_count
file.close()

