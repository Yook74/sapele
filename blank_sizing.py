"""Returns Blank sizing information based on entered bore diameter and wall thickness"""


def get_dimension(dimension_name: str, default=None) -> float:
    """Get value for Dimension Name in inches"""
    while True:
        value = input(f'Enter the {dimension_name}: ')

        if not value:
            return default

        try:
            return float(value)
        except ValueError:
            print('Invalid Input')


def get_blank_height(bore_diameter: float, wall_thickness: float) -> float:
    """Calculate and return the required blank size for a single bore blank width"""
    return bore_diameter/2 + wall_thickness


def get_blank_single(bore_diameter: float, wall_thickness: float) -> float:
    """Calculate and return the required blank size for a single bore blank width"""
    return bore_diameter + (wall_thickness * 2)


def get_blank_drone(bore_diameter: float, wall_thickness: float) -> float:
    """Calculate and return the required blank size for a double bore blank width"""
    return (bore_diameter * 2) + (wall_thickness * 3)


def get_blank_length(bore_diameter: float, dl_factor: float) -> float:
    """Calculate and return the required blank size for a double bore blank width"""
    return bore_diameter * dl_factor


def main():

    bore_diameter = get_dimension('bore diameter')
    wall_thickness = get_dimension('wall thickness')
    dl_factor = get_dimension('D/L Factor', default=18)

    blank_height = get_blank_height(bore_diameter, wall_thickness)
    blank_single_width = get_blank_single(bore_diameter, wall_thickness)
    blank_drone_width = get_blank_drone(bore_diameter, wall_thickness)
    bore_length = get_blank_length(bore_diameter, dl_factor)
    blank_length = bore_length + 7

    print(f'----------------------------')
    print(f'BLANK LENGTH: {blank_length:.2f} inches')
    print(f'BLANK HEIGHT: {blank_height} inches')
    print(f'BORE LENGTH: {bore_length:.2f} inches')
    print(f'SINGLE WIDTH: {blank_single_width:.2f} inches')
    print(f'DRONE WIDTH: {blank_drone_width:.2f} inches')
    print(f'----------------------------\n')


if __name__ == '__main__':
    main()
