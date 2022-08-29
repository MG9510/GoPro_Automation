################################################################

from open_gopro import GoPro, Params, GoProResp

################################################################

def open_connection_gopro():

    gopro = GoPro()
    gopro.open()

    print('-'*75)
    print('Connection established !!!')
    print('-'*75)

    return gopro

################################################################