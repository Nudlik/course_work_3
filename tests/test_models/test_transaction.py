import pytest

from models.transaction import Transaction


def test_Transaction__repr__good(test_fixture_trans_good):
    assert Transaction(test_fixture_trans_good).__repr__() == 'Transaction(date=2019-12-07T06:17:14.634890, ' \
                                                              'description="Перевод организации", ' \
                                                              'from="Visa Classic 2842878893689012", ' \
                                                              'id="114832369", ' \
                                                              'operation_amount="{"amount": "48150.39", ' \
                                                              '"currency": {"code": "USD", "name": "USD"}}", ' \
                                                              'state="EXECUTED", to="Счет 35158586384610753655")'


def test_Transaction__str__good(test_fixture_trans_good):
    assert Transaction(test_fixture_trans_good).__str__() == f'07.12.2019 Перевод организации\n' \
                                                             f'Visa Classic 2842 87** **** 9012 -> Счет **3655\n' \
                                                             f'48150.39 USD'


def test_Transaction__str__not_good(test_fixture_trans_not_good):
    assert Transaction(test_fixture_trans_not_good).__str__() == '08.12.2019 Открытие вклада\n' \
                                                                 'Неизвестно \x08 -> Счет **5907\n' \
                                                                 '41096.24 USD'


@pytest.mark.parametrize('card, expected', [
    ('1234567890123456', '1234 56** **** 3456'),
    ('2842878893689012', '2842 87** **** 9012'),
    ('35158586384610753655', '**3655'),
    ('abcdefg', None),
    (None, '')
])
def test_Transaction_mask_cards(card, expected):
    assert Transaction._Transaction__mask_cards(card) == expected


def test_Transaction_get_date(test_fixture_trans_good, test_fixture_trans_not_good):
    assert Transaction(test_fixture_trans_good)._Transaction__get_date() == '07.12.2019'
    assert Transaction(test_fixture_trans_not_good)._Transaction__get_date() == '08.12.2019'


def test_Transaction_get_from(test_fixture_trans_good, test_fixture_trans_not_good):
    assert Transaction(test_fixture_trans_good)._Transaction__get_from() == 'Visa Classic'
    assert Transaction(test_fixture_trans_not_good)._Transaction__get_from() == 'Неизвестно'


def test_Transaction_get_to(test_fixture_trans_good, test_fixture_trans_not_good):
    assert Transaction(test_fixture_trans_good)._Transaction__get_to() == 'Счет'
    assert Transaction(test_fixture_trans_not_good)._Transaction__get_to() == 'Счет'
