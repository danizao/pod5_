"""Tests for the loaders module"""
# from life_expectancy.loaders import save_data, load_data
from life_expectancy.src.utils.loaders import save_data, load_data
from pytest import MonkeyPatch

BASE_DIR = Path(__file__).parent.parent / "data"
FIXTURES_DIR = Path(__file__).parent / "fixtures"
print(BASE_DIR)

def test_load_data(monkeypatch: MonkeyPatch) -> None:

    """testing if the load_data is called with the necessary arguments"""
    data_expected = 
    data = load_data("eu_life_expecancy_raw")
    assert data_actual = data_expected


def test_save_data(monkeypatch: MonkeyPatch) -> None:

    """testing if the save_data is called with the necessary arguments"""

    pass


