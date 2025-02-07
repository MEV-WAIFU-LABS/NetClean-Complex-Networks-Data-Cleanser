#!/usr/bin/env python
 

import os
from constants import SUBFOLDERS, FEATURES  


def create_input_files(subfolder):
    return '../../output/vectors_proc/' + subfolder + '.data'


def create_output_files():

    out = '../../output/'
    if not os.path.exists(out):
        os.makedirs(out) 
    out_v = out + 'vectors_together/'      
    if not os.path.exists(out_v):
        os.makedirs(out_v)     
    return out_v + 'together.data'




if __name__ == '__main__':

    output_file = create_output_files()

    # Loop saving the values for each file
    for subfolder in SUBFOLDERS:  
        input_file  = create_input_files(subfolder)

        print 'Processing ' + input_file + ' ...'
        tempfile = open(input_file, 'r')
        aux = tempfile.read()
        outfile = open(output_file, 'a')
        outfile.write(aux)
        tempfile.close()
        outfile.close()
          
    print '\nDone!!!'
