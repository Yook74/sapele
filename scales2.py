import pandas as pd


def main(my_key):
    file_path = r'C:\Users\carl.young\Documents\sapele\csv_stuff\notes_table.csv'

    fp = r'C:\Users\carl.young\Documents\sapele\csv_stuff\intervals.csv'

    df = pd.read_csv(file_path)

    row = df[df['0'].str.contains('(D)', regex=False)].to_string(index=False, justify='center', header=None)

    row = (row.split())

    df2 = pd.read_csv(fp)

    row2 = df2[df2['0'].str.contains('Minor_Pent', regex=False)].to_string(index=False, justify='center', header=None)

    row2 = row2.split()

    for num in range(1, 7, 1):
        if row2[num] != "NaN":
            print('FH:', [num], ': ', row[int(row2[num])])
    print()



