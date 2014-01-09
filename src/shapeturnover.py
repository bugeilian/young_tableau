'''
Created on 2013-12-22

@author: Administrator
'''

def shape_turnover(young_digram,o_DDS):
    '''
    young_digram.insert( 0,o_DDS )
    young_digram_over = [ len(young_digram) ]
    for i in xrange(2,young_digram[0]+1):
        num = 0
        for j in xrange(0,len(young_digram) ):
            if young_digram[j]>= i:
                num+= 1
            else:
                break
        young_digram_over.append( num )  
        '''
    young_digram_over = [ len(young_digram) ]
    for i in xrange(2,young_digram[0]):
        num = 0
        for j in xrange(0,len(young_digram) ):
            if young_digram[j] >=i:
                num += 1
            else:
                break
        young_digram_over.append(num)
    return young_digram_over