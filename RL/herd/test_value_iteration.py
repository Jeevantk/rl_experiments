'''
Test value iteration

Created on 24 Sep 2009

@author: joh
'''

from value_methods import value_iteration

if __name__ == '__main__':
    V = value_iteration(gamma=0.9, sweeps=10)
    
    def vcmp(v1, v2):
        #print 'vcmp',v1,v2
        return cmp(v1[1], v2[1])
        
    V = sorted(V.items(), cmp=vcmp)
    
    for v in V:
        print v
    
    
