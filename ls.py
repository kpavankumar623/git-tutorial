import pdb

# list of num and key exits=> True
#list of num and key exits => False
#if list is empty => False
#if key is None => False

import logging
import sys
logging.basicConfig(level = logging.ERROR,filename = "/home/edyoda/python1/test.log",format="%(asctime)s-%(levelname)s-%(message)s")
def linear_search(l,key):
    logging.debug("Success entered to the function")
    for value in l:
        if value == key:
            return True
    else:
            return False

#pdb.set_trace()

#l = [10,20,30,40,50]
#key = 50
key=int(sys.argv[1])
l=sys.argv[2].split(',')
result = linear_search(l,key)
logging.error("Success completed  the function")
print(result)
print(sys.argv)


