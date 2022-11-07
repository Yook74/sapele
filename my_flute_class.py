import csv
from math import sqrt
import linecache


class MyFlute:
    """ """
    def __init__(self, bore_length, bore_diameter, wall_thickness, dl_factor, blank_length, blank_height,
                 single_width, drone_width, drone_bore_center, key, octave, tuner_ref):
        self.bore_length = bore_length
        self.bore_diameter = bore_diameter
        self.wall_thickness = wall_thickness
        self.dl_factor = dl_factor
        self.blank_length = blank_length
        self.blank_height = blank_height
        self.single_width = single_width
        self.drone_width = drone_width
        self.drone_bore_center = drone_bore_center
        self.fh_values = []
        self.key = key
        self.octave = octave
        self.fudge_factor = float()
        self.tuner_ref = int(tuner_ref)

    def print_sizing(self):
        print(f'----------------------------')
        print(f'BLANK LENGTH: {self.blank_length:.2f}')
        print(f'BLANK HEIGHT: {self.blank_height:.2f}')
        print(f'BORE LENGTH: {self.bore_length:.2f}')
        print(f'SINGLE WIDTH: {self.single_width:.2f}')
        print(f'DRONE_WIDTH: {self.drone_width:.2f}')
        print(f'DRONE_BORE_CENTER: {self.drone_bore_center:.3f}')
        print(f'----------------------------')

    def get_tuner_ref(self):
        self.tuner_ref = input('Enter tuner Reference in Hz: (default = 440)')
        if not self.tuner_ref:
            self.tuner_ref = 440
        ambient_temp = input('Enter the ambient temperature in Deg (default = 72): ')
        if not ambient_temp:
            ambient_temp = float(72)
        offset = (12600.535 * sqrt((float(ambient_temp) + 459.4) / 459.4)) / 30.80006182 - 440
        return float(self.tuner_ref) + offset

    def get_flute_key(self):
        return self.key

    def get_flute_octave(self):
        return self.octave


    @classmethod
    def get_blank_sizing(cls):
        bore_diameter = float(input('Enter bore diameter: '))
        wall_thickness = float(input('Enter wall thickness: '))
        dl_factor = float(input('Enter wall D/L ratio: '))
        fudge_factor = float(input('Enter fudge factor: '))
        bore_length = bore_diameter * dl_factor
        blank_length = bore_length + 7
        blank_height = (bore_diameter/2) + wall_thickness + fudge_factor
        single_width = bore_diameter + (wall_thickness * 2) + fudge_factor
        drone_width = (bore_diameter * 2) + (wall_thickness * 4)
        drone_bore_center = (bore_diameter / 2) + wall_thickness
        tuner_ref = int(input('Enter tuner Reference: '))

        if not tuner_ref:
            tuner_ref = 440

        return cls(bore_length, bore_diameter, wall_thickness, dl_factor, blank_length, blank_height,
                   single_width, drone_width, drone_bore_center, tuner_ref)

    def print_fh_placement(self):
        for index, holes in enumerate(self.fh_values):
            print(f'FH_{index+1}: {holes:.2f}')


    @classmethod
    def flute_key(cls):
        key = input('Enter the flute Key: ')
        octave = input('Enter the key Octave (default = 4): ')
        tuner_ref = (input('Enter tuner Reference in Hz (default = 440): '))

        if not tuner_ref:
            tuner_ref = '440'

        if not octave:
            octave = '4'

        my_key = key + '_' + octave
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
                    blank_height = (bore_diameter/2) + wall_thickness + fudge
                    single_width = bore_diameter + (wall_thickness * 2) + fudge
                    drone_width = (bore_diameter * 2) + (wall_thickness * 4)
                    drone_bore_center = (bore_diameter / 2) + wall_thickness
                    return cls(bore_length, bore_diameter, wall_thickness, dl_factor, blank_length, blank_height,
                               single_width, drone_width, drone_bore_center, key, octave, tuner_ref)

        if not row:
            bore_diameter = float(input('Enter bore diameter: '))
            wall_thickness = float(input('Enter wall thickness: '))
            dl_factor = float(input('Enter wall D/L ratio: '))
            fudge_factor = float(input('Enter fudge factor: '))
            bore_length = bore_diameter * dl_factor
            blank_length = bore_length + 7
            blank_height = (bore_diameter/2) + wall_thickness + fudge_factor
            single_width = bore_diameter + (wall_thickness * 2) + fudge_factor
            drone_width = (bore_diameter * 2) + (wall_thickness * 4)
            drone_bore_center = (bore_diameter / 2) + wall_thickness
            return cls(bore_length, bore_diameter, wall_thickness, dl_factor, blank_length, blank_height,
                       single_width, drone_width, drone_bore_center, key, octave, tuner_ref)

    def get_finger_hole_placements(self):
        self.fh_values.clear()
        self.bore_length = float(input('Enter the actual bore length: '))
        finger_hole_percents = [.685, .62, .55, .475, .39, .305]
        for percent in finger_hole_percents:
            self.fh_values.append(percent * self.bore_length)

