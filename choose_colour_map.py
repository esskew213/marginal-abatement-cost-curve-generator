SUPPORTED_COLOUR_MAPS = ['gnuplot2', 'jet', 'rainbow', 'gist_rainbow', 'terrain', 'turbo', 'brg', 'nipy_spectral']


def choose_colour_map():
    user_colour_map = input('Please choose a colour map for your MAC curve or hit Enter for default.'
                            '\nHere are some exotic choices: ' + ', '.join(cmap for cmap in SUPPORTED_COLOUR_MAPS) + '.\nYour selection: ')
    if user_colour_map in SUPPORTED_COLOUR_MAPS:
        return user_colour_map
    elif user_colour_map == '':
        return 'jet'
    else:
        print('Invalid selection.')
        return choose_colour_map()