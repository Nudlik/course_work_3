import os

import pytest

from models.readjson import ReadJson


def test_read_json(test_fixture_trans_good, test_fixture_trans_not_good):
    path = os.path.join(os.path.dirname(__file__), '../test_data/test_json.json')
    path_bad = os.path.join(os.path.dirname(__file__), 'test_json1.json')
    assert ReadJson.load_json(path) == [test_fixture_trans_good, test_fixture_trans_not_good]
    with pytest.raises(FileNotFoundError):
        assert ReadJson.load_json(path_bad)
