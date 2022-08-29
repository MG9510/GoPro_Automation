################################################################

# Import Python Modules #
from flask import Flask, render_template, redirect, url_for, request
import os
import sys
sys.dont_write_bytecode = True


################################################################
# CUSTOM FUNCTIONS #

from GoPro_1_OpenConnection import open_connection_gopro
from GoPro_2_CloseConnection import close_connection_gopro
from GoPro_3_CapturePhoto import take_photo
from GoPro_4_CaptureVideo import take_video, start_video, stop_video
from GoPro_5_MediaList import extract_mediaList
from GoPro_6_DownloadMedia import download_files
from GoPro_7_DeleteMedia import delete_mediaFile

################################################################

# Download Media Directory #
homeDir = os.getcwd()
mediaDir = homeDir + '\Media'

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

# Disconnect GoPro #

@app.route('/disconnect')
def disconnect():

    close_connection_gopro(gopro)

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

# Download & Delete Media Files #

@app.route('/downloadDeleteMedia')
def downloadDelete():

    mediaFiles, mediaFilenames = extract_mediaList(gopro)
    download_files(gopro, 'All', mediaFilenames)
    delete_mediaFile('all')

    return render_template('1_Home_Page.html')

################################################################

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=int(os.environ.get('PORT', 8080)), debug=False)

################################################################