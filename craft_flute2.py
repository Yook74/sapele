import csv
from math import sqrt


def get_sizing(key, octave) -> str:
    my_key = key + '_' + str(octave)
    with open('records/initialSetup.csv') as data:
        my_file = csv.DictReader(data)
        for row in my_file:
            if row['Key'] == my_key:
                bore_diameter = float(dict.pop(row, 'bore'))
                wall_thickness = float(dict.pop(row, 'wall'))
                dl_factor = float(dict.pop(row, 'd/l'))
                fudge = float(dict.pop(row, 'fudge'))
                bore_length = bore_diameter * dl_factor
                blank_length = bore_length + 7
                blank_height = (bore_diameter / 2) + wall_thickness + fudge
                single_width = bore_diameter + (wall_thickness * 2) + fudge
                drone_width = (bore_diameter * 2) + (wall_thickness * 3) + fudge
                drone_bore_center = (bore_diameter / 2) + wall_thickness

        return str(f'BLANK LENGTH: {blank_length:.2f}'
                   f'\nBLANK HEIGHT: {blank_height:.2f}'
                   f'\n BORE LENGTH: {bore_length:.2f}'
                   f'\n    BORE DIA: {bore_diameter:.3f}'
                   f'\n        WALL: {wall_thickness:.3f}'
                   f'\nSINGLE WIDTH: {single_width:.2f}'
                   f'\n DRONE WIDTH: {drone_width:.2f}'
                   f'\nDRONE CENTER: {drone_bore_center:.3f}')


def get_ref_offset(temp, tuner_ref):
    offset = (12600.535 * sqrt((float(temp) + 459.4) / 459.4)) / 30.80006182 - 440
    return float(tuner_ref) + offset