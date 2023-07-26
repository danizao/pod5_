from pathlib import Path
import pandas as pd
import os

BASE_DIR = Path(__file__).parent / "data"
print("this is the BASE_DIR", BASE_DIR)
FIXTURES_DIR = Path(__file__).parent / "tests" / "fixtures"
print("this is the FIXTURE_DIR", FIXTURES_DIR)
print(FIXTURES_DIR)

def load_data(file: str) -> pd.DataFrame:
    """ load data from a file"""
    print('printing in load_data', BASE_DIR / file)
    return pd.read_csv(BASE_DIR / file, delimiter="\t")

def save_data(df: pd.DataFrame, file: str, dir: str = FIXTURES_DIR) -> None:
    """save a dataframe into a file in a directory"""
    print(os.path.join(dir, file))
    return df.to_csv(os.path.join(dir, file), index=False)

