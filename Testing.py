################################################################

# Import Python Modules #
from asyncore import write
import json
from open_gopro import GoPro, Params, GoProResp

import os
import sys
sys.dont_write_bytecode = True
import pickle

################################################################

# Download Media Directory #
homeDir = os.getcwd()
pickleFile = homeDir + '\GoPro.pickle'
mediaDir = homeDir + '\Media'

################################################################
# CUSTOM FUNCTIONS #

# Establish GoPro connection #
def open_connection_gopro():

    gopro = GoPro()
    # gopro.open()

    print('-'*75)
    print('Connection established !!!')
    print('-'*75)

    return gopro


# Close GoPro connection #
def close_connection_gopro(gopro):

    gopro.close()

    print('-'*75)
    print('Connection closed !!!')
    print('-'*75)

    return None

################################################################

goPro = open_connection_gopro()

# print(goPro.__dict__['_response_parsers'])

fileHandle = open(pickleFile, 'w')
pickle.dump(goPro, fileHandle)

close_connection_gopro(goPro)

################################################################