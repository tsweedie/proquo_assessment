import os
import sys

import pandas as pd
from datetime import datetime
from datetime import date


def calculate_age(born):
    born = datetime.strptime(born, '%d-%m-%Y').date()
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def process_file(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError

    df = pd.read_csv(filename, sep='|', skipinitialspace=True)
    df['age'] = df['date-of-birth'].apply(calculate_age)
    df = df.sort_values(by=['date-of-birth'])

    print(df.to_string(index=False))
    print('Average Age', df['age'].sum()/df.shape[0])


if __name__ == '__main__':
    try:
        process_file(sys.argv[1])
    except IndexError:
        print("not enough arguments to run program, please specify filename")
    except FileNotFoundError:
        print('file \'%s\' doesn\'t exist' % sys.argv[1])

# python file_reading.py data/dob.txt
