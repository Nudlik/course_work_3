import utils
from models import ReadJson, Transaction
from settings import PATH_TO_JSON


def main():
    transactions = ReadJson.load_json(PATH_TO_JSON)
    sorted_transactions = utils.sort_transactions(transactions)
    transactions_list = [Transaction(transaction) for transaction in sorted_transactions]
    for i in transactions_list:
        print(i, '\n')


if __name__ == '__main__':
    main()
