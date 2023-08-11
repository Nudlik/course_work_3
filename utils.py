def sort_transactions(transactions, count=5, sort_by='date', state='state'):
    return sorted(transactions, key=lambda x: x[sort_by] if x and x[state] == 'EXECUTED' else '', reverse=True)[:count]


if __name__ == '__main__':
    pass
