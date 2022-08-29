################################################################

# Download Media files #
def download_files(gopro, downloadType, mediaFilenames):

    if downloadType == 'Last':

        gopro.wifi_command.download_file(mediaFilenames[0])

    else:

        for filename in mediaFilenames:
            gopro.wifi_command.download_file(filename)

    print('-'*75)
    print(f'Downloaded {downloadType} media file !!!')
    print('-'*75)

    return None

################################################################