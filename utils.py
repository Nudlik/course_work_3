def sort_transactions(transactions, count=5, sort_by='date', state='EXECUTED'):
    """
    Сортировка списка со словарями
    :param transactions: список словарей
    :param count: какая нужна длинна
    :param sort_by: сортировка по
    :param state: условие EXECUTED - пройденные операции, CANCELED - отмененныу
    :return: список отсортированных словарей
    """
    return sorted(transactions, key=lambda x: x[sort_by] if x and x['state'] == state else '', reverse=True)[:count]


if __name__ == '__main__':
    pass
