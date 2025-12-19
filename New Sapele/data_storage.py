import csv
import pandas as pd

def append_to_csv(file_path, row_data):
    file_name = f'{file_path}'
    with open(file_name, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(row_data)


def create_csv_file(file_path, csv_labels):
    file_name = f'{file_path}'
    with open(file_name, 'w',  newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(csv_labels)


def update_file(file_path, column_name, order_id, target, value):
    df = pd.read_csv(file_path)
    df.loc[df[column_name] == order_id, target] = value
    df.to_csv(file_path, index=False)
