################################################################

from open_gopro import GoPro, Params, GoProResp

################################################################

# Close GoPro connection #
def close_connection_gopro(gopro):

    gopro.close()

    print('-'*75)
    print('Connection closed !!!')
    print('-'*75)

    return None


################################################################