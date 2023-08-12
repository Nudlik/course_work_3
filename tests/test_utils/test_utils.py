from utils import sort_transactions

import pytest


@pytest.mark.parametrize('transactions, expected', [
    ([{'date': 1, 'state': 'EXECUTED'}, {'date': 2, 'state': 'EXECUTED'}],
     [{'date': 2, 'state': 'EXECUTED'}, {'date': 1, 'state': 'EXECUTED'}]),
    ([{}, {}, {}, {}, {}, {}, {}, {}, {}], [{}, {}, {}, {}, {}])
])
def test_sort_transactions(transactions, expected):
    assert sort_transactions(transactions) == expected


def test_sort_transactions_rise():
    with pytest.raises(KeyError):
        sort_transactions([{'da': 1}])
    with pytest.raises(TypeError):
        sort_transactions([{'date': 1, 'state': 'EXECUTED'}], count='asd')
