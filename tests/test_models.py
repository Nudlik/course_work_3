import pytest
from models import Transaction, ReadJson
import os


GOOD = {'date': '2019-12-07T06:17:14.634890',
        'description': 'Перевод организации',
        'from': 'Visa Classic 2842878893689012',
        'id': 114832369,
        'operationAmount': {'amount': '48150.39',
                            'currency': {'code': 'USD', 'name': 'USD'}},
        'state': 'EXECUTED',
        'to': 'Счет 35158586384610753655'}

NOT_GOOD = {'date': '2019-12-08T22:46:21.935582',
            'description': 'Открытие вклада',
            'id': 863064926,
            'operationAmount': {'amount': '41096.24',
                                'currency': {'code': 'USD', 'name': 'USD'}},
            'state': 'EXECUTED',
            'to': 'Счет 90424923579946435907'}


@pytest.fixture()
def test_fixture_trans_good():
    return GOOD.copy()


@pytest.fixture()
def test_fixture_trans_not_good():
    return NOT_GOOD.copy()


def test_Transaction__repr__good(test_fixture_trans_good):
    assert Transaction(test_fixture_trans_good).__repr__() == "Transaction(data=2019-12-07T06:17:14.634890, " \
                                                              "description=Перевод организации, " \
                                                              "fromm=Visa Classic 2842878893689012, " \
                                                              "id_transaction=114832369, " \
                                                              "operation_amount={'amount': '48150.39', " \
                                                              "'currency': {'code': 'USD', 'name': 'USD'}}, " \
                                                              "state=EXECUTED, to=Счет 35158586384610753655)"


def test_Transaction__str__good(test_fixture_trans_good):
    assert Transaction(test_fixture_trans_good).__str__() == f'07.12.2019 Перевод организации\n' \
                                                             f'VisaClassic 2842 78** **** 9012 -> Счет **3655\n' \
                                                             f'48150.39 USD'


def test_Transaction__str__not_good(test_fixture_trans_not_good):
    assert Transaction(test_fixture_trans_not_good).__str__() == '08.12.2019 Открытие вклада\n' \
                                                                 'Неизвестно  -> Счет **5907\n' \
                                                                 '41096.24 USD'


def test_read_json(test_fixture_trans_good, test_fixture_trans_not_good):
    path = os.path.join(os.path.dirname(__file__), 'test_json.json')
    path_bad = os.path.join(os.path.dirname(__file__), 'test_json1.json')
    assert ReadJson.load_json(path) == [test_fixture_trans_good, test_fixture_trans_not_good]
    assert ReadJson.load_json(path_bad) is None
