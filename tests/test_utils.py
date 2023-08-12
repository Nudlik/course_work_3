import pytest
from utils import sort_transactions


@pytest.mark.parametrize('transactions, expected', [
    ([{'date': 1, 'state': 'EXECUTED'}, {'date': 2, 'state': 'EXECUTED'}],
     [{'date': 2, 'state': 'EXECUTED'}, {'date': 1, 'state': 'EXECUTED'}]),
    ([{}, {}, {}, {}, {}, {}, {}, {}, {}], [{}, {}, {}, {}, {}])
])
def test_sort_transactions(transactions, expected):
    assert sort_transactions(transactions) == expected
