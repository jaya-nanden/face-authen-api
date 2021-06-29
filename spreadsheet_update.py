import csv
import pandas as pd


def append_data(data_ls):
    with open('datasheet.csv', 'a') as f_object:
        writer_object = csv.writer(f_object)
        writer_object.writerow(data_ls)
        f_object.close()


def read_data():
    df = pd.read_csv('datasheet.csv')
    # print(df.columns)
    # print(len(df))
    # print(df['status'])

    # data_dict = {}
    # with open("datasheet.csv", 'r') as file:
    #     csv_file = csv.DictReader(file)
    #     i = 0
    #     for row in csv_file:
    #         data_dict[i] = row
    #         # print(dict(row))
    #         i += 1

    return df
