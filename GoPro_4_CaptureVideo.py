################################################################

from open_gopro import GoPro, Params, GoProResp
import time

################################################################

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

    return None

################################################################