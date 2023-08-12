import pytest


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
    """ Фикстура словоря с from для тестов """
    return GOOD.copy()


@pytest.fixture()
def test_fixture_trans_not_good():
    """ Фикстура словоря без from для тестов """
    return NOT_GOOD.copy()
