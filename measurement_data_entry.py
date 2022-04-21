"""This script is used to gather flute measurement data of a finished flute, prior top placing the finger holes"""


def get_flute_dimension(dimension_name: str, default=None) -> float:
    """Get value for Dimension Name in inches"""

    while True:
        value = input(f'Enter the {dimension_name}: ')

        if not value:
            return default

        try:
            return float(value)
        except ValueError:
            print('Invalid Input')


def main():
    # TODO I want to pull percentages based on key and octave and scale from the database

   key = get_flute_dimension('Total Length')
   octave = get_flute_dimension('Total Length')
   total_length = get_flute_dimension('Total Length')
   bore_length = get_flute_dimension('Bore Length')
   bore_diameter = get_flute_dimension('Bore Diameter')
   tsh_width = get_flute_dimension('TSH Width')
   tsh_length = get_flute_dimension('TSH Length')
   flue_depth = get_flute_dimension('Flue Depth')
   wall_thickness = get_flute_dimension('wall_thickness')


if __name__ == '__main__':
        main()