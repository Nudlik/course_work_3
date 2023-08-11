import os
import json


class Transaction:

    def __init__(self, transaction: dict):
        self.date: str = transaction.get('date')
        self.description: str = transaction.get('description')
        self.fromm: str = transaction.get('from', 'Неизвестно')
        self.id_transaction: int = transaction.get('id')
        self.operation_amount: dict = transaction.get('operationAmount')
        self.state: str = transaction.get('state')
        self.to: str = transaction.get('to')
        self.amount: int = transaction.get('operationAmount').get('amount')
        self.code: str = transaction.get('operationAmount').get('currency').get('code')
        self.name: str = transaction.get('operationAmount').get('currency').get('name')

    def __repr__(self):
        return f'{self.__class__.__name__}(data={self.date}, description={self.description}, fromm={self.fromm}, ' \
               f'id_transaction={self.id_transaction}, operation_amount={self.operation_amount}, state={self.state}, ' \
               f'to={self.to})'

    def __str__(self):
        """
        # Пример вывода для одной операции:
        14.10.2018 Перевод организации
        Visa Platinum 7000 79** **** 6361 -> Счет **9638
        82771.72 руб
        """
        return f'{self.date.split("T")[0]} {self.description}\n' \
               f'{"".join(self.fromm.split()[:-1]) or "Отправитель"} {self.mask_cards(self.fromm)} -> ' \
               f'{"".join(self.to.split()[:-1])} {self.mask_cards(self.to)}\n' \
               f'{self.amount} {self.name}'

    @staticmethod
    def mask_cards(card):
        if card == 'Неизвестно':
            return card
        card = card.split()[-1]
        if card.isdigit():
            if len(card) == 16:
                return f'{card[:4]} {card[5:7]}** **** {card[-4:]}'
            elif len(card) == 20:
                return f'**{card[-4:]}'


class ReadJson:

    @staticmethod
    def load_json(path):
        if not os.path.exists(path):
            return None
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data


if __name__ == '__main__':
    trans = Transaction()
    print(trans)
