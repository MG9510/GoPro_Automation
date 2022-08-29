################################################################

from datetime import datetime

################################################################

# Extract Media List #
def extract_mediaList(gopro):

    try:
        media_list = gopro.wifi_command.get_media_list().flatten
        media_list.reverse()
        
        mediaFilenames = [val['n'] for val in media_list]
        mediaTimestamp = [val['cre'] for val in media_list]
        mediaDates = [datetime.fromtimestamp(int(val)) for val in mediaTimestamp]

        mediaDict = dict(zip(mediaFilenames, mediaDates))
        
        print('-'*75)
        print(f'Media Files --->')
        for key, val in mediaDict.items():
            print(f'{key} | {val}')
        print('-'*75)

    except:

        print('-'*75)
        print(f'No Media files in SD Card')
        mediaDict = {} 
        mediaFilenames = []
        print('-'*75)

    return mediaDict, mediaFilenames

################################################################