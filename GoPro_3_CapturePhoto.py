################################################################

from open_gopro import GoPro, Params, GoProResp
import time

################################################################

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

    return None


################################################################