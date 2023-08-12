import utils
from models.transaction import Transaction
from models.readjson import ReadJson
from settings import PATH_TO_JSON


def main():
    transactions_load = ReadJson.load_json(PATH_TO_JSON)
    transactions_sorted = utils.sort_transactions(transactions_load)
    transactions_list = [Transaction(transaction) for transaction in transactions_sorted]
    [print(i, '\n') for i in transactions_list]


if __name__ == '__main__':
    main()
