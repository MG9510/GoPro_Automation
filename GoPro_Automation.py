################################################################

# Import Python Modules #
from flask import Flask, render_template, redirect, url_for, request
from open_gopro import GoPro, Params, GoProResp
from goprocam import GoProCamera

from datetime import datetime
import time
import os
import sys
sys.dont_write_bytecode = True

################################################################

# Download Media Directory #
homeDir = os.getcwd()
mediaDir = homeDir + '\Media'

################################################################
# CUSTOM FUNCTIONS #

# Establish GoPro connection #
def open_connection_gopro():

    gopro = GoPro()
    gopro.open()

    print('-'*75)
    print('Connection established !!!')
    print('-'*75)

    return gopro


# Take Photo #
def take_photo(gopro, photo_type):

    if photo_type == 'Photo':
        gopro.ble_command.load_preset(Params.Preset.PHOTO)
    elif photo_type == 'Max Photo':
        gopro.ble_command.load_preset(Params.Preset.MAX_PHOTO)
    elif photo_type == 'Night Photo':
        gopro.ble_command.load_preset(Params.Preset.NIGHT_PHOTO)

    time.sleep(1)

    gopro.ble_command.set_shutter(Params.Shutter.ON)
    gopro.ble_command.set_shutter(Params.Shutter.OFF)

    print('-'*75)
    print(f'{photo_type} taken !!!')
    print('-'*75)

    mediaFiles, mediaFilenames = extract_mediaList(gopro)
    download_files('Last', mediaFilenames)

    return None


# Take Video - Set duration#
def take_video(gopro, video_type, duration):

    if video_type == 'Standard':
        gopro.ble_command.load_preset(Params.Preset.STANDARD)
    elif video_type == 'Cinematic':
        gopro.ble_command.load_preset(Params.Preset.CINEMATIC)
    elif video_type == 'Activity':
        gopro.ble_command.load_preset(Params.Preset.ACTIVITY)
    elif video_type == 'Slow Motion':
        gopro.ble_command.load_preset(Params.Preset.SLOMO_EB)

    time.sleep(1)

    gopro.ble_command.set_shutter(Params.Shutter.ON)
    time.sleep(duration)
    gopro.ble_command.set_shutter(Params.Shutter.OFF)

    print('-'*75)
    print(f'{video_type} Video taken !!!')
    print('-'*75)

    mediaFiles, mediaFilenames = extract_mediaList(gopro)
    download_files('Last', mediaFilenames)

    return None


# Start Video #
def start_video(gopro, video_type):

    if video_type == 'Standard':
        gopro.ble_command.load_preset(Params.Preset.STANDARD)
    elif video_type == 'Cinematic':
        gopro.ble_command.load_preset(Params.Preset.CINEMATIC)
    elif video_type == 'Activity':
        gopro.ble_command.load_preset(Params.Preset.ACTIVITY)
    elif video_type == 'Slow Motion':
        gopro.ble_command.load_preset(Params.Preset.SLOMO_EB)

    time.sleep(1)

    gopro.ble_command.set_shutter(Params.Shutter.ON)

    print('-'*75)
    print(f'{video_type} Video recording started ...')

    return None


# Stop Video #
def stop_video(gopro):

    gopro.ble_command.set_shutter(Params.Shutter.OFF)

    print(f'Video recording stopped ...')
    print('-'*75)

    mediaFiles, mediaFilenames = extract_mediaList(gopro)
    download_files('Last', mediaFilenames)

    return None


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


# Download Media files #
def download_files(downloadType, mediaFilenames):

    if downloadType == 'Last':

        gopro.wifi_command.download_file(mediaFilenames[0])

    else:

        for filename in mediaFilenames:
            gopro.wifi_command.download_file(filename)

    print('-'*75)
    print(f'Downloaded {downloadType} media file !!!')
    print('-'*75)

    return None


# Close GoPro connection #
def close_connection_gopro(gopro):

    gopro.close()

    print('-'*75)
    print('Connection closed !!!')
    print('-'*75)

    return None


# Delete Media #
def delete_mediaFile(gopro, deleteType):
    
    if gopro != '-':
        close_connection_gopro(gopro)

    try:

        print('-'*75)
        goProCam = GoProCamera.GoPro()
        print('-'*75)

        if deleteType in ['last', 'all']:
            
            goProCam.delete(deleteType)

        print('-'*75)
        print(f'{deleteType.capitalize()} media deleted !!! ')
        print('-'*75)

    except:

        print('*** ERROR DELETING FILES ***')

    gopro = open_connection_gopro()

    return gopro

################################################################

gopro = open_connection_gopro()

################################################################

app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"

################################################################

# HOME PAGE #

@app.route('/')
def homePage():

    return render_template('1_Home_Page.html')

################################################################

# CLICK PHOTO #

@app.route('/takePhoto/<photoType>')
def takePhoto(photoType):

    take_photo(gopro, photoType)

    return render_template('1_Home_Page.html')


################################################################

# START VIDEO REC. #

@app.route('/startVideo/<videoType>')
def startVideo(videoType):

    start_video(gopro, videoType)

    return render_template('2_Recording.html')

################################################################

# START VIDEO REC. #

@app.route('/stopVideo')
def stopVideo():

    stop_video(gopro)

    return render_template('1_Home_Page.html')

################################################################

# START VIDEO REC. #

@app.route('/disconnect')
def disconnect():

    close_connection_gopro(gopro)

    return render_template('1_Home_Page.html')

################################################################

# take_video(gopro, 'Cinematic', 5)

################################################################

# start_video(gopro, 'Activity')
# time.sleep(10)
# stop_video(gopro)

################################################################

# mediaFiles, mediaFilenames = extract_mediaList(gopro)
# download_files('All', mediaFilenames)

################################################################

# gopro = delete_mediaFile('-', 'all')

################################################################

# close_connection_gopro(gopro)

################################################################

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=int(os.environ.get('PORT', 8080)), debug=False)

################################################################