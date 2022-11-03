

class MyFlute:
    """ """
    def __init__(self, bore_length, bore_diameter, wall_thickness, dl_factor, blank_length, blank_height,
                 single_width, drone_width, drone_bore_center):
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

    def print_sizing(self):
        print(f'----------------------------')
        print(f'BLANK LENGTH: {self.blank_length:.2f}')
        print(f'BLANK HEIGHT: {self.blank_height:.2f}')
        print(f'BORE LENGTH: {self.bore_length:.2f}')
        print(f'SINGLE WIDTH: {self.single_width:.2f}')
        print(f'DRONE_WIDTH: {self.drone_width:.2f}')
        print(f'DRONE_BORE_CENTER: {self.drone_bore_center:.3f}')
        print(f'----------------------------')

    @classmethod
    def get_blank_sizing(cls):
        bore_diameter = float(input('Enter bore diameter: '))
        wall_thickness = float(input('Enter wall thickness: '))
        dl_factor = float(input('Enter wall D/L ratio: '))
        fudge_factor = float(input('Enter fudge factor: '))
        bore_length = bore_diameter * dl_factor
        blank_length = bore_length + 7
        blank_height = bore_diameter + wall_thickness + fudge_factor
        single_width = bore_diameter + (wall_thickness * 2) + fudge_factor
        drone_width = (bore_diameter * 2) + (wall_thickness * 4)
        drone_bore_center = (bore_diameter / 2) + wall_thickness
        return cls(bore_length, bore_diameter, wall_thickness, dl_factor, blank_length, blank_height,
                   single_width, drone_width, drone_bore_center)

    def print_fh_placement(self):
        for index, holes in enumerate(self.fh_values):
            print(f'FH_{index+1}: {holes:.2f}')

    def get_finger_hole_placements(self):
        self.bore_length = float(input('Enter the actual bore length: '))
        finger_hole_percents = [.68, .62, .56, .48, .40, .33]
        for percent in finger_hole_percents:
            self.fh_values.append(percent * self.bore_length)

