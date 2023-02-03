import csv
import sys
from typing import List, Dict

def spend_points(points_to_spend: int, transactions: List[Dict[str, str]]) -> Dict[str, int]:
    final_points = {}
    transactions = sorted(transactions, key=lambda x: x['timestamp'])
    total=0
    for transaction in transactions:
        payer = transaction['payer']
        if payer not in final_points:
            final_points[payer] = 0
        final_points[payer] += int(transaction['points'])
        total+=int(transaction['points'])

    for key, val in final_points.items():
        if val < 0:
            return "Negative Points"

    if points_to_spend > total:
        return "Not Enough Points"

    for transaction in transactions:
        payer = transaction['payer']
        points = min(final_points[payer], int(transaction['points']))
        if(points >= points_to_spend):
            final_points[payer] -= points_to_spend
            return final_points
        else:
            points_to_spend = points_to_spend - points
            final_points[payer] -= points
    return final_points

if __name__ == '__main__':
    filename = 'transactions.csv'
    points_to_spend = int(sys.argv[1])
    transactions = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    result = spend_points(points_to_spend, transactions)
    print(result)