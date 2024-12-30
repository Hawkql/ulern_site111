import csv 
import pandas as pd
file_name = 'vacancies_2024.csv'


def name_csv(row):
    name_profecion = ['игры','unity','game','unreal']
    for name_game in name_profecion:
        for coulumns in row:
            coulumns= coulumns['name']
            if name_game in coulumns:
                print(coulumns)
      

def reading():
    with open(file_name,'r',encoding='utf-8')as f:
        df = pd.read_csv(f)


        for row in df:
           name_csv(row)

def main():
    reading()

if __name__ == '__main__':
    main()