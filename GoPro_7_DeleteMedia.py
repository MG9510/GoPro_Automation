################################################################

from goprocam import GoProCamera

################################################################

# Delete Media #
def delete_mediaFile(deleteType):

    print('-'*75)
    goProCam = GoProCamera.GoPro()
    print('-'*75)

    if deleteType in ['last', 'all']:
        
        goProCam.delete(deleteType)

    print('-'*75)
    print(f'{deleteType.capitalize()} media deleted !!! ')
    print('-'*75)

    return None

################################################################
