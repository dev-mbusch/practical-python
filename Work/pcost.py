# pcost.py
#
# Exercise 1.27

import csv
import sys


def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        print(headers)

        total_cost = 0
        for row in rows:
            try:
                total_cost += int(row[1]) * float(row[2])
            except ValueError:
                print('The given file has missing fields!')

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = r'Data/portfolio.csv'

cost = portfolio_cost(r'Data/portfolio.csv')
print(f'Total Cost: {cost}')
