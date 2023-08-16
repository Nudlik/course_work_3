import datetime


class Transaction:
    """
    Класс для работы с транзакциями
    """

    def __init__(self, transaction: dict):
        self.__date: str = transaction.get('date')
        self.__description: str = transaction.get('description')
        self.__from: str = transaction.get('from')
        self.__id: int = transaction.get('id')
        self.__operation_amount: dict = transaction.get('operationAmount')
        self.__state: str = transaction.get('state')
        self.__to: str = transaction.get('to')
        self.__amount: int = self.__operation_amount.get('amount')
        self.__code: str = self.__operation_amount.get('currency').get('code')
        self.__name: str = self.__operation_amount.get('currency').get('name')

    def __repr__(self):
        correct_amount = str(self.__operation_amount).replace("\'", "\"")
        return f'{self.__class__.__name__}(date={self.__date}, ' \
               f'description="{self.__description}", ' \
               f'from="{self.__from}", ' \
               f'id="{self.__id}", ' \
               f'operation_amount="{correct_amount}", ' \
               f'state="{self.__state}", ' \
               f'to="{self.__to}")'

    def __str__(self):
        """
        # Пример вывода для одной операции:
        14.10.2018 Перевод организации
        Visa Platinum 7000 79** **** 6361 -> Счет **9638
        82771.72 руб
        """
        return f'{self.__get_date()} {self.__description}\n' \
               f'{self.__get_from()}{self.__mask_cards(self.__from) or ""} -> ' \
               f'{self.__get_to()} {self.__mask_cards(self.__to)}\n' \
               f'{self.__amount} {self.__name}'

    @staticmethod
    def __mask_cards(card):
        """
        Шифрует номера карт
        :param card: номер карточки
        :return: скрытый номер
        """
        if card is None:
            return ''
        card = card.split()[-1]
        if card.isdigit():
            if len(card) == 16:
                return f'{card[:4]} {card[4:6]}** **** {card[-4:]}'
            elif len(card) == 20:
                return f'**{card[-4:]}'

    def __get_date(self):
        """
        Удобный формат даты
        :return: время день месяц год
        """
        date_format = datetime.datetime.strptime(self.__date, '%Y-%m-%dT%H:%M:%S.%f')
        date = date_format.strftime('%d.%m.%Y')
        return date

    def __get_from(self):
        if self.__from is None:
            return 'Неизвестно'
        return "".join(self.__from.split()[:-1])

    def __get_to(self):
        return "".join(self.__to.split()[:-1])
