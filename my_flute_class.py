import csv
from math import sqrt
import pandas as pd
import os


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
        self.fh_delta_values = []
        self.key = key
        self.octave = octave
        self.fudge_factor = float()
        self.tuner_ref = int(tuner_ref)

    def print_sizing(self):
        print(f'----------------------------')
        print(f'BLANK LENGTH: {self.blank_length:.2f}')
        print(f'BLANK HEIGHT: {self.blank_height:.2f}')
        print(f'BORE LENGTH: {self.bore_length:.2f}')
        print(f'BORE DIAMETER: {self.bore_diameter:.3f}')
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

    def print_fh_placement(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        fh = []
        fhp = []
        for index, holes in enumerate(self.fh_values):
            fh.append(index+1)
            fhp.append(f'{holes:.2f}')
        for num in range(len(fh)-1, -1, -1):
            print(f'FH_{fh[num]}: {fhp[num]}')


    @classmethod
    def flute_key(cls):
        keys = ['C', 'B', 'Bb', 'A#', 'A', 'Ab', 'G#', 'G', 'Gb', 'F#', 'F', 'E', 'Eb', 'D#', 'D', 'Db', 'C#']
        check = False
        key = ''
        while not check:
            key = input('Enter the flute Key: ').upper()
            if not len(key) == 1:
                key = key[0] + (key[1].lower())
            if key not in keys:
                print('Invalid Key...')
                check = False
            else:
                if key == 'Bb':
                    key = 'A#'
                if key == 'Ab':
                    key = 'G#'
                if key == 'Gb':
                    key = 'F#'
                if key == 'Eb':
                    key = 'D#'
                if key == 'Db':
                    key = 'C#'
                check = True

        octave = input('Enter the key Octave (default = 4): ')
        tuner_ref = (input('Enter tuner Reference in Hz (default = 440): '))

        if not tuner_ref:
            tuner_ref = '440'

        if not octave:
            octave = '4'

        my_key = key + '_' + octave
        with open('csv_stuff/initialSetup.csv') as data:

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
                    drone_width = (bore_diameter * 2) + (wall_thickness * 3) + fudge
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
            drone_width = (bore_diameter * 2) + (wall_thickness * 3) + fudge_factor
            drone_bore_center = (bore_diameter / 2) + wall_thickness
            return cls(bore_length, bore_diameter, wall_thickness, dl_factor, blank_length, blank_height,
                       single_width, drone_width, drone_bore_center, key, octave, tuner_ref)

    def get_finger_hole_placements(self):
        file_path = r'C:\Users\carl.young\Documents\sapele\csv_stuff\fh_percents.csv'
        bore = input('\nEnter the actual bore length: ')
        if bore:
            while True:
                self.fh_values.clear()
                selection = (input('\n(1) Get FHP Values, (2) Update FHP Values: \n'))
                if not selection:
                    break
                df = pd.read_csv(file_path)
                fhp = df[(df['key'] == self.key) & (df['octave'] == int(self.octave))]
                fhp_list = list(fhp[['fh_1', 'fh_2', 'fh_3', 'fh_4', 'fh_5', 'fh_6', 'fh_7']].values)[0]
                for percent in fhp_list:
                    if percent != 0:
                        self.fh_values.append(percent * float(bore))
                self.print_fh_placement()

                update_holes = input('\nUpdate Holes? ')
                if update_holes:
                    df = pd.read_csv(file_path)
                    idx = (df[(df['key'] == self.key) & (df['octave'] == int(self.octave))].index[0])
                    hole = input('\nEnter hole number: ')
                    hole = int(hole) - 1
                    new_pos = input('New Value: ')
                    df.loc[idx, f'fh_{hole+1}'] = (float(new_pos) / float(bore))
                    df.to_csv(file_path, index=False)
                    self.fh_values[int(hole)] = float(new_pos)
                    print()
                    self.print_fh_placement()

                if not selection:
                    break



