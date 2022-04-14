"""Returns Top and Bottom hole Recommendations"""

def get_bore_length() -> float:
    """Get Bore Length"""
    while True:
        value = input(f'Enter the bore length: ')
        try:
            return float(value)
        except ValueError:
            print('Invalid Input')


def get_hole_placements(bore_length: float):
    """Get top finger hole placement"""
    return bore_length - (bore_length * .315), bore_length * .315


def main():
    while True:
        bore_length = get_bore_length()
        max_distance, min_distance = get_hole_placements(bore_length)
        print(f'\nMAX: {max_distance:.2f} inches\nMIN: {min_distance:.2f} inches\n')


if __name__ == '__main__':
    main()
