from life_expectancy.main import main
import pandas as pd
from pytest import MonkeyPatch



def test_main(
        monkeypatch: MonkeyPatch,
        eu_life_expectancy_raw: pd.DataFrame,
        pt_life_expectancy_expected: pd.DataFrame,
) -> None:
    """test the main function result against expected"""

    # Mock the inputs
    def _mock_load_data(*arg, **kwargs) -> pd.DataFrame:
        return eu_life_expectancy_raw
    
    monkeypatch.setattr("life_expectancy.loaders.pd.read_csv", _mock_load_data)

    def _mock_save_data(*arg, **kwargs) -> None:
        print("Data was saved")
    
    monkeypatch.setattr("life_expectancy.loaders.pd.DataFrame.to_csv", _mock_save_data)

    expected = pt_life_expectancy_expected
    actual = main().reset_index(drop = True)
    pd.testing.assert_frame_equal(
        actual, expected
        )

